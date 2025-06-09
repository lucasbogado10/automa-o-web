from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# definir navegador
navegador = webdriver.Chrome()

time.sleep(10) # Reduzido para agilizar

navegador.get("https://www.google.com/?hl=pt-BR")

time.sleep(10) # Reduzido para agilizar

navegador.maximize_window()

time.sleep(10) # Pequena pausa após maximizar

# 1. Definir o texto fixo a ser pesquisado
texto_a_digitar = "YouTube"

# 2. Localizar a barra de pesquisa do Google
# Esta linha pode causar um erro se o elemento não for encontrado
barra_pesquisa = navegador.find_element(By.NAME, "q")

# 3. Digitar o texto fixo na barra de pesquisa
barra_pesquisa.send_keys(texto_a_digitar)

# 4. Pressionar Enter para realizar a pesquisa
barra_pesquisa.submit()

time.sleep(10) # Dê tempo para os resultados da pesquisa carregarem

# 5. Localizar o link do YouTube nos resultados da pesquisa
# Esta linha pode causar um erro se o elemento não for encontrado
link_youtube = navegador.find_element(By.PARTIAL_LINK_TEXT, "YouTube")

# 6. Clicar no link
link_youtube.click()


time.sleep(10) # Tempo para ver a página do YouTube antes de fechar

navegador.quit() # Fecha o navegador ao final do script
