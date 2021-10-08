from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver="your seleninum webdeiver path"
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver =webdriver.Chrome(executable_path=chrome_driver,options=options)
        self.current_speed ={}  
         
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(20)
        go_button=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(50)
        self.current_speed={"down_speed":float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text) ,
        "up_speed" :float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text) }
        print(self.current_speed)
        
        while True:
            if self.current_speed['down_speed'] and self.current_speed['up_speed']:
                return self.current_speed
            time.sleep(5)   
        

    def tweet_at_provider(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        email=self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email.send_keys("your email id")
        next_button=self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        next_button.click()

        time.sleep(2)
        password=self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        password.send_keys('your password')
        time.sleep(2)
        login_button=self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        login_button.click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
        time.sleep(2)

        tweet_text=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys(f"Hello @JioCare, This is the download speed {self.current_speed['down_speed']}Mbps and upload speed {self.current_speed['up_speed']}Mbps i get which is not equal to as promise.")
        tweet_button =self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()