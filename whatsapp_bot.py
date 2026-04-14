from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Escanea el QR y pulsa ENTER")

# Espera a que cargue WhatsApp
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='grid']"))
)

chat_name = "Mama"

print("Buscando chat...")

chat = driver.find_element(By.XPATH, f"//span[@title='{chat_name}']")
chat.click()

print("Chat abierto ")

time.sleep(5)

messages = driver.find_elements(By.CSS_SELECTOR, "div.message-in, div.message-out")

if "0:" in last_message:
    print("Es un audio ")
else:
    print("Es texto ")

if messages:
    last_message = messages[-1].text
    print("Último mensaje:", last_message)
else:
    print("No hay mensajes aún")
    
