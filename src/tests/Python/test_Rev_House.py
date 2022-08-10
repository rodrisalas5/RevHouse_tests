import time

import pytest

from src.pages.Python.RevHouse import RevHousePage


def test_load_page(browser):
    home_page = RevHousePage(browser)
    assert home_page.is_display()


def test_click_button_image(browser):
    home_page = RevHousePage(browser)
    home_page.button_main_image()
    assert home_page.id_culture()


def test_our_mission(browser):
    home_page = RevHousePage(browser)
    home_page.click_mission()
    assert home_page.is_display()


def test_services(browser):
    home_page = RevHousePage(browser)
    home_page.click_services()
    assert home_page.is_display()


def test_contact(browser):
    home_page = RevHousePage(browser)
    home_page.click_contact()
    assert home_page.is_display()


def test_select_service(browser):
    home_page = RevHousePage(browser)
    home_page.select_service()
    assert home_page.is_display()


def test_image_nav(browser):
    home_page = RevHousePage(browser)
    home_page.click_image_nav()
    assert home_page.is_display()


def test_form(browser):
    home_page = RevHousePage(browser)
    home_page.complete_form()
    assert home_page.message_ok()


def test_form_name_with_numbers(browser):
    home_page = RevHousePage(browser)
    home_page.complete_form_name_with_numbers()
    assert home_page.message_ok()


def test_form_email_without_at(browser):
    home_page = RevHousePage(browser)
    home_page.complete_form_email_without_at()
    assert home_page.message_ok()
