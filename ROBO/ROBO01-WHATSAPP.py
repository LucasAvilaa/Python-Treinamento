from selenium import webdriver
import time

class whatsBot:
    def __init__(self):
        print("Robo iniciado") 
        self.mensagem = input("Digite a mensagem para ser enviada: ")
        self.grupos = input("Digite para quem vai a mensagem: ")
        # Fazer o programa aceitar variaveis para esse campos self.grupos = input("Para quem deseja enviar? ")
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe') 
         
#        GRUPO -             <span dir="auto" title="Meus Documentos" class="_1wjpf
#                             _3NFp9 _3FXB1">Meus Documentos</span>
#        CAIXA DE MENSAGEM - <div tabindex="-1" class="_1Plpp">
#        BOTAO ENVIAR -      <span data-icon="send" class="">       
        
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)

        grupo = self.driver.find_element_by_xpath(f"//span[@title='{self.grupos}']") 
        time.sleep(2)
        grupo.click()

        time.sleep(2)
        chat_box = self.driver.find_element_by_class_name('_3uMse')
        chat_box.click()
        chat_box.send_keys(self.mensagem)

        botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")       
        time.sleep(2)
        botao.click()
        time.sleep(2)
        print("Robo concluido com exito")
        self.driver.quit()

bot = whatsBot()
bot.__init__()