from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def run():
    
    
    driver = webdriver.Chrome(executable_path = r'C:/chrome-driver/chromedriver.exe')
    
    driver.get('https://www.kijijiautos.ca/cars/#od=down&sb=rel&st=FSBO')
    cars = driver.find_elements(By.TAG_NAME, 'article')
    first_art = 1
    list_div = 1
    
    driver.implicitly_wait(2)
    # //*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div/div[1]
    div_path = f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div'
    total_articles = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[1]/h2')
    total_num_articles = int(total_articles.text.split()[0].replace(",", ""))
    print(total_articles)
    count_articles = 0

    while count_articles != total_num_articles:
        
        print(div_path)
        try:
            elements_div_path = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, div_path))) 
        except:
            driver.execute_script("window.scrollBy(0, 2000);")
            print("scrolled down")
            elements_div_path = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, div_path))) 
        articles = elements_div_path.find_elements(By.TAG_NAME, 'article')
        advertisement = elements_div_path.find_elements(By.CLASS_NAME, 'h2GjMu')
        print(f"total for the loop:  {len(articles) + len(advertisement)}")
        for article in range(len(articles) + len(advertisement)):
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
                time.sleep(1)
                
                try:
                    click_article.click()
                except:
                    try:
                        driver.execute_script("window.scrollBy(0, 500);")
                        print("scrolled down")
                        click_article.click()
                    except:
                        continue
                title = driver.find_element(By.TAG_NAME, 'h1')
                print(title.text)
                current_url = driver.current_url
                print(current_url)
                time.sleep(1)
                try:
                    WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[3]/section/div/nav/div[2]/button[1]/span/span'))
                    ).click()
                    time.sleep(1)
                    number = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[3]/section/div/nav/div[2]/button[1]/span/span')
                    print(number.text)
                    driver.back()
                    time.sleep(1)
                    count_articles += 1
                    # driver.execute_script("window.scrollBy(0, 50);")
                except:
                    print('no phone')
                    driver.back()
                    time.sleep(1)
                    print(article)
                    time.sleep(1)
                    count_articles += 1
                    # driver.execute_script("window.scrollBy(0, 50);")
        
                 
        first_art = 1
        list_div += 1
        div_path = f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div{[list_div]}'
        print(f"scaned articles {count_articles} / {total_num_articles}")
        
            
    
    time.sleep(30)
    
if __name__ == "__main__":
    run()

# for i in range(5):
#     driver.execute_script("window.scrollBy(0, 500);")
#     car_articles = driver.find_elements(By.TAG_NAME, 'article')
#     time.sleep(2)
#     for car in car_articles:
#         set_cars.add(car)
#         # car_url = car.find_element(By.TAG_NAME, 'a')
#         # url = car_url.get_attribute("href")
#         # print(url)
#     print(len(set_cars))

# for click in set_cars:
#     click.click()
#     time.sleep(4)
#     driver.back()
#     time.sleep(2)
    # try:
    #     div_articles = driver.find_element(By.XPATH, xpath)
    #     articles = div_articles.find_elements(By.TAG_NAME, 'article')
    #     for j in range(articles):
    #         click_article = driver.find_element(By.XPATH, f'{xpath}/div[{j+1}]')
    #         click_article.click()
    #         time.sleep(3)
    #         driver.back()
    #     count += 1
    # except:
    #     driver.execute_script("window.scrollBy(0, 50);")
    #     time.sleep(0.5)
    #     count += 1
    #     f'//*[@id="root"]/div[3]/div/section[5]/div/div/div[2]/div/div[2]/div[{count}]'
    # print(i)

time.sleep(1000)

# listItemPage-0