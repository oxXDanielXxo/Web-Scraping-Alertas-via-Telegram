import requests
from bs4 import BeautifulSoup
import time

# 1. Credenciais de Comunicação (As chaves da base)
TOKEN_TELEGRAM = "COLOQUE_SEU_TOKEN_AQUI"
CHAT_ID = "COLOQUE_SEU_CHAT_ID_AQUI"

def enviar_alerta(mensagem):
    """Função tática para disparar mensagens no Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    dados = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=dados)

# 2. Configuração da Missão
paginas_para_raspar = 2 # Reduzimos para 2 páginas para um teste mais rápido
alvo_preco_maximo = 20.00 # O gatilho do nosso alerta (£20)

print("🤖 Iniciando patrulha de preços...")
enviar_alerta("🤖 Patrulha de preços iniciada. Escaneando o mercado...")

for i in range(1, paginas_para_raspar + 1):
    url_alvo = f"http://books.toscrape.com/catalogue/page-{i}.html"
    resposta = requests.get(url_alvo)
    resposta.encoding = 'utf-8' 
    
    if resposta.status_code == 200:
        sopa = BeautifulSoup(resposta.text, "html.parser")
        produtos = sopa.find_all("article", class_="product_pod")
        
        for item in produtos:
            titulo = item.h3.a["title"]
            
            # Limpeza avançada: Tira o 'Â' e o '£' para sobrar SÓ o número
            preco_texto = item.find("p", class_="price_color").text.replace("Â", "").replace("£", "")
            
            # Transforma o texto '19.99' em matemática (Float/Decimal)
            preco_matematico = float(preco_texto)
            
            # 3. A Lógica do Gatilho
            if preco_matematico < alvo_preco_maximo:
                msg = f"🚨 OPORTUNIDADE DETECTADA!\n📚 {titulo}\n💰 Apenas: £{preco_matematico}"
                print(f"Alerta disparado para o livro: {titulo}")
                enviar_alerta(msg)
                
        time.sleep(1) # Robô respira 1 segundo por página