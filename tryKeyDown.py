from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r'C:/chrome-driver/linux/chromedriver.exe')
    
driver.get('https://www.kijijiautos.ca/cars/#od=down&sb=rel&st=FSBO')
count = 1
xpath = f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div'

time.sleep(3)
for i in range(10000):
    try:
        div_articles = driver.find_element(By.XPATH, xpath)
        articles = div_articles.find_elements(By.TAG_NAME, 'article')
        for j in range(articles):
            click_article = driver.find_element(By.XPATH, f'{xpath}/div[{j+1}]')
            click_article.click()
            time.sleep(3)
            driver.back()
        count += 1
    except:
        driver.execute_script("window.scrollBy(0, 50);")
        time.sleep(0.5)
        count += 1
        f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[{count}]'
    print(i)

time.sleep(1000)

# listItemPage-0