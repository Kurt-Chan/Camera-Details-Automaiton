from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ipAddress=input("Enter ip address: ")

drive_options = Options()
drive_options.add_experimental_option("detach", True)

drive = webdriver.Chrome(options=drive_options)
drive.get("http://"+ipAddress+"/")

username_elem = drive.find_element(By.ID, "username")
password_elem = drive.find_element(By.ID, "password")

username_elem.clear()
username_elem.send_keys("admin")

password_elem.clear()
password_elem.send_keys("Pax12345")

password_elem.send_keys(Keys.RETURN)

# Loading
WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Configuration']")))

# Navigating to Configuration Tab
tab = drive.find_element(By.XPATH,"//a[text()='Configuration']")
tab.click()



WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='item']/span[contains(text(), 'Device Name')]/following-sibling::span/input")))
# Find the elements containing device name, device number, model number, and serial number
device_name_element = drive.find_element(By.XPATH, "//div[@class='item']/span[contains(text(), 'Device Name')]/following-sibling::span/input")
device_number_element = drive.find_element(By.XPATH,"//div[@class='item']/span[contains(text(), 'Device No.')]/following-sibling::span/input")
model_element = drive.find_element(By.XPATH, "//div[@class='item']/span[contains(text(), 'Model')]/following-sibling::span")
serial_element = drive.find_element(By.XPATH, "//div[@class='item']/span[contains(text(), 'Serial No.')]/following-sibling::span")


# Extract the text from the elements
device_name = device_name_element.get_attribute("value")
device_number = device_number_element.get_attribute("value")
model_number = model_element.get_attribute("title")
serial_number = serial_element.get_attribute("title")


# Finding the MAC Address
net_tab = drive.find_element(By.XPATH, "//div[@title='Network']")
net_tab.click()

WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@ng-model='oEthernetParams.szMacAddress']")))
mac_element = drive.find_element(By.XPATH, "//input[@ng-model='oEthernetParams.szMacAddress']")
mac_address = mac_element.get_attribute("value")

print("Camera IP: ", ipAddress)
print("Device Name:", device_name)
print("Device Number:", device_number)
print("Model Number:", model_number)
print("Serial Number:", serial_number)
print("MAC Address:", mac_address)

drive.quit()