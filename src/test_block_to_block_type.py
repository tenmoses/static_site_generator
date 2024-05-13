import unittest
from block_to_block_type import block_to_block_type
from enums.block_type import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        text = "###### Heading level 6"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        text = "```Try to put a blank line before...\n\n---\n\n...and after a horizontal rule.\n        ```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        text = "> Dorothy followed her through many of the beautiful rooms in her castle.\n>\n> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_invalid_quote(self):
        text = "> Dorothy followed her through many of the beautiful rooms in her castle.\n\n> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        text = "- First item\n* Second item\n- Third item\n- Fourth item "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        text = "- First item\n* Second item\n Third item\n- Fourth item "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        text = "1. First item\n1. Second item\n1. Third item\n1. Fourth item "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_invalid_ordered_list(self):
        text = "1. First item\n1. Second item\n- Third item\n1. Fourth item "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        text = "Heading level 6"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)        