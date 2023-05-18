import datetime
import re

import dateutil.parser

import settings.types


def set_life_dates(text_parts: list[str], scientist: settings.types.Scientist) -> None:
    date_regex = r"\d+\D+\d{4}"
    for text in text_parts:
        if text.startswith("Died"):
            scientist.death_date = dateutil.parser.parse(
                re.findall(date_regex, text)[0]
            ).date()
        if re.match(date_regex, text):
            scientist.birth_date = dateutil.parser.parse(
                re.findall(date_regex, text)[0]
            ).date()


def get_age(birth_date: datetime.date, death_date: datetime.date) -> int:
    return (death_date - birth_date) // datetime.timedelta(days=365.2425)
