from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def macaddress_access_control(driver, block=False):

    """ Function that blocks or allows access to have internet connection.

    The steps it performs are: enter the router,login and go to 2.4 GHz secction, then go to Mac Address Control section,
    if the block parameter is true the function will block the mac addresses that are listed, however if it is false 
    it will allows all mac adresses to be able to connect. By default the block parameter is in false.
    """

    # router login credentials
    username = ""
    password = ""

    # wait until find user field and after insert the user 
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "UserName")).send_keys(username)

    # find password field and insert the password
    driver.find_element(By.ID, "Password").send_keys(password)

  # click login button 
    driver.find_element(By.CLASS_NAME, "submitBtn").click()

    # wait for the page to load
    time.sleep(8)

    try:
        # if there is some error in login, it will appear an alert
        alert = WebDriverWait(driver, timeout=10).until(EC.alert_is_present())
        alert.accept()
        # close session
        driver.close()
    except:
        pass
        
    # enter in Inalámbrico de 2.4 GHz secction 
    driver.find_element(By.LINK_TEXT, "Inalámbrico de 2.4 GHz").click()
     # wait for the page to load
    time.sleep(10)

    # enter in Control de direcciones MAC secction 
    driver.find_element(By.CSS_SELECTOR, 'a[title="Control de direcciones MAC"]').click()
    # wait for the page to load
    time.sleep(5)

    #Get the Select element to choose some option 
    select = Select(driver.find_element(By.ID, "MacAddressFilterType"))
    
    #  if block parameter is true, this option will be used
    option_one = 'Blacklist: device must NOT be listed below.' 

    # if block parameter is false, this option will be used
    option_two = 'None: Any device can try to connect.'

    # choose the option one or two
    select.select_by_visible_text(option_one if block else option_two)
    # wait for the page to load
    time.sleep(5)

    # click in apply button
    driver.find_element(By.XPATH, '//*[@id="ApplyButton"]/input').click()
    time.sleep(8)

    driver.close()

# initialize the Chrome driver
driver = webdriver.Chrome()

#router configuration url
driver.get("http://192.168.0.1/")

# call to the function 
macaddress_access_control(driver, True)





