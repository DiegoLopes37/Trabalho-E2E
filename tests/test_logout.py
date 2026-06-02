from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina


def test_logout(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()

    login.realizar_login(
        "Admin",
        "admin123"
    )

    menu.realizar_logout()

    assert "login" in driver.current_url.lower()