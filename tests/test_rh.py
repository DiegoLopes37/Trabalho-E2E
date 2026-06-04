import time
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

    time.sleep(2)  # pausa para ver a tela do PIM

    rh.pesquisar_funcionario("Linda Anderson")

    time.sleep(3)  # pausa para ver o resultado da busca

    assert rh.resultado_visivel("Linda Anderson")
