from dataclasses import dataclass


@dataclass
class ResultDataclass:
    base_rate: int
    floater_discount: int
    discounted_rate: int
    description: str
    age: int
