from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPagina:
    TITULO_DASHBOARD = (By.XPATH, "//h6[contains(.,'Dashboard')]")

    def __init__(self, driver):
        self.driver = driver

    def dashboard_visivel(self):
        try:
            elemento = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.TITULO_DASHBOARD)
            )
            return elemento.is_displayed()
        except:
            # fallback pela URL
            return "dashboard" in self.driver.current_url.lower()
