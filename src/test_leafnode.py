import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_without_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), string)

    def test_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        string = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), string)        


if __name__ == "__main__":
    unittest.main()