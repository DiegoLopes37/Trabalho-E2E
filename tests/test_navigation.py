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

    getattr(menu, menu_func)()  # chama dinamicamente o método
    assert expected_url in driver.current_url.lower()
