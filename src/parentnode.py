from htmlnode import HTMLNode
from textnode import TextNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        if tag == None:
            raise ValueError("The tag is not provided")
        
        super().__init__(tag, value, children, props)

    def to_html(self):
        if  self.children == None:
            raise ValueError("ParentNode should have at least one children node")
        
        html_string = ""

        html_string += f"<{self.tag}{self.props_to_html()}>"
        
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"

        return html_string
    
    def add_child(self, child: HTMLNode):
        if self.children == None:
            self.children = []

        self.children.append(child)