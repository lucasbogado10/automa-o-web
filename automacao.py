from selenium import webdriver
import time

#definir navegador
navegador = webdriver.Chrome() #definindo variavel para o navegador

time.sleep(10) #aguarda 10 segundos para acessar o link do google

navegador.get("https://www.google.com/?hl=pt-BR") #definindo qual link o navegador irá seguir

time.sleep(10) #define o tempo em que o navegador continuará aberto após abrir o link

navegador.maximize_window() #coloca o navegador em tela cheia

time.sleep(10)

