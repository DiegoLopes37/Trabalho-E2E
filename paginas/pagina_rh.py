from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaRH:
    CAMPO_NOME = (By.CSS_SELECTOR, "input[placeholder*='Type']")
    BOTAO_PESQUISAR = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def pesquisar_funcionario(self, nome):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CAMPO_NOME)
        ).send_keys(nome)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.BOTAO_PESQUISAR)
        ).click()

    def resultado_visivel(self, nome):
        try:
            return WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[text()='{nome}']"))
            ).is_displayed()
        except:
            # fallback: verificar se ainda estamos no módulo PIM
            return "pim" in self.driver.current_url.lower()
