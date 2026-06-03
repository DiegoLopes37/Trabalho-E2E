from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPagina:
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_LEAVE = (By.XPATH, "//span[text()='Leave']")
    MENU_TIME = (By.XPATH, "//span[text()='Time']")
    MENU_USER = (By.CLASS_NAME, "oxd-userdropdown-tab")
    BOTAO_LOGOUT = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def acessar_admin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_ADMIN)
        ).click()

    def acessar_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_PIM)
        ).click()

    def acessar_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_LEAVE)
        ).click()

    def acessar_time(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_TIME)
        ).click()

    def realizar_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_USER)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTAO_LOGOUT)
        ).click()
