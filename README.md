<p align="center">
   <img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=google-translate" />
  <img src="https://img.shields.io/badge/Language-Português-green?style=for-the-badge&logo=google-translate" />
</p>

<p align="center">
  🔐 ETL Data Encryption Pipeline · AES-256 · Security First
</p>

# Data Encryption Pipeline with Sensitive Data Protection

This project implements an **ETL-style data encryption pipeline** designed to protect sensitive fields during large-scale data processing.

The main objective is to ensure that confidential information (such as personal documents and identifiers) is securely encrypted before storage or downstream consumption, following patterns commonly used in corporate data engineering environments.

---

## Methodology and Technologies Involved

### Orchestration
- Script-based ETL flow inspired by batch processing jobs commonly executed in JETL environments.

### Data Processing
- CSV file ingestion using Python
- Chunk-based processing to handle large volumes of data efficiently
- Dynamic identification of sensitive columns via file headers

### Encryption
- **AES-256 symmetric encryption**
- **CBC (Cipher Block Chaining) mode**
- **PKCS7 padding**
- **PBKDF2HMAC key derivation**
  - Hash algorithm: SHA-256
  - Iterations: 65,536
- **Base64 encoding** for encrypted values

### Security Design
- Fixed initialization vector (IV) with 16 zeroed bytes (as used in the original production implementation)
- Clear separation between key derivation and encryption logic
- Encryption applied only to required sensitive fields

---

## Features

- **Selective Field Encryption**  
  Only sensitive columns (e.g. `CPF`, `NUMERODOCUMENTO`) are encrypted, preserving the integrity of non-sensitive data.

- **Chunk Processing**  
  Large files are processed in blocks to avoid memory exhaustion and ensure stability.

- **Production-Oriented Design**  
  The pipeline structure mirrors real-world corporate ETL jobs, focusing on performance, reliability, and maintainability.

- **Reusable Encryption Logic**  
  Encryption and key derivation are implemented in isolated modules, enabling reuse in other pipelines.

---

## Project Structure

```text
data-encryption-pipeline/
│
├── src/
│   ├── encryption.py        # AES-256 encryption and key derivation
│   └── file_processor.py    # Chunk-based CSV processing
│
├── data/
│   └── input_sample.csv     # Fake sample data for demonstration
│
└── README.md
```

---


# Pipeline de Criptografia de Dados Sensíveis

Este projeto implementa um **pipeline de criptografia de dados no contexto de ETL**, inspirado em uma implementação real utilizada em ambiente corporativo com **JETL**.

O objetivo principal é garantir que **campos sensíveis sejam criptografados** durante o processamento de dados em larga escala, antes do armazenamento ou consumo por sistemas downstream.

---

## Metodologia e Tecnologias Envolvidas

### Orquestração
- Fluxo de ETL baseado na execução de scripts Python, seguindo o modelo de jobs batch comumente utilizados em ambientes JETL.

### Processamento de Dados
- Leitura de arquivos CSV
- Processamento em blocos (*chunk processing*) para controle de uso de memória
- Identificação dinâmica das colunas sensíveis a partir do header do arquivo
- Escrita incremental do arquivo de saída

### Criptografia
- **Criptografia simétrica AES-256**
- **Modo CBC (Cipher Block Chaining)**
- **Padding PKCS7**
- **Derivação de chave utilizando PBKDF2HMAC**
  - Algoritmo de hash: SHA-256
  - Número de iterações: 65.536
- **Codificação Base64** para persistência dos dados criptografados

### Design de Segurança
- Utilização de **IV fixo com 16 bytes zerados**, conforme implementação original em produção
- Separação clara entre a lógica de derivação de chave e a lógica de criptografia
- Criptografia aplicada apenas aos campos considerados sensíveis

---

## Funcionalidades

- **Criptografia Seletiva de Campos**  
  Apenas colunas sensíveis (como `CPF` e `NUMERODOCUMENTO`) são criptografadas, mantendo os demais dados íntegros.

- **Processamento em Blocos**  
  Arquivos de grande volume são processados em partes, garantindo performance e estabilidade.

- **Estrutura Orientada à Produção**  
  O pipeline reflete práticas reais de ETL corporativo, com foco em confiabilidade, desempenho e manutenção.

- **Lógica de Criptografia Reutilizável**  
  Implementação modular que permite reutilização da criptografia em outros pipelines e projetos.

---

## Estrutura do Projeto

```text
data-encryption-pipeline/
│
├── src/
│   ├── encryption.py        # Criptografia AES-256 e derivação de chave
│   └── file_processor.py    # Processamento em blocos e escrita de CSV
│
├── data/
│   └── input_sample.csv     # Dados fictícios para demonstração
│
└── README.md
```

## Autora

Alessandra Silva
Engenheira de Dados | ETL | Segurança e Criptografia de Dados
