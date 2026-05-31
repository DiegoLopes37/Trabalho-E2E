from selenium.webdriver.common.by import By


class PaginaRH:

    CAMPO_NOME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    BOTAO_PESQUISAR = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def pesquisar_funcionario(self, nome):
        self.driver.find_element(*self.CAMPO_NOME).send_keys(nome)
        self.driver.find_element(*self.BOTAO_PESQUISAR).click()
