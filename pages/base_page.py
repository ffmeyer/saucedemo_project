import time

from tests import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        inicio = time.time()
        print(f'estou procurando o elemento com locator =  {locator}')
        self.esperar_um_elemento_aparecer(locator)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"O método levou {tempo_execucao:.2f} segundos para ser executado")
        return self.driver.find_elements(*locator)

    def escrever(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f'O elemento "{locator}" nao foi encontrado na tela.'

    def pegar_texto_elemento(self, locator):
        self.esperar_um_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_um_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def verificar_elemento_nao_existe(self, locator):
        assert self.encontrar_elemento(locator), f'O elemento "{locator}" nao existe mas e esperado que exista.'

    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator) == 0, f'O elemento "{locator}" existe mas e esperado que nao exista.')

    def clique_duplo(self, locator):
        element = self.esperar_um_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_duplo(self, locator):
        element = self.esperar_um_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator, key):
        element = self.esperar_um_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()
        if key == 'ENTER':
            element.send_keys(Keys.ENTER)
        elif key == 'ESPACO':
            element.send_keys(Keys.SPACE)