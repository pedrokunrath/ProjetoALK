# 📷 Projeto ALK - Automação de Download de Fotos

Este projeto foi desenvolvido para a **ALK** com o objetivo de automatizar o processo de download de **1620 fotos** do sistema de produtos, clicando manualmente nas posições específicas da tela para salvar as imagens.

## 🚀 Funcionalidades

- **Automação de Cliques**: O script automatiza cliques em posições específicas da tela para facilitar o processo de download das fotos.
- **Interrupção de Segurança**: O processo pode ser interrompido a qualquer momento pressionando a tecla **'q'**.
- **Feedback em Tempo Real**: O sistema informa o progresso da automação com mensagens no console.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pyautogui`: Para automatizar cliques na tela.
  - `time`: Para controlar o tempo entre as ações.
  - `threading`: Para executar o monitoramento de interrupção em paralelo.
  - `keyboard`: Para detectar a pressão da tecla 'q' e parar o processo.

## 📂 Estrutura do Projeto

```plaintext
ProjetoALK/
│
├── main.py                  # Script principal de automação
├── README.md                # Documentação do projeto
└── ponteiro.py              # Script para capturar a posição do ponteiro
