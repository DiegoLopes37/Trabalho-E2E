from paginas.login_pagina import LoginPagina


def test_login_sucesso(driver):

    pagina = LoginPagina(driver)

    pagina.abrir()
    pagina.realizar_login("Admin", "admin123")

    assert "dashboard" in driver.current_url.lower()