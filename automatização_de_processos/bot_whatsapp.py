from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do navegador
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("Escaneie o QR code...")

# Espera o WhatsApp Web carregar
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "side"))
)

print("Bot iniciado")

ultima_mensagem_respondida = ""

def enviar_mensagem(texto):
    try:
        # XPATH atualizado para a caixa de texto
        caixa_texto = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        caixa_texto.send_keys(texto)
        caixa_texto.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Erro ao enviar: {e}")

def responder_mensagem():
    global ultima_mensagem_respondida
    try: 
        # Pega todos os containers de mensagem
        mensagens = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in")]')

        if mensagens:
            # Pega o texto da última mensagem recebida (apenas as que entram)
            ultima_mensagem = mensagens[-1].text.lower()

            if ultima_mensagem != ultima_mensagem_respondida:
                print(f"Nova mensagem: {ultima_mensagem}")
                
                if "oi" in ultima_mensagem:
                    enviar_mensagem("Olá! Eu sou um bot de automação.")
                elif "tchau" in ultima_mensagem:
                    enviar_mensagem("Até mais!")
                else:
                    enviar_mensagem("Estou aprendendo ainda.")

                # Atualiza para não responder a mesma mensagem de novo
                ultima_mensagem_respondida = ultima_mensagem
    
    except Exception as e:
        print("Erro ao processar mensagem:", e)

# Loop principal
while True:
    responder_mensagem()
    time.sleep(3)
