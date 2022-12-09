import functools
import logging
import time
from typing import Type, Callable

from selenium.webdriver.remote.webdriver import WebDriver

from pages.generic import Page


LOGGER = logging.getLogger(__name__)


def get_page(page_model: Type[Page], driver: WebDriver, **kwargs) -> Page:
    try:
        page = page_model(driver=driver, **kwargs)
        LOGGER.info("Getting page: %s", page.url)
        page.get()
        return page
    except Exception as exc:
        raise
