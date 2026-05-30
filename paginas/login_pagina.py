from selenium.webdriver.common.by import By


class LoginPagina:

    URL = "https://opensource-demo.orangehrmlive.com"

    CAMPO_USUARIO = (By.NAME, "username")
    CAMPO_SENHA = (By.NAME, "password")
    BOTAO_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def realizar_login(self, usuario, senha):
        self.driver.find_element(*self.CAMPO_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(*self.BOTAO_LOGIN).click()