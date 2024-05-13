from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from enums.block_type import BlockType
import re

def markdown_to_html(markdown):
    html = ParentNode("div")

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_transformers[block_type](block)

        html.add_child(block_node)

    return html.to_html()


def transform_heading(block: str):
    num = block.count("#")
    text = block.lstrip("# ")

    child_nodes = text_to_textnodes(text)

    if len(child_nodes) > 1:
        return ParentNode(f"h{num}", None, map(text_node_to_html_node, child_nodes))
    
    return LeafNode(f"h{num}", text)

def transform_code(block: str):
    codeNode = LeafNode("code", block.strip("`\n"))
    return ParentNode("pre", None, [codeNode])

def transform_quote(block: str):
    child_nodes = text_to_textnodes(block.lstrip("> ").replace("\n> ", "\n"))

    if len(child_nodes) > 1:
        return ParentNode("blockquote", None, map(text_node_to_html_node, child_nodes))
    
    return LeafNode("blockquote", block.lstrip("> ").replace("\n> ", "\n"))

def transform_unordered_list(block: str):
    lis = []

    for li in block.split("\n"):
        clear_text = re.sub(r"(-|\*) ", "", li)
        # clear_text = li.lstrip("-* ")
        child_nodes = text_to_textnodes(clear_text)

        if len(child_nodes) > 1:
            lis.append(ParentNode("li", None, map(text_node_to_html_node, child_nodes)))
        else:
            lis.append(LeafNode("li", clear_text))  

    return ParentNode("ul", None, list(lis))

def transform_ordered_list(block: str):
    lis = []

    for li in block.split("\n"):
        clear_text = li.lstrip("1234567890. ")
        child_nodes = text_to_textnodes(clear_text)

        if len(child_nodes) > 1:
            lis.append(ParentNode("li", None, map(text_node_to_html_node, child_nodes)))
        else:
            lis.append(LeafNode("li", clear_text))  

    return ParentNode("ol", None, list(lis))

def transform_paragraph(block: str):
    child_nodes = text_to_textnodes(block)

    if len(child_nodes) > 1:
        return ParentNode("p", None, map(text_node_to_html_node, child_nodes))
    
    return LeafNode("p", block)

block_transformers = {
    BlockType.HEADING: transform_heading,
    BlockType.CODE: transform_code,
    BlockType.QUOTE: transform_quote,
    BlockType.UNORDERED_LIST: transform_unordered_list,
    BlockType.ORDERED_LIST: transform_ordered_list,
    BlockType.PARAGRAPH: transform_paragraph
}