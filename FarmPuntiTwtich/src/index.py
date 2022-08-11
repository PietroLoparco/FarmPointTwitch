from time import sleep
from Settings import Setting as S   #memmotron
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

mode: str = By.CSS_SELECTOR

opt: Options = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

driver: Chrome = Chrome(service=Service(ChromeDriverManager().install()), chrome_options=opt)

if driver.find_elements(mode, S.CONTROL):
    print("Twitch already open")    
else:
    driver.get(S.LINK)

while True:

    try:
        driver.find_element(mode, S.BUTTON_CHEST).click()
        print("Clicked")

    except:
        print("Element still absent")

    sleep(S.TIME)

