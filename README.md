# 🤖 Tracker Bot: Web Scraping & Alertas via Telegram

Um agente autônomo desenvolvido em Python focado em extração de dados (Web Scraping) e automação de alertas em tempo real. O robô varre e-commerces em busca de oportunidades de preços e notifica o usuário diretamente no smartphone.

## ⚙️ Tecnologias Utilizadas (Arsenal)
* **Linguagem:** Python
* **Mineração de Dados (Scraping):** BeautifulSoup4 e Requests
* **Integração de Mensageria:** API Oficial do Telegram (via HTTP POST)
* **Controle de Fluxo:** Lógica de paginação dinâmica e controle de *Rate Limiting* (Time sleep) para evitar bloqueios do servidor alvo.

## 🚀 Arquitetura e Funcionalidades
1. **Infiltração e Varredura:** O script faz requisições HTTP sequenciais, navegando automaticamente por múltiplas páginas do catálogo alvo.
2. **Parsing de HTML:** O código-fonte da página é fatiado usando BeautifulSoup, extraindo cirurgicamente as tags e classes referentes a títulos e preços.
3. **Data Cleaning e Conversão:** Os dados de texto (strings) sofrem limpeza de encoding e caracteres monetários, sendo convertidos para valores matemáticos (floats) para avaliação lógica.
4. **Gatilho de Notificação:** Uma condicional de negócio avalia se o preço do item está abaixo do limite estipulado (£20).
5. **Comunicação Externa:** Se o gatilho for acionado, o script se conecta à API do Telegram e envia um relatório formatado instantaneamente para o dispositivo do usuário.

## 💻 Como Rodar o Projeto
1. Instale as dependências: `pip install requests beautifulsoup4`
2. Crie um bot no Telegram através do BotFather para obter o seu `HTTP API Token`.
3. Descubra o seu `CHAT_ID` enviando uma mensagem para o bot e lendo a resposta da API do Telegram.
4. Insira as credenciais no arquivo `scraper.py`.
5. Execute o robô no terminal: `python scraper.py`
