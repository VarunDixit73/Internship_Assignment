from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd


def get_add(query='mobiles',start=1):
    url = 'https://www.flipkart.com/search'
    param1 = f'q={query}'
    param2 = f'page={start}'
    return f'{url}?{param1}&{param2}'

def extract_data(driver):
    data =[]
    cards =driver.find_elements_by_css_selector('div._2kHMtA')
    if len(cards)>0:
        for item in cards:
            data.append(dict(
                Brand = item.find_element_by_css_selector('div._4rR01T').text,
                Specs = item.find_element_by_css_selector('div.fMghEO').text,
                Price = item.find_element_by_css_selector('div._30jeq3._1_WHN1').text,
            ))
    return data

def get_flipkart_data(search = 'mobiles', pos=1, limit=None):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    all_data= [] 
    while True:
        addr = get_add(search, pos)
        driver.get(addr)
        data = extract_data(driver)
        if len(data):
            all_data.extend(data)
            if limit and limit== pos:
                break
            pos+=1
        else:
            driver.close()
            break
    return all_data

content = get_flipkart_data(limit=14)

pd.DataFrame(content).to_csv('flipkart_mobiles.csv')