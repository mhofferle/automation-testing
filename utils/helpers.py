from selenium import webdriver
from selenium.webdriver.common.by import By # Para poder localizar elementos en la página web
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # Gestiona automáticamente la instalación y actualización del driver de Chrome
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Definimos las variables para los tests
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
    
    # Instancia de Service que gestiona el driver de Chrome. Instala y configura el servicio del driver
    chrome_service = Service(ChromeDriverManager().install())
    
    # Iniciamos una instancia del navegador Chrome controlada por Selenium
    driver = webdriver.Chrome(service=chrome_service) 
    
    # Esperamos 5 segundos para asegurarnos que el navegador se inicie correctamente
    time.sleep(5)  
    
    return driver


# Función para hacer login completando los datos y click en el botón de login, esperando a que los elementos estén presentes con explicit waits
def login(driver, username, password):
    driver.get(URL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()