from typing import List

def markdown_to_blocks(text: str) -> List[str]:
    return text.split("\n\n")