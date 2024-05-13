class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""

        if self.props:
            for prop in self.props:
                prop_string += f" {prop}=\"{self.props[prop]}\""

        return prop_string
    
    def __repr__(self) -> str:
        string = f"Tags: {self.tag}\n"
        string += f"Value: {self.value}\n"
        string += f"Children:"

        if self.children:
            string += "\n"
            for child in self.children:
                string += f" - {child.tag}\n"

        else:
            string += "None\n"

        string += f"Props: "

        if self.props:
            string += "\n"
            for prop in self.props:
                string += f" - {prop}: {self.props.prop}"

        else:
            string += "None\n"

        return string