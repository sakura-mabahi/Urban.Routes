import data
import helpers

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    request_taxi_button = (By.CSS_SELECTOR, "button.button:nth-child(3)")
    comfort_button = (By.CSS_SELECTOR, "div.tcard:nth-child(5)>div:nth-child(3)")
    comfort_validation_label = (By.CLASS_NAME, "r-sw-label")

    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_field = (By.ID, "phone")
    phone_number_next_button = (By.XPATH, "//*[@id=\"root\"]/div/div[1]/div[2]/div[1]/form/div[2]/button")

    phone_number_code_field = (By.ID, "code")
    phone_number_code_confirm_button = (By.XPATH, "//*[@id=\"root\"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")

    way_to_pay_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.CSS_SELECTOR, "input[placeholder='12']")
    link_button = (By.CSS_SELECTOR, ".pp-buttons>button:nth-child(1)")
    close_button = (By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[2]/div[1]/button")

    comment_field = (By.ID, "comment")

    blanket_scarves_slider = (By.XPATH, "//*[@id=\"root\"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    blanket_scarves_input = (By.CLASS_NAME, "switch-input")

    ice_cream_plus_button = (By.CLASS_NAME, "counter-plus")
    ice_cream_value_counter = (By.CLASS_NAME, "counter-value")

    take_taxi_button = (By.CLASS_NAME, "smart-button")

    order_header_title = (By.CLASS_NAME, "order-header-title")
    travel_information_button = (By.CSS_SELECTOR, "div.order-btn-group:nth-child(3)>button:nth-child(1)")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, set_from, set_to):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        self.set_from(set_from)
        self.set_to(set_to)

    def click_ask_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.request_taxi_button))
        self.driver.find_element(*self.request_taxi_button).click()

    def click_comfort_option(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.comfort_button))
        self.driver.find_element(*self.comfort_button).click()

    def get_validation_comfort(self):
        return self.driver.find_element(*self.comfort_validation_label).text
        #Se verifica que aparezca "Manta y pañuelos" ya que es una opción que aparece en la tarifa confort.

    def set_phone_number(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.phone_number_button))
        self.driver.find_element(*self.phone_number_button).click()  # Dar click a agregar número

        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)  # Colocar número telefónico

        self.driver.find_element(*self.phone_number_next_button).click()  # Dar click al boton siguiente

        phone_confirmation_code = str(helpers.retrieve_phone_code(self.driver))
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.phone_number_code_field))
        self.driver.find_element(*self.phone_number_code_field).send_keys(phone_confirmation_code)  # Agregar código de telefono

        self.driver.find_element(*self.phone_number_code_confirm_button).click()  # Dar click en el botón para confirmar código

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_phone_number_code(self):
        return self.driver.find_element(*self.phone_number_code_field).get_property('value')

    def set_payment_method(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.way_to_pay_button))
        the_card = data.card_number
        the_code = data.card_code
        self.driver.find_element(*self.way_to_pay_button).click()  # Click en el botón de agregar método de pago
        self.driver.find_element(*self.add_card_button).click()  # Click en el botón de agregar tarjeta

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.card_number_field)).click()

        self.driver.find_element(*self.card_number_field).send_keys(the_card)  # Agregar número de tarjeta

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.card_code_field)).click()

        self.driver.find_element(*self.card_code_field).send_keys(the_code)  # Agregar Codigo de la tarjeta
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)  # Dar click en Teclado TAB

        self.driver.find_element(*self.link_button).click()  # Dar click al botón enlace

        self.driver.find_element(*self.close_button).click()  # Cerrar Ventana de agregar metodo de pago

    def get_card(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_code_card(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def add_comment_to_driver(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.comment_field))
        message_for_driver = data.message_for_driver
        self.driver.find_element(*self.comment_field).send_keys(message_for_driver)  # Agregar mensaje para al conductor

    def get_comment(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    def add_blankets_and_scarves(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.blanket_scarves_slider))
        self.driver.find_element(*self.blanket_scarves_slider).click()  # Agregar manta y pañuelos

    def get_blankets_and_scarves(self):
        return self.driver.find_element(*self.blanket_scarves_input).is_selected()

    def add_two_icecream(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.ice_cream_value_counter))
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.driver.find_element(*self.ice_cream_plus_button)).perform()  # Agregar dos helados

    def get_ice_cream(self):
        return self.driver.find_element(*self.ice_cream_value_counter).text

    def take_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.take_taxi_button))
        self.driver.find_element(*self.take_taxi_button).click()

    def get_take_taxi(self):
        return self.driver.find_element(*self.take_taxi_button).text

    def wait_for_load_information(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.order_header_title))

        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.travel_information_button))

    def get_wait_driver_information(self):
        return self.driver.find_element(*self.order_header_title)

    def get_wait_travel_information(self):
        return self.driver.find_element(*self.travel_information_button)


