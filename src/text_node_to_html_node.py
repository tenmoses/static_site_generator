from textnode import TextNode
from leafnode import LeafNode
from enums.text_type import TextType

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})