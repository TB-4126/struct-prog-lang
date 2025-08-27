from tokenizer import tokenize

"""
factor = <number> | "(" expression ")"
term = factor { "*"|"/" factor }
expression = term { "+"|"-" term }
statement = <print> expression | expression
"""

def parse_factor(tokens):
    """
    factor = <number> | "(" expression ")"
    """
    token = token[0]
    if (token["tag"] == "number"):
        return {
            "tag":"number",
            "value": token["value"]
        }, tokens[1:]
    if (token["tag"] == "("):
        ast, tokens = parse_expression(tokens[1:])
        assert tokens[0]["tag"] == ")"
        return ast, tokens[1:]
    raise Exception(f"Unexpected token '{token['tag']}' ")

def test_parse_factor():
    """
    factor = <number> | "(" expression ")"
    """

def parse_expression(tokens):
    return parse_factor(tokens)

def parse_statement(tokens):
    #...
    return ast, tokens

# def parse(tokens): # --> AST
#     #...
#     return AST

# def test_parse():
#     t = tokenize("1")
#     ast = parse(t)
#     assert ast == {
#         #
#     }

if (__name__ == "__main__"):
    print("Testing parser...")
    test_parse_factor()
    print("Done.")
