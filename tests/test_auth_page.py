import pytest
from pages.auth_page import AuthPage

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('bulychev73@gmail.com')

    page.password.send_keys("Kott22011980")

    page.btn.click()

    assert page.get_current_url() == 'http://petfriends.skillfactory.ru/all_pets'

