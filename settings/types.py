from typing import Optional
import dataclasses
import datetime


@dataclasses.dataclass
class Scientist:
    name: str
    birth_date: Optional[datetime.date] = None
    death_date: Optional[datetime.date] = None
    age: Optional[int] = None
    info: Optional[str] = None

    def get_info(self):
        print(f"Information about a scientist: {self.name}")
        print(f"Born: {self.birth_date}")
        print(f"Died: {self.death_date} (aged {self.age})")
        print(f"Summary: {self.info}\n")
