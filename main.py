from selenium import webdriver

def accountWarmer():

    # Some of these you dont need to for logging in such as window size, etc. The ones you need are the last two
    
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1280,800")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")   


    driver = webdriver.Chrome(options=options)

    driver.get("https://www.nike.com/ca/login?continueUrl=https://www.nike.com/ca/member/profile") # Or you can go to make page and click sign in.
