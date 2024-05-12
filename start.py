from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Configura las opciones del controlador
options = webdriver.ChromeOptions()

# Crea el controlador
driver = webdriver.Chrome(options=options)

# Ahora puedes usar el controlador para navegar a una URL
url = "https://gmail.com/"
driver.get(url)

button ="//span[contains(text(), 'Crear cuenta')]"

crear_cuenta = driver.find_element(By.XPATH,button)
crear_cuenta.click()

spam ="//span[contains(text(), 'Para uso personal')]"
uso_personal = driver.find_element(By.XPATH,spam)

uso_personal.click()

nombre = "Migel"
rellenar_nombre = driver.find_element(By.NAME,"firstName")
rellenar_nombre.clear()
rellenar_nombre.send_keys(nombre,Keys.ENTER)

lastname = "Torrenciega"

rellenar_nombre = driver.find_element(By.NAME,"lastName")
rellenar_nombre.clear()
rellenar_nombre.send_keys(lastname,Keys.ENTER)

# fecha

dey= 15
month =11
year ="2004"
WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,"day"))
)
dey_PUT = driver.find_element(By.ID,"day")
time.sleep(3)
dey_PUT.send_keys("15")

# Conseguir un elemento de un select 
# se crea una instancia de el elemento a seleccionar 
month_select = Select(driver.find_element(By.ID,"month"))
# se selecciona el value
month_select.select_by_value("2")

year = driver.find_element(By.NAME,"year")

year.send_keys("2004")


# genero

gender = Select(driver.find_element(By.ID,"gender"))
# se selecciona el value
gender.select_by_value("2")

year.send_keys(Keys.ENTER)

WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,"selectionc2"))
)
seleccion_nombre_correo = driver.find_element(By.ID,"selectionc2")
time.sleep(3)
seleccion_nombre_correo.click()

button ="//span[contains(text(), 'Siguiente')]"
sig = driver.find_element(By.XPATH,button)
time.sleep(3)
sig.click()

# contraseña
WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.NAME,"Passwd"))
)
year = driver.find_element(By.NAME,"Passwd")
year.send_keys("Jc.123456@")

WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.NAME,"PasswdAgain"))
)
year = driver.find_element(By.NAME,"PasswdAgain")
year.send_keys("Jc.123456@")

button ="//span[contains(text(), 'Siguiente')]"
sig = driver.find_element(By.XPATH,button)
time.sleep(3)
sig.click()

"""
input_element.clear()
input_element.send_keys("pokemon Reolader",Keys.)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"X")
link.click()
"""

time.sleep(100000)

driver.quit()