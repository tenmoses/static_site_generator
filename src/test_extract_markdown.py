import unittest

import extract_markdown

class TestExtractMarkdown(unittest.TestCase):
    def test_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        data = extract_markdown.images(text)
        self.assertEqual(data, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
)
    
    def test_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        data = extract_markdown.links(text)
        self.assertEqual(data, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

if __name__ == "__main__":
    unittest.main()