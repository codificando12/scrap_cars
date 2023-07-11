from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run():
    
    
    driver = webdriver.Chrome(executable_path = r'C:/chrome-driver/linux/chromedriver.exe')
    
    driver.get('https://www.kijijiautos.ca/cars/#od=down&sb=rel&st=FSBO')
    time.sleep(3)
    cars = driver.find_elements(By.TAG_NAME, 'article')
    print(len(cars))

    for i in range(len(cars)):
        try:
            driver.find_element(By.XPATH, f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div{[i + 1]}').click()
            time.sleep(3)
            title = driver.find_element(By.TAG_NAME, 'h1')
            print(title.text)
            driver.back()
            time.sleep(10)
            print(i)
        except:
            print('there no element')
            continue
    time.sleep(30)
    
    time.sleep(30)
    
if __name__ == "__main__":
    run()

#  //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[9]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[10]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[11]