import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_have_no_props(self):
        node = HTMLNode()
        string = ""
        self.assertEqual(node.props_to_html(), string)

    def test_props(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), string)


if __name__ == "__main__":
    unittest.main()