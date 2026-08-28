from selenium import webdriver

def goto(link):
    driver = webdriver.Chrome()
    print('driver init ok, going to link')
    driver.get(link)
    return driver

def scrape(driver):
    pass
   
def main():
    driver = goto("https://baomoi.com/")

main()