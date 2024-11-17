from dataclasses import dataclass
from datetime import time

@dataclass(order=True)
class Patient:
    visit_time: time
    name: str
    surname: str
    age: int
    disease: str
