from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina
from paginas.pagina_rh import PaginaRH


def test_pesquisar_funcionario(driver):
    login = LoginPagina(driver)
    menu = MenuPagina(driver)
    rh = PaginaRH(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")
    menu.acessar_pim()

    rh.pesquisar_funcionario("Linda Anderson")

    assert rh.resultado_visivel("Linda Anderson")
