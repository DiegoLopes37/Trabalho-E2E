from paginas.login_pagina import LoginPagina
from paginas.menu_pagina import MenuPagina


def test_navegacao_admin(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login(
        "Admin",
        "admin123"
    )

    menu.acessar_admin()

    assert "admin" in driver.current_url.lower()


def test_navegacao_pim(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login(
        "Admin",
        "admin123"
    )

    menu.acessar_pim()

    assert "pim" in driver.current_url.lower()


def test_navegacao_leave(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login(
        "Admin",
        "admin123"
    )

    menu.acessar_leave()

    assert "leave" in driver.current_url.lower()


def test_navegacao_time(driver):

    login = LoginPagina(driver)
    menu = MenuPagina(driver)

    login.abrir()
    login.realizar_login(
        "Admin",
        "admin123"
    )

    menu.acessar_time()

    assert "time" in driver.current_url.lower()