import time

from RPA.Browser.Selenium import Selenium

import settings.types
import utils


class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.browser = Selenium()
        self.browser.auto_close = False

    def say_hello(self) -> None:
        print("Hello, my name is " + self.name)

    @staticmethod
    def intro() -> None:
        print(
            "I will open Google Chrome to get information about scientists from Wikipedia."
        )
        print("I will type the name of a scientist to the Chrome.")
        print(
            "After that, I will open Wikipedia and collect data about each scientist."
        )

    @staticmethod
    def say_goodbye() -> None:
        print("Goodbye, take care")

    def open_webpage(self, webpage: str) -> None:
        self.browser.open_available_browser(webpage)
        self.browser.maximize_browser_window()
        # Refuse cookies
        self.browser.click_button_when_visible(locator="W0wltc")

    def input_text(self, text: str) -> None:
        self.browser.click_element(locator="APjFqb")
        self.browser.input_text(locator="APjFqb", text=text)

    def submit_form(self) -> None:
        self.browser.submit_form()

    def go_to_wikipedia(self, name: str):
        # I used the link, because different countries can have Wikipedia on different languages.
        link = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
        if self.browser.does_page_contain_link(link):
            self.browser.click_link(link)
        else:
            print("Something went wrong")

    def scrape_data(self, scientist_name: str) -> settings.types.Scientist:
        scientist = settings.types.Scientist(name=scientist_name)
        # Download a table from Wikipedia
        wiki_table = str(self.browser.get_text("css:div#mw-content-text table"))
        table_parts = wiki_table.split("Born")[1][:200].strip().split("\n")
        # Parse dates from the text
        utils.set_life_dates(text_parts=table_parts, scientist=scientist)
        scientist.age = utils.get_age(scientist.birth_date, scientist.death_date)

        scientist_info = self.browser.get_text(
            "xpath://div[@id='mw-content-text']/div[1]/p[2]"
        )
        if scientist_info == "":
            scientist_info = self.browser.get_text(
                "xpath://div[@id='mw-content-text']/div[1]/p[3]"
            )
        scientist.info = scientist_info
        return scientist

    def retrieve_scientist_info(self, scientist_name: str) -> None:
        self.input_text(text=scientist_name)
        self.submit_form()
        # Add sleep to make it a bit slower for realistic human behavior
        time.sleep(2)
        self.go_to_wikipedia(scientist_name)
        scientist_data = self.scrape_data(scientist_name)
        scientist_data.get_info()
        self.browser.go_back()
