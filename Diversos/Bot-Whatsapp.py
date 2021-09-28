import sys, string, os, subprocess, time
from selenium import webdriver

class whatsBot:
    def __init__(self):
        print("Robo iniciado") 
        self.mensagem = "Teste"#input("Digite a mensagem para ser enviada: ")
        self.grupos = "Meus Documentos" #input("Digite para quem vai a mensagem: ")    
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.driver = webdriver.Chrome(r"C:\\Program Files (x86)\\Google\\Chrome\Application/chrome.exe","web.whatsapp.com")       
        print("ae")
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(2)

        grupo = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']") 
        time.sleep(2)
        grupo.click()

        time.sleep(2)
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        chat_box.click()
        chat_box.send_keys(self.mensagem)

        botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")       
        time.sleep(2)
        botao.click()
        time.sleep(2)
        print("Robo concluido com exito")

bot = whatsBot()