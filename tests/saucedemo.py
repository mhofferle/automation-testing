import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))) # Añadimos el directorio padre al path para importar utils.helpers
from utils.helpers import get_driver, login, USERNAME, PASSWORD

# Fixture para inicializar y cerrar el driver. Con un fixture evitamos repetir código porque en los tests vamos a usar el driver varias veces
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Test de login: Verifica que el usuario pueda iniciar sesión correctamente y sea redirigido a la página de productos/inventario
def test_login(driver):
    
    login(driver, USERNAME, PASSWORD)
    
    assert "inventory.html" in driver.current_url
    
    title = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]').text
    assert title == "Products"


# Test de catálogo: Verifica que los productos, menú, filtros y carrito se muestren correctamente en la web
def test_catalog(driver):
    
    login(driver, USERNAME, PASSWORD)
    
    title = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]').text
    assert title == "Products"
    
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    
    menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    assert menu.is_displayed()
    
    filters = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    assert filters.is_displayed()
    
    cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    assert cart.is_displayed()
    
    first_product_name = products[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
    assert first_product_name == "Sauce Labs Backpack"
    
    first_product_price = products[0].find_element(By.CLASS_NAME, 'inventory_item_price').text
    assert first_product_price == "$29.99"
    
    print(first_product_name, first_product_price)

# Test de carrito: Verifica que se pueda agregar un producto al carrito, que se muestre el badge correspondiente y que al ir al carrito se vea el producto agregado
def test_cart(driver):
    login(driver, USERNAME, PASSWORD)
    
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    
    products[0].find_element(By.TAG_NAME, 'button').click()
    
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert badge.text == '1'
    
    cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    assert "cart.html" in driver.current_url
    cart_product = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
    assert cart_product == "Sauce Labs Backpack"