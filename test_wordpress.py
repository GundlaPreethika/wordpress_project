import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestWordPress:

    @pytest.mark.title
    def test_verify_title(self, driver):
        driver.get("https://wordpress.org/")
        assert "WordPress" in driver.title
        print("Title Verified Successfully")

    @pytest.mark.themes
    def test_search_theme_and_verify_image(self, driver):

        wait = WebDriverWait(driver, 30)

        # Step 1: Open WordPress
        driver.get("https://wordpress.org/")

        # Step 2: Mouse Hover on Extend
        extend = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Extend']")
            )
        )
        ActionChains(driver).move_to_element(extend).perform()

        # Step 3: Click Themes
        themes = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Themes']")
            )
        )
        themes.click()

        # Step 4: Open real theme search page directly (stable method)
        driver.get("https://wordpress.org/themes/search/astra/")

        # Step 5: Wait for Astra title to appear
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(text(),'Astra')]")
            )
        )

        # Verify Astra title
        theme_titles = driver.find_elements(By.CSS_SELECTOR, ".theme-name")
        assert any("Astra" in title.text for title in theme_titles)

        print("Astra Theme Title Verified")

        # Step 6: Verify Astra image displayed
        astra_image = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[contains(@src,'astra')]")
            )
        )

        assert astra_image.is_displayed()

        print("Astra Theme Image Verified Successfully ✅")