from tokenizer import tokenize
from parser import parse

def evaluate(ast):
    if (ast['tag'] == 'number'):
        return ast['value']
    if (ast['tag'] in ["+","-","*","/"]):
        left_value = evaluate(ast["left"])
        right_value = evaluate(ast["right"])

def test_evaluate_number():
    print("testing evaluate number...")
    assert evaluate({'tag': 'number', 'value': 4}) == 4

def eval(s):
    tokens = tokenize(s)
    ast = parse(tokens)
    result = evaluate(ast)
    return result

if (__name__ == "__main__"):
    print("Testing evaluator...")
    test_evaluate_number()
    print("Done.")
