def minus(left, right):
    return left - right
def mult(left, right):
    return left * right
def add(left, right):
    return left + right
def div(left, right):
        return left / right

def tree(tugas):
    if isinstance(tugas, tuple):
        left, operator, right = tugas
        operators = {'+': add, '-': minus, '*': mult, '/': div}
        return operators[operator](tree(left), tree(right))
    else:
        return tugas

expression_tree = ((2, '+', 3), '*', (5, '-', 1))

result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)