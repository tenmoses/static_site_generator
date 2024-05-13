from textnode import TextNode
from enums.text_type import TextType
from typing import List
import split_nodes

def text_to_textnodes(text: str) -> List[TextNode]:
    images_extracted = split_nodes.image([TextNode(text, TextType.TEXT_TYPE_TEXT)])
    links_extracted = split_nodes.link(images_extracted)
    code_extracted = split_nodes.delimiter(links_extracted, "`", TextType.TEXT_TYPE_CODE)
    bold_extracted = split_nodes.delimiter(code_extracted, "**", TextType.TEXT_TYPE_BOLD)
    italic_extracted = split_nodes.delimiter(bold_extracted, "*", TextType.TEXT_TYPE_ITALIC)

    nodes = italic_extracted
    
    return nodes