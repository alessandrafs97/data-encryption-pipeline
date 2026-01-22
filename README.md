# Secure Data Encryption Pipeline (AES-256)


## 🇧🇷 Português

Este projeto reproduz um **processo real de criptografia de dados aplicado a ETL**, originalmente implementado em um ambiente corporativo utilizando **JETL**.

O foco é a **proteção de campos sensíveis** durante o processamento de grandes arquivos, seguindo padrões comuns em pipelines de dados de produção.

---

###  Contexto

Em ambientes de engenharia de dados, informações sensíveis como documentos pessoais e identificadores de clientes precisam ser criptografadas antes de serem armazenadas ou distribuídas para sistemas downstream.

Este projeto simula esse cenário por meio da leitura de arquivos CSV de grande volume, criptografando colunas específicas de forma eficiente e controlada.

---

###  Estratégia de Criptografia

A estratégia de criptografia utilizada neste projeto é a mesma aplicada no processo original em produção:

- **AES-256 (Advanced Encryption Standard)**
- **Modo CBC (Cipher Block Chaining)** com **IV fixo zerado (16 bytes)**
- **Padding PKCS7**
- **Derivação de chave com PBKDF2HMAC**
  - Algoritmo: SHA-256  
  - Iterações: 65.536
- **Codificação Base64** para persistência dos dados criptografados

---

###  Processamento de Dados (ETL)

O pipeline foi estruturado para lidar com grandes volumes de dados, utilizando:

- Leitura de arquivos CSV
- Processamento **em blocos (chunk processing)** para controle de memória
- Identificação dinâmica das colunas sensíveis pelo header
- Criptografia linha a linha apenas dos campos necessários
- Escrita incremental do arquivo de saída

Esse modelo reflete práticas reais de ETL utilizadas em ambientes produtivos.

---
###  Estrutura do Projeto

```text
data-encryption-pipeline/
│
├── src/
│   ├── encryption.py        # Criptografia AES-256 + derivação de chave
│   └── file_processor.py   # Processamento em blocos e escrita de CSV
│
├── data/
│   └── input_sample.csv    # Dados fictícios para simulação
│
└── README.md
```
---
###  Autora

Alessandra Silva
Engenheira de Dados | ETL | Segurança e Criptografia de Dados

