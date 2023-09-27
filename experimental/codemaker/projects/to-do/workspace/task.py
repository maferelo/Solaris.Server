from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    category: str
    status: str
