from selenium import webdriver
import time

class googleBot:

    
    def __init__(self):
        print("Robo iniciado")
        self.login = "gmail@gmail.com"
        self.senha = "Senha18331"      
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Logar(self):     
        
        self.driver.get("https://www.google.com")
        time.sleep(2)

        botao = self.driver.find_element_by_xpath("//div[@class='gb_qg gb_i']")
        time.sleep(1)
        botao.click()

        log = self.driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        log.send_keys(self.login)
        time.sleep(1)

        enviar = self.driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
        enviar.click()
        time.sleep(2)

        senha = self.driver.find_element_by_xpath("//input[@type='password']")
        senha.click()
        senha.send_keys(self.senha)
        time.sleep(2)

        proximo = self.driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
        proximo.click()
        time.sleep(10)
        


bot = googleBot()
bot.Logar()