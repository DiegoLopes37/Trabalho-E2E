import pytest
from paginas.login_pagina import LoginPagina
from paginas.dashboard_pagina import DashboardPagina


def test_login_sucesso(driver):
    login = LoginPagina(driver)
    dashboard = DashboardPagina(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")

    assert dashboard.dashboard_visivel()


def test_login_invalido(driver):
    login = LoginPagina(driver)

    login.abrir()
    login.realizar_login("usuario_invalido", "senha_errada")

    assert login.mensagem_erro_visivel() == "Invalid credentials"
