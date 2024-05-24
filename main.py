import data
import pages

from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = pages.UrbanRoutesPage(cls.driver)

# 1.Configurar la dirección

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        routes_page.set_route(address_from, address_to)
        routes_page.click_ask_taxi()
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# 2.Seleccionar la tarifa Comfort.

    def test_choose_comfort(self):
        rates_page = pages.UrbanRoutesPage(self.driver)
        rates_page.click_comfort_option()

        validation = pages.UrbanRoutesPage(self.driver).get_validation_comfort()
        assert validation == 'Manta y pañuelos'

# 3.Rellenar el número de teléfono.

    def test_set_number_phone(self):
        phone_page = pages.UrbanRoutesPage(self.driver)
        phone_page.set_phone_number()

        phone_number = data.phone_number
        assert phone_page.get_phone_number() == phone_number

# 4.Agregar una tarjeta de crédito.

    def test_add_card(self):
        card_page = pages.UrbanRoutesPage(self.driver)
        card_page.set_payment_method()

        the_card = data.card_number
        the_code = data.card_code
        assert card_page.get_card() == the_card
        assert card_page.get_code_card() == the_code

# 5.Escribir un mensaje para el controlador.

    def test_add_message_driver(self):
        comments_page = pages.UrbanRoutesPage(self.driver)
        comments_page.add_comment_to_driver()

        message_for_driver = data.message_for_driver
        assert comments_page.get_comment() == message_for_driver

# 6.Pedir una manta y pañuelos.

    def test_add_details(self):
        details_page = pages.UrbanRoutesPage(self.driver)
        details_page.add_blankets_and_scarves()

        assert details_page.get_blankets_and_scarves()

# 7.Pedir 2 helados.

    def test_add_ice(self):
        ice_page = pages.UrbanRoutesPage(self.driver)
        ice_page.add_two_icecream()

        element_count = pages.UrbanRoutesPage(self.driver).get_ice_cream()
        assert element_count == "2"

# 8.Aparece el modal para buscar un taxi.

    def test_take_taxi(self):
        taxi_page = pages.UrbanRoutesPage(self.driver)
        taxi_page.take_taxi()

        element_text = pages.UrbanRoutesPage(self.driver).get_take_taxi()
        assert element_text == "Pedir un taxi\nEl recorrido será de 1 kilómetros y se hará en 2 min"

# 9.Esperar a que aparezca la información del conductor en el modal.

    def test_wait_for_info(self):
        info_page = pages.UrbanRoutesPage(self.driver)
        info_page.wait_for_load_information()

        driver_information = pages.UrbanRoutesPage(self.driver).get_wait_driver_information()
        assert driver_information.is_displayed()

        travel_information = pages.UrbanRoutesPage(self.driver).get_wait_travel_information()
        assert travel_information.is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
