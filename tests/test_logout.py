import time
from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina


def test_logout(driver):
    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")

    time.sleep(2)  # pausa para ver o login realizado

    menu.realizar_logout()

    time.sleep(2)  # pausa para ver o retorno à tela de login

    assert "login" in driver.current_url.lower()
