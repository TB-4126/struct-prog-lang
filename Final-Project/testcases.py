#testcases.c
#Thomas Bond
#2025-12-5

import sys
from cevaluator import evaluate

"""The only reason this sys.path shenanigans is here is because
Python does not like it when you try to import source files in different directories,
so I found this quick and dirty solution.
Is there a cleaner way of doing this? probably, but as of the time I'm writing this I don't have time to find it.
So you get this instead."""

sys.path.append('src/')
from tokenizer import tokenize
from parser import parse

printed_string = None

def test_evaluate_number():
    print("testing evaluate number")
    assert evaluate({"tag":"number","value":4}) == 4

def test_evaluate_addition():
    print("testing evaluate addition")
    ast = {
        "tag":"+",
        "left":{"tag":"number","value":1},
        "right":{"tag":"number","value":3}
        }
    assert evaluate(ast) == 4

def test_evaluate_subtraction():
    print("testing evaluate subtraction")
    ast = {
        "tag":"-",
        "left":{"tag":"number","value":3},
        "right":{"tag":"number","value":2}
        }
    assert evaluate(ast) == 1

def test_evaluate_multiplication():
    print("testing evaluate multiplication")
    ast = {
        "tag":"*",
        "left":{"tag":"number","value":3},
        "right":{"tag":"number","value":2}
        }
    assert evaluate(ast) == 6

def test_evaluate_division():
    print("testing evaluate division")
    ast = {
        "tag":"/",
        "left":{"tag":"number","value":4},
        "right":{"tag":"number","value":2}
        }
    assert evaluate(ast) == 2

def eval(s, environment={}):
    tokens = tokenize(s)
    ast = parse(tokens)
    result = evaluate(ast, environment)
    return result

def test_evaluate_expression():
    print("testing evaluate expression")
    assert eval("1+2+3") == 6
    assert eval("1+2*3") == 7
    assert eval("(1+2)*3") == 9
    assert eval("(1.0+2.1)*3") == 9.3
    assert eval("1<2") == True
    assert eval("2<1") == False
    assert eval("2>1") == True
    assert eval("1>2") == False
    assert eval("1<=2") == True
    assert eval("2<=2") == True
    assert eval("2<=1") == False
    assert eval("2>=1") == True
    assert eval("2>=2") == True
    assert eval("1>=2") == False
    assert eval("2==2") == True
    assert eval("1==2") == False
    assert eval("2!=1") == True
    assert eval("1!=1") == False
    # tokens = tokenize("-1")
    # ast = parse(tokens)
    # result = evaluate(ast, {})
    # print(ast, result)
    # exit(0)

    assert eval("-1") == -1
    assert eval("-(1)") == -1
    assert eval("!1") == False
    assert eval("!0") == True
    assert eval("0&&1") == False
    assert eval("1&&1") == True
    assert eval("1||1") == True
    assert eval("0||1") == True
    assert eval("0||0") == False


def test_evaluate_identifier():
    print("testing evaluate identifier")
    try:
        assert eval("x+3") == 6
        raise Exception("Error expected for missing value in environment")
    except Exception as e:
        assert "not found" in str(e) 
    assert eval("x+3", {"x":3}) == 6
    assert eval("x+y",{"x":4,"y":5}) == 9
    assert eval("x+y",{"$parent":{"x":4},"y":5}) == 9

def test_evaluate_print():
    print("testing evaluate print")
    assert eval("print 3") == None    
    assert printed_string == "3"
    assert eval("print 3.14") == None    
    assert printed_string == "3.14"

def test_evaluate_assignment():
    print("testing evaluate assignment")
    env = {"x":4,"y":5}
    assert eval("x=7",env) == 7
    assert env["x"] == 7

def test_if_statement():
    print("testing if statement")
    env = {"x":4,"y":5}
    assert eval("if(1){x=8}",env) == None
    assert env["x"] == 8
    assert eval("if(0){x=5}else{y=9}",env) == None
    assert env["x"] == 8
    assert env["y"] == 9

def test_while_statement():
    print("testing while statement")
    env = {"x":4,"y":5}
    assert eval("while(x<6){y=y+1;x=x+1}",env) == None
    assert env["x"] == 6
    assert env["y"] == 7


if (__name__ == "__main__"):
   print("Testing cevaluator...")
   test_evaluate_number()
   test_evaluate_addition()
   test_evaluate_subtraction()
   test_evaluate_multiplication()
   test_evaluate_division()
   test_evaluate_expression()
   test_evaluate_print()
   test_evaluate_identifier()
   test_if_statement()
   test_while_statement()
   print("Done.")
