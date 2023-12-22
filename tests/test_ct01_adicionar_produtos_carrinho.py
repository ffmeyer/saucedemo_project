import pytest

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
class TestLogin:

    def test_ct_01_login_valido(self):
        username = 'standard_user'
        password = 'secret_sauce'
        produto1 = 'Sauce Labs Backpack'
        produto2 = 'Sauce Labs Bolt T-Shirt'

        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        login_page.fazer_login(username, password)
        home_page.adcionar_ao_carrinho(produto1)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        carrinho_page.clicar_continuar_comprando()
        home_page.adcionar_ao_carrinho(produto2)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        carrinho_page.verificar_produto_carrinho_existe(produto2)
