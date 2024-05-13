class TextNode:
    def __init__(self, text, text_type, url = ""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return f"{self.text}{self.text_type}{self.url}" == f"{text_node.text}{text_node.text_type}{text_node.url}"
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
