import os
import streamlit as st
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# =====================================================================
# CONFIGURAÇÃO DA PÁGINA (ESTILO CHATGPT)
# =====================================================================
st.set_page_config(page_title="Meu ChatGPT RAG", page_icon="🤖", layout="wide")

# Aplica um tema escuro elegante nativo via CSS
st.markdown("""
    <style>
    .stApp { background-color: #212121; color: #ececf1; }
    .stChatMessage { border-radius: 10px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Cache do Pipeline para o sistema carregar instantaneamente
@st.cache_resource
def inicializar_pipeline_rag():
    Settings.llm = Ollama(model="llama3.2", request_timeout=120.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    documents = SimpleDirectoryReader("./dados").load_data()
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("meu_pipeline_rag")
    
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    return index.as_query_engine()

query_engine = inicializar_pipeline_rag()

# =====================================================================
# INTERFACE VISUAL - BARRA LATERAL (SIDEBAR)
# =====================================================================
with st.sidebar:
    st.title("⚙️ Painel de Controle")
    st.write("Use os botões abaixo para disparar relatórios automáticos:")
    
    if st.button("📊 Relatório de Estoque Crítico", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Gerar Relatório de Estoque Crítico"})
        prompt = "Analise o arquivo produtos.csv. Quais itens têm estoque menor que 30 unidades? Liste o nome e a quantidade."
        resposta = query_engine.query(prompt)
        st.session_state.messages.append({"role": "assistant", "content": str(resposta)})
        
    if st.button("🗺️ Clientes por Região", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Gerar Relatório Geográfico de Clientes"})
        prompt = "Agrupe e liste todos os clientes pelo nome da cidade onde moram, usando o clientes.csv."
        resposta = query_engine.query(prompt)
        st.session_state.messages.append({"role": "assistant", "content": str(resposta)})
        
    st.divider()
    if st.button("🗑️ Limpar Histórico de Conversa", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# =====================================================================
# CORPO PRINCIPAL DO CHAT (ESTILO CHATGPT)
# =====================================================================
st.title("🤖 Meu ChatGPT Empresarial Local")
st.caption("Pergunte qualquer coisa sobre os seus arquivos CSV de Produtos, Clientes e Vendas.")

# Inicializa o histórico de mensagens na tela
if "messages" not in st.session_state:
    st.session_state.messages = []

# Desenha todas as mensagens anteriores na tela (com balões de chat)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Campo de entrada de texto inferior (Igualzinho ao do ChatGPT)
if prompt_usuario := st.chat_input("Envie uma mensagem para a IA..."):
    # Mostra a pergunta do usuário na tela
    with st.chat_message("user"):
        st.write(prompt_usuario)
    st.session_state.messages.append({"role": "user", "content": prompt_usuario})
    
    # Processa a resposta usando o LlamaIndex
    with st.chat_message("assistant"):
        with st.spinner("Pensando localmente..."):
            resposta_ia = query_engine.query(prompt_usuario + " Responda em português de forma clara.")
            st.write(str(resposta_ia))
    st.session_state.messages.append({"role": "assistant", "content": str(resposta_ia)})
