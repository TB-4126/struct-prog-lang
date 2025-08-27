import re

patterns = [
    [r"print","print"],                       #Keyword print
    [r"\d*\.\d+|\d+\.\d*|\d+","number"],      #Number
    [r"[a-zA-Z_][a-zA-Z0-9_]*","identifier"], #Identifier
    [r"\+","+"],                              #Plus sign
    [r"\-","-"],                              #Minus sign
    [r"\*","*"],                              #Multiplication sign
    [r"\/","/"],                              #Division sign
    [r"\(","("],
    [r"\)",")"],
    [r"\s+","whitespace"],                    #Defines whitespace
    [r".","error"]                            #Unexpected error
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while (position < len(characters)):
        for pattern,tag in patterns: #Find first matching token
          match = pattern.match(characters,position)
          if (match):
            break
        
        assert(match)
    
        if (tag == "error"):
          raise Exception(f"Syntax error: illegal character :{[match.group(0)]}")
        
        token = {"tag":tag,"position":position}
        value = match.group(0)
        if (token["tag"] == "number"):
          if ("." in value):
            token["value"] = float(value)
          else:
            token["value"] = int(value)
        if (token["tag"] == "identifier"):
            token["value"] = value
        if (token["tag"] != "whitespace"):
            tokens.append(token)
        position = match.end()
    
    tokens.append({"tag":None,"position":position})
    return tokens

def test_simple_tokens():
    print("Test simple tokens...")
    for c in "+-*/()":
        assert tokenize(c) == [
            {"tag":c, "position":0},
            {"tag":None, "position":1}
        ]
    assert tokenize("3") == [
        {"tag":"number", "position":0, "value":3},
        {"tag":None, "position":1}
    ]
    assert tokenize("cat") == [
        {"tag":"identifier", "position":0, "value":"cat"},
        {"tag":None, "position":3}
    ]

def test_whitespace():
    print("Test whitespace")
    tokens = tokenize("2 + 3")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 2}, {'tag': '+', 'position': 2}, {'tag': 'number', 'position': 4, 'value': 3}, {'tag': None, 'position': 5}]

def test_simple_expressions():
    print("Test simple expressions...")
    t = tokenize("2+3")
    assert t == [{'tag': 'number', 'position': 0, 'value': 2}, {'tag': '+', 'position': 1}, {'tag': 'number', 'position': 2, 'value': 3}, {'tag': None, 'position': 3}]

if (__name__ == "__main__"):
    print("Testing Tokenizer...")
    test_simple_tokens()
    test_whitespace()
    test_simple_expressions()
    print("Done.")
