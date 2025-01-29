# 🧠 CrewAI com modelo de IA Llama 3.1 e Ollama

Este projeto utiliza a biblioteca **CrewAI** para simular um time Scrum, utilizando o modelo **Llama 3.1** rodando localmente via **Ollama**.

## 🛠️ Requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes requisitos atendidos:

### 1️⃣ Instalar o Ollama

O Ollama é necessário para rodar o modelo de IA localmente. Escolha sua plataforma e instale:

- **Windows**:
  - Baixe e instale o Ollama: [ollama.com/download](https://ollama.com/download)
  - Reinicie o terminal após a instalação.

- **Linux**:
  ```sh
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- **macOS**:
  ```sh
  brew install ollama
  ```

### 2️⃣ Baixar o Modelo Llama 3.1

Após instalar o Ollama, baixe o modelo Llama 3.1 executando o seguinte comando:

```sh
ollama pull llama3.1
```

Isso pode levar alguns minutos, pois o modelo será baixado e armazenado localmente.

### 3️⃣ Instalar o Python e Configurar o Ambiente Virtual

- Certifique-se de ter o **Python 3.9+** instalado. Verifique com:
  ```sh
  python --version
  ```
- Crie e ative um ambiente virtual:
  ```sh
  python -m venv venv
  ```
  - No **Windows**:
    ```sh
    venv\Scripts\activate
    ```
  - No **Linux/macOS**:
    ```sh
    source venv/bin/activate
    ```

### 4️⃣ Instalar as Dependências do Projeto

Após ativar o ambiente virtual, instale as dependências necessárias:
```sh
pip install -r requirements.txt
```

## 🚀 Como Rodar o Projeto

1. Certifique-se de que o **Ollama** está rodando e o modelo **Llama 3.1** foi baixado.
2. Ative o ambiente virtual conforme explicado acima.
3. Execute o script principal:
   ```sh
   python main.py
   ```

O projeto irá simular uma equipe Scrum, com agentes desempenhando diferentes papéis utilizando IA.

## 📝 Sobre o Projeto

Este projeto demonstra como integrar a **CrewAI** com um modelo **Llama 3.1** rodando localmente via **Ollama**, possibilitando interações inteligentes entre agentes de um time ágil.

📌 Se tiver dúvidas, sinta-se à vontade para abrir uma issue! 😊

