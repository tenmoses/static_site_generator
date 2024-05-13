import unittest

from textnode import TextNode
import split_nodes
from enums.text_type import TextType

class TestSplitNodes(unittest.TestCase):
    def test_delimiter_on_valid_markdown(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT_TYPE_TEXT)
        new_nodes = split_nodes.delimiter([node, node], "`", TextType.TEXT_TYPE_CODE)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT_TYPE_TEXT),
    TextNode("code block", TextType.TEXT_TYPE_CODE),
    TextNode(" word", TextType.TEXT_TYPE_TEXT),
    TextNode("This is text with a ", TextType.TEXT_TYPE_TEXT),
    TextNode("code block", TextType.TEXT_TYPE_CODE),
    TextNode(" word", TextType.TEXT_TYPE_TEXT),
]
)

    def test_delimiter_on_invalid_markdown(self):
        node = TextNode("This is text with a ``code block` word", TextType.TEXT_TYPE_TEXT)
        with self.assertRaises(Exception):
            split_nodes.delimiter([node], "`", TextType.TEXT_TYPE_CODE)

    def test_image_on_valid_markdown(self):
        node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and text",
    TextType.TEXT_TYPE_TEXT,
)
        new_nodes = split_nodes.image([node])
        self.assertEqual(new_nodes, [
    TextNode("This is text with an ", TextType.TEXT_TYPE_TEXT),
    TextNode("image", TextType.TEXT_TYPE_IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", TextType.TEXT_TYPE_TEXT),
    TextNode(
        "second image", TextType.TEXT_TYPE_IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
    TextNode(" and text", TextType.TEXT_TYPE_TEXT)       
        ])

    def test_link_on_valid_markdown(self):
        node = TextNode(
    "This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and text",
    TextType.TEXT_TYPE_TEXT,
)
        new_nodes = split_nodes.link([node])
        self.assertEqual(new_nodes, [
    TextNode("This is text with an ", TextType.TEXT_TYPE_TEXT),
    TextNode("image", TextType.TEXT_TYPE_LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", TextType.TEXT_TYPE_TEXT),
    TextNode(
        "second image", TextType.TEXT_TYPE_LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
    TextNode(" and text", TextType.TEXT_TYPE_TEXT)       
        ])        


if __name__ == "__main__":
    unittest.main()