from textnode import TextNode
from enums.text_type import TextType
from typing import List
import extract_markdown

def delimiter(
        old_nodes: List[TextNode], 
        delimiter: str, 
        text_type: TextType
        ) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT_TYPE_TEXT:
            new_nodes.append(node)
            continue

        sub_nodes = node.text.split(delimiter)

        if len(sub_nodes) % 2 == 0:
            raise Exception(f"Node {node} has invalid markdown syntax. Delimiter: {delimiter}")
        
        for i in range(0, len(sub_nodes)):
            if i % 2 == 0 or i == 0:
                new_nodes.append(TextNode(sub_nodes[i], TextType.TEXT_TYPE_TEXT))
            else:
                new_nodes.append(TextNode(sub_nodes[i], text_type))

    return new_nodes

def image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown.images(node.text)
        text = node.text

        if len(images):
            for i in range(0, len(images)):
                image = images[i]
                splitted = text.split(f"![{image[0]}]({image[1]})", 1)

                if len(splitted) != 2:
                    raise Exception("Cannot split by image string!")
                
                new_nodes.append(TextNode(splitted[0], TextType.TEXT_TYPE_TEXT))
                new_nodes.append(TextNode(image[0], TextType.TEXT_TYPE_IMAGE, image[1]))
                
                text = splitted[1]

            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT_TYPE_TEXT))
        else:
            new_nodes.append(node)

    return new_nodes

def link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown.links(node.text)
        text = node.text

        if len(links):
            for i in range(0, len(links)):
                link = links[i]
                splitted = text.split(f"[{link[0]}]({link[1]})", 1)

                if len(splitted) != 2:
                    raise Exception("Cannot split by link string!")
                
                new_nodes.append(TextNode(splitted[0], TextType.TEXT_TYPE_TEXT))
                new_nodes.append(TextNode(link[0], TextType.TEXT_TYPE_LINK, link[1]))
                
                text = splitted[1]

            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT_TYPE_TEXT))
        else:
            new_nodes.append(node)

    return new_nodes