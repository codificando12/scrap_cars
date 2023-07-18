from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def run():
    
    
    driver = webdriver.Chrome(executable_path = r'C:/chrome-driver/linux/chromedriver.exe')
    
    driver.get('https://www.kijijiautos.ca/cars/#od=down&sb=rel&st=FSBO')
    cars = driver.find_elements(By.TAG_NAME, 'article')
    first_art = 1
    list_div = 1
    
    driver.implicitly_wait(2)
    # //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[1]
    div_path = f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div'
    count_articles = 0
    for i in range(0, 200):
        
        print(div_path)
        elements_div_path = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, div_path))) 
        articles = elements_div_path.find_elements(By.TAG_NAME, 'article')
        print(len(articles))
        for article in range(len(articles) + 1):
            print(div_path)
            
                # click_article = WebDriverWait(driver, 10).until(
                #     EC.element_to_be_clickable(
                #     (By.XPATH, f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div{[article + 1]}/article')
                #     )
                # )
            click_article = driver.find_element(By.XPATH, f'{div_path}/div{[article + 1]}') 
                #     )')
            div_class = click_article.get_attribute('class')
            print(div_class)
            if div_class == 'h2GjMu':
                continue
            else:
                time.sleep(2)
                click_article.click()
                title = driver.find_element(By.TAG_NAME, 'h1')
                print(title.text)
                current_url = driver.current_url
                print(current_url)
                time.sleep(1)
                try:
                    WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[3]/section/div/nav/div[2]/button[1]/span/span'))
                    ).click()
                    time.sleep(0.5)
                    number = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[3]/section/div/nav/div[2]/button[1]/span/span')
                    print(number.text)
                    driver.back()
                    time.sleep(1)
                    # driver.execute_script("window.scrollBy(0, 50);")
                except:
                    print('no phone')
                    driver.back()
                    time.sleep(1)
                    print(article)
                    time.sleep(1)
                    # driver.execute_script("window.scrollBy(0, 50);")
                    
        first_art = 1
        list_div += 1
        div_path = f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div{[list_div]}'
        print(count_articles)
        
            
    time.sleep(30)
    
    time.sleep(30)
    
if __name__ == "__main__":
    run()

#  //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[9]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[10]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[11]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[2]/div[6]/
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[3]/div[21]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[10]/div[7]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[24]/div[20]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[24]/div[6]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[23]/div[20]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[1]/div[21]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[1]/div[1]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[10]
#  //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[11]/article

# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div

# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[1]/article
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[2]/article
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[2]/div[22]

# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[7]/div[1]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[6]/div[20]
# //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[24]
# data-testid