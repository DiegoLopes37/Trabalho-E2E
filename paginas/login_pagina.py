from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPagina:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    CAMPO_USUARIO = (By.NAME, "username")
    CAMPO_SENHA = (By.NAME, "password")
    BOTAO_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAMPO_USUARIO)
        )

    def realizar_login(self, usuario, senha):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAMPO_USUARIO)
        ).send_keys(usuario)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAMPO_SENHA)
        ).send_keys(senha)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTAO_LOGIN)
        ).click()

    def mensagem_erro_visivel(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MENSAGEM_ERRO)
        ).text
