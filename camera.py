from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip


# Functions and Configurations
def Hikvision():
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

    print("Camera brand: HikVision")
    print("Camera IP: ", ipAddress)
    print("Device Name:", device_name)
    print("Device Number:", device_number)
    print("Model Number:", model_number)
    print("Serial Number:", serial_number)
    print("MAC Address:", mac_address,"\n")
    print("Done scanning")

    drive.quit()

def Revotech():
    username_elem = drive.find_element(By.ID, "userName")
    password_elem = drive.find_element(By.ID, "passWord")

    username_elem.clear()
    username_elem.send_keys("admin")

    password_elem.clear()
    password_elem.send_keys("Pax12345")

    password_elem.send_keys(Keys.RETURN)

    # Loading
    WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.ID,"btn_config")))
    tab = drive.find_element(By.ID,"btn_config")
    tab.click()

    WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.ID, 'contentframe')))
    drive.switch_to.frame(drive.find_element(By.ID, 'contentframe'))

    sub_tab = drive.find_element(By.XPATH, "//label[@id='laSystemInof']")
    sub_tab.click()

    WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='sSerial']")))

    serial_element = drive.find_element(By.XPATH, "//span[@id='sSerial']")
    mac_element = drive.find_element(By.XPATH, "//span[@id='sMAC']")

    serial_number = serial_element.text
    # pyperclip.copy(serial_number)
    mac_number = mac_element.text

    print("Camera brand: Revotech")
    print("Camera IP: ", ipAddress)
    print("Serial Number: ", serial_number)
    print("MAC: ", mac_number,"\n")
    print("Done scanning")

    drive.quit()

try_again = "Y"

print("IP Camera Serial and MAC Fetcher v.1")
print("Supports Revotech and HikVision brands\n")

while(try_again == "Y"):
    try:
        # Access the Camera through IP Address
        ipAddress=input("Enter IP Address: ")

        drive_options = Options()
        drive_options.add_experimental_option("detach", True)

        drive = webdriver.Chrome(options=drive_options)
        drive.get("http://"+ipAddress+"/")

        print("Please wait ...")
        # Wait for footer to be located
        WebDriverWait(drive, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='footer']")))

        # Check if the footer has Hikvision text or not
        footer_elem = drive.find_element(By.XPATH,"//div[@class='footer']")
        footer_id = footer_elem.text

        # Check what barnd of Camera
        if(footer_id.__contains__("Hikvision")):
            Hikvision()
        else:
            Revotech()
    except Exception as e:
        drive.quit()
        print("Error: ", e)

    try_again=input("Check another IP camera? (Y/N): ")

    match try_again:
        case "Y":
            try_again = "Y"
        case "y":
            try_again = "Y"
        case "n":
            try_again = "N"
            print("Press any key to exit...")
            input()
        case "N":
            try_again = "N"
            print("Press any key to exit...")
            input()
    