# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
import os
import locale


class Automation:
    def __init__(self):
        # Declarar variáveis
        load_dotenv(find_dotenv())
        self.url = os.getenv("URL")
        self.pesquisas = os.getenv("PESQUISAS").split(";")

        # Nomes de HTML
        self.campo_pesquisar = "input[name='q']"
        self.tecla_enter = "Enter"
        self.campo_span = "//*[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span[1]"
        self.atributo_span = "data-value"

        # Iniciar Navegador
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        self.page = browser.new_page()
    
    def abrir_navegador(self):
        # Entrar no google
        self.page.goto(self.url)
        self.page.wait_for_selector(self.campo_pesquisar)

    def fechar_navegador(self):
        # Fechar Navegador
        self.page.close()

    def consultar_valor(self, pesquisa):
        # Realizar consultas
        nome = pesquisa.replace("hoje", "").strip()
        self.page.fill(self.campo_pesquisar, pesquisa)
        self.page.keyboard.press(self.tecla_enter)

        while True:
            try:
                span = self.page.locator(self.campo_span)
                if span:
                    break
            except:
                pass

        # Pegar e formatar o valor
        data_value = float(span.get_attribute(self.atributo_span))
        valor = locale.format_string("%.3f", data_value)
        print(f"{nome}: {valor}")
    
    def iniciar_consultas(self):
        # Iniciar processo
        print("\nValores (R$):\n")

        for pesquisa in self.pesquisas:
            self.abrir_navegador()
            self.consultar_valor(pesquisa)

        self.fechar_navegador()
