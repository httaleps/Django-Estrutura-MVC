# core/rpa/coletor.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def executar_automacao(url):

    # função q abre um site e coleta o titulo da pagina
    # pde ser expandida para coletar outros dados, clicar em botões, preencher formulários, etc.

    # configurações do Chrome para execução headless (modo headless = sem abrir janela)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar em modo headless (sem
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Aguarde o carregamento da página

        titulo = driver.find_element(By.TAG_NAME, "title").text
        primeiro_h1 = driver.find_element(By.TAG_NAME, "h1").text

        return {
            "sucesso": True,
            "titulo": titulo,
            "h1": primeiro_h1,
            "url": url,
            "mensagem": "Automação executada com sucesso."
        }
    
    except Exception as e:
        return {
            "sucesso": False,
            "erro": str(e),
            "mensagem": "Ocorreu um erro durante a execução da automação."
        }
    
    finally:
        driver.quit()