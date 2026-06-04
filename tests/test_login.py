import time
from paginas.login_pagina import LoginPagina
from paginas.dashboard_pagina import DashboardPagina


def test_login_sucesso(driver):
    login = LoginPagina(driver)
    dashboard = DashboardPagina(driver)

    login.abrir()
    login.realizar_login("Admin", "admin123")

    time.sleep(3)  # pausa para visualizar o dashboard

    assert dashboard.dashboard_visivel()


def test_login_invalido(driver):
    login = LoginPagina(driver)

    login.abrir()
    login.realizar_login("usuario_invalido", "senha_errada")

    time.sleep(2)  # pausa para ver a mensagem de erro

    assert login.mensagem_erro_visivel() == "Invalid credentials"
