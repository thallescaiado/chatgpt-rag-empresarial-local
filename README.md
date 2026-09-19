# 🤖 Meu ChatGPT Empresarial Local (RAG + ChromaDB + Ollama)

Este projeto consiste em um **Pipeline RAG (Retrieval-Augmented Generation)** completo, privado e 100% offline, projetado para permitir que empresas consultem dados confidenciais (como relatórios de vendas, estoque e clientes) por meio de uma interface visual idêntica à do ChatGPT.

A solução resolve um grande problema do mercado: utilizar o poder das LLMs sem expor dados corporativos sensíveis a APIs de terceiros ou à internet pública.

---

## 🛠️ Tecnologias e Arquitetura Utilizadas

- **Cérebro da IA (LLM):** `Ollama` rodando o modelo local `Llama 3.2 (3B)`.
- **Orquestrador de Dados:** `LlamaIndex` para realizar a leitura, chunking e roteamento das consultas.
- **Banco de Dados Vetorial:** `ChromaDB` configurado de forma persistente para armazenar os embeddings dos documentos locais.
- **Modelo de Embeddings:** `BAAI/bge-small-en-v1.5` processado localmente via CPU.
- **Interface de Usuário:** `Streamlit` para criar uma experiência web fluida com histórico de chat e relatórios automatizados na barra lateral.

---

## 📈 Funcionalidades Implementadas

- [x] **Desafio Básico:** Carga dinâmica de múltiplos arquivos estruturados (`clientes.csv`, `produtos.csv`, `vendas.csv`).
- [x] **Desafio Avançado:** Indexação vetorial persistente em disco rígido utilizando banco de dados ChromaDB.
- [x] **Interface Avançada:** Chat estilo ChatGPT com gerenciamento de estado (memória de conversa) e botões de atalho para geração de relatórios de estoque crítico e distribuição geográfica.
- [x] **Privacidade Total:** Processamento local que dispensa o uso de chaves de API externas ou conexões com a internet.

---

## 📸 Interface de Usuário

Aqui está o visual da plataforma desenvolvida de forma integrada com o modelo local:

<img width="1897" height="841" alt="print_interface" src="https://github.com/user-attachments/assets/61c209c1-d788-4dda-aece-2ed323b7c678" />

<img width="1902" height="853" alt="print_resposta" src="https://github.com/user-attachments/assets/f97394b9-4548-45c4-8aaf-6e8ec9d7b0ca" />

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.12 ou superior instalado, além do [Ollama](https://ollama.com).

Com o Ollama ativo, baixe o modelo de linguagem no terminal:
```bash
ollama run llama3.2
```

### 2. Instalação das Dependências
Clone este repositório ou baixe os arquivos em uma pasta, abra o terminal no local e execute:
```bash
pip install -r requirements.txt
```

### 3. Inicialização do Chat
Execute o servidor local do Streamlit:
```bash
streamlit run app.py
```
O seu navegador abrirá automaticamente no endereço seguro de host local: `http://localhost:8501`.

## 🧠 Processo de Desenvolvimento & Engenharia de Prompts

Este projeto foi desenvolvido utilizando práticas modernas de **Engenharia de Prompts e Programação Assistida por IA**. 
Atuei como o Arquiteto de Soluções e Engenheiro de Software do pipeline, sendo responsável por:
- Desenhar a arquitetura de dados integrando LlamaIndex e ChromaDB.
- Mitigar problemas críticos de compatibilidade de pacotes de IA (como dependências do `Pillow` e `torchvision` no ambiente Windows).
- Configurar e garantir o isolamento e privacidade dos dados corporativos através do deploy local utilizando o Ollama.

