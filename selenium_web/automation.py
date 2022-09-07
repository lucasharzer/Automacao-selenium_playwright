# pip3 install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv, find_dotenv
import os
import locale


class Automation:
    def __init__(self):
        # Variáveis
        load_dotenv(find_dotenv())
        self.url = os.getenv("URL")
        self.pesquisas = os.getenv("PESQUISAS").split(";")

        # Nomes de HTML
        self.campo_pesquisar = "q"
        self.campo_div = "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]"
        self.campo_span = "span[1]"
        self.atributo_span = "data-value"

        # Declarar Navegador
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def abrir_navegador(self):
        # Entrar no google
        self.driver.get(self.url)

        while True:
            try:
                self.pesquisar = self.driver.find_element(By.NAME, self.campo_pesquisar)
                if self.pesquisar:
                    break
            except:
                pass
        
        self.driver.maximize_window()
    
    def fechar_navegador(self):
        # Fechar o Navegador
        self.driver.close()

    def consultar_valor(self, pesquisa):
        # Realizar consultas
        nome = pesquisa.replace("hoje", "").strip()
        self.pesquisar.send_keys(pesquisa + Keys.ENTER)

        while True:
            try:
                div = self.driver.find_element(By.XPATH, self.campo_div)
                if div:
                    break
            except:
                pass
        
        # Pegar e formatar o valor
        span = div.find_element(By.XPATH, self.campo_span)
        data_value = float(span.get_attribute(self.atributo_span))
        valor = locale.format_string("%.3f", data_value)
        print(f"{nome}: {valor}")
    
    def iniciar_consultas(self):
        # Iniciar o processo
        print("\nValores (R$):\n")
        
        for pesquisa in self.pesquisas:
            self.abrir_navegador()
            self.consultar_valor(pesquisa)

        # Finalizar processo
        self.fechar_navegador()
