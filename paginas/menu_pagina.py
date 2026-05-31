from selenium.webdriver.common.by import By


class MenuPagina:

    MENU_ADMIN = (By.LINK_TEXT, "Admin")
    MENU_PIM = (By.LINK_TEXT, "PIM")
    MENU_LEAVE = (By.LINK_TEXT, "Leave")
    MENU_TIME = (By.LINK_TEXT, "Time")

    def __init__(self, driver):
        self.driver = driver

    def acessar_admin(self):
        self.driver.find_element(*self.MENU_ADMIN).click()

    def acessar_pim(self):
        self.driver.find_element(*self.MENU_PIM).click()

    def acessar_leave(self):
        self.driver.find_element(*self.MENU_LEAVE).click()

    def acessar_time(self):
        self.driver.find_element(*self.MENU_TIME).click()
