from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina


def test_acessar_pim(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")

    menu.acessar_pim()

    assert "pim" in driver.current_url.lower()