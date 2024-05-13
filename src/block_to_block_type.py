import re
import functools
from enums.block_type import BlockType

def block_to_block_type(block: str) -> str:
    if re.match(r"^#{1,6}.*$", block) != None:
        return BlockType.HEADING
    
    if re.match(r"^(`{3})((.*)\n*)*(`{3})$", block) != None:
        return BlockType.CODE
    
    lines = block.split("\n")

    def bool_reducer_constructor(expression):
        def bool_reducer(prev, line):
            return (prev and expression(line))
        
        return bool_reducer

    if functools.reduce(bool_reducer_constructor(lambda l: re.match(r"^>.*$", l)), lines, True):
        return BlockType.QUOTE

    if functools.reduce(bool_reducer_constructor(lambda l: re.match(r"^(-|\*) .*$", l)), lines, True):
        return BlockType.UNORDERED_LIST
 
    if functools.reduce(bool_reducer_constructor(lambda l: re.match(r"^[0-9]+. .*$", l)), lines, True):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH