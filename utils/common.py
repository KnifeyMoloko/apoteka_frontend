import logging
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver

from pages.generic import Page


def get_page(page_model: Type[Page], driver: WebDriver) -> Page:
    try:
        page = page_model(driver=driver)
        logging.info("Getting page: %s", page.url)
        page.get()
        return page
    except Exception as exc:
        raise
