import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip

ipAddress = input("Enter ip address: ")

drive_options = Options()
drive_options.add_experimental_option("detach", True)

drive = webdriver.Chrome(options=drive_options)
drive.get("http://"+ipAddress+"/")

username_elem = drive.find_element(By.ID, "userName")
password_elem = drive.find_element(By.ID, "passWord")

username_elem.clear()
username_elem.send_keys("admin")

password_elem.clear()
password_elem.send_keys("Pax12345")

password_elem.send_keys(Keys.RETURN)

# Loading
# time.sleep(3)
WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.ID,"btn_config")))
tab = drive.find_element(By.ID,"btn_config")
tab.click()

# time.sleep(4)
WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.ID, 'contentframe')))
drive.switch_to.frame(drive.find_element(By.ID, 'contentframe'))

sub_tab = drive.find_element(By.XPATH, "//label[@id='laSystemInof']")
sub_tab.click()

# time.sleep(3)
WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='sSerial']")))

serial_element = drive.find_element(By.XPATH, "//span[@id='sSerial']")
mac_element = drive.find_element(By.XPATH, "//span[@id='sMAC']")

serial_number = serial_element.text
pyperclip.copy(serial_number)
mac_number = mac_element.text

print("Camera IP: ", ipAddress)
print("Serial Number: ", serial_number)
print("MAC: ", mac_number)

drive.quit()
