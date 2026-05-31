from selenium.webdriver.common.by import By


class DashboardPagina:

    TITULO_DASHBOARD = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def __init__(self, driver):
        self.driver = driver

    def dashboard_visivel(self):
        return self.driver.find_element(
            *self.TITULO_DASHBOARD
        ).is_displayed()
