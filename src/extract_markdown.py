import re
from typing import List

def images(text: str) -> List[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def links(text: str) -> List[tuple]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)