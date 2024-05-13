import unittest

from textnode import TextNode
from enums.text_type import TextType
import text_to_textnodes

class TestTextToTextnode(unittest.TestCase):
    def test_on_valid_markdown(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes.text_to_textnodes(text)
        self.assertEqual(nodes, [
    TextNode("This is ", TextType.TEXT_TYPE_TEXT),
    TextNode("text", TextType.TEXT_TYPE_BOLD),
    TextNode(" with an ", TextType.TEXT_TYPE_TEXT),
    TextNode("italic", TextType.TEXT_TYPE_ITALIC),
    TextNode(" word and a ", TextType.TEXT_TYPE_TEXT),
    TextNode("code block", TextType.TEXT_TYPE_CODE),
    TextNode(" and an ", TextType.TEXT_TYPE_TEXT),
    TextNode("image", TextType.TEXT_TYPE_IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and a ", TextType.TEXT_TYPE_TEXT),
    TextNode("link", TextType.TEXT_TYPE_LINK, "https://boot.dev"),
]
)