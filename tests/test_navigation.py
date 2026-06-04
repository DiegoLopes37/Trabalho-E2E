import time
import pytest
from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina


@pytest.mark.parametrize("menu_func, expected_url", [
    ("acessar_admin", "admin"),
    ("acessar_pim", "pim"),
    ("acessar_leave", "leave"),
    ("acessar_time", "time"),
])
def test_navegacao(driver, menu_func, expected_url):
    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")

    time.sleep(2)  # pausa para ver o login

    getattr(menu, menu_func)() 

    time.sleep(2)  # pausa para ver a navegação

    assert expected_url in driver.current_url.lower()
