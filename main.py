from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import pandas as pd

toWishList = []
while True:
    if datetime.now().time().hour == 22:
        toWishList.clear()
        df = pd.read_csv('memory.csv')
        nextDay = datetime.now().date() + timedelta(days=1)
        results = df.loc[df['date'] == f'{nextDay.day}/{nextDay.month}/{nextDay.year}']
        for one in results.index:
            toWishList.append(df.loc[one])

    if datetime.now().time().hour == 0 and len(toWishList)!=0:
        #your chrome driver path goes down here
        chromeDriverPath = "chromedriver.exe"
        ch_options = Options()
        ch_options.add_argument("--silent")
        ch_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3641.0 Safari/537.36 ")
        #user data path goes down here
        ch_options.add_argument("user-data-dir=E:\\Work\Blog\\birthday automation\\Default")
        driver = webdriver.Chrome(executable_path = chromeDriverPath, options = ch_options)
        driver.get("https://web.whatsapp.com")

        
        for one in toWishList:
            searchBox = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//div[@title='Search input textbox']")))
            searchBox.send_keys(one['number'])
            searchBox.send_keys(Keys.RETURN)
            messageBox = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//div[@title='Type a message']")))
            messageBox.click()
            messageBox.send_keys(one['message'])
            messageBox.send_keys(Keys.RETURN)
       
        sleep(1.5)
        driver.quit()
