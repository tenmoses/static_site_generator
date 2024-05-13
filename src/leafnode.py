from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value = None, props=None) -> None:
        if value == None:
            raise ValueError("All leaf nodes require a value")
        
        super().__init__(tag, value, None, props)

    def to_html(self):
        html_string = ""

        if self.tag:
            html_string += f"<{self.tag}{self.props_to_html()}>"
            html_string += self.value
            html_string += f"</{self.tag}>"
        else:
            html_string += self.value

        return html_string
