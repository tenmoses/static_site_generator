import unittest
from markdown_to_html import markdown_to_html

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_empty(self):
        markdown = ""
        html = markdown_to_html(markdown)

        self.assertEqual(html, "<div><p></p></div>")

    def test_simple(self):
        markdown = "# Sample Markdown\n\nThis is some basic, sample markdown.\n\n## Second Heading\n\n* Unordered lists, and:\n* More\n\n> Blockquote\n\nAnd code highlighting:\n\n```\nvar foo = 'bar';\n```"
        html = markdown_to_html(markdown)

        valid = "<div><h1>Sample Markdown</h1><p>This is some basic, sample markdown.</p><h2>Second Heading</h2><ul><li>Unordered lists, and:</li><li>More</li></ul><blockquote>Blockquote</blockquote><p>And code highlighting:</p><pre><code>var foo = 'bar';</code></pre></div>"

        self.assertEqual(html, valid)

    def test_with_inline(self):
        markdown = "# Sample Markdown\n\nThis is some basic, sample markdown.\n\n## Second Heading\n\n* Unordered **lists**, and:\n* More\n\n1. One\n1. Two\n1. Three\n\n> Lists are made by using *indentation* and a beginning-of-line marker to indicate a list item. For example, unordered lists are made like this\n\nAnd **bold**, *italics*. [A link](https://markdowntohtml.com) to somewhere.\n\nOr inline code like `var foo = 'bar';`.\n\nOr an image of bears\n\n![bears](http://placebear.com/200/200)\n\nThe end ..."
        html = markdown_to_html(markdown)

        valid = "<div><h1>Sample Markdown</h1><p>This is some basic, sample markdown.</p><h2>Second Heading</h2><ul><li>Unordered <b>lists</b>, and:</li><li>More</li></ul><ol><li>One</li><li>Two</li><li>Three</li></ol><blockquote>Lists are made by using <i>indentation</i> and a beginning-of-line marker to indicate a list item. For example, unordered lists are made like this</blockquote><p>And <b>bold</b>, <i>italics</i>. <a href=\"https://markdowntohtml.com\">A link</a> to somewhere.</p><p>Or inline code like <code>var foo = 'bar';</code>.</p><p>Or an image of bears</p><p><img src=\"http://placebear.com/200/200\" alt=\"bears\"></img></p><p>The end ...</p></div>"

        self.assertEqual(html, valid)