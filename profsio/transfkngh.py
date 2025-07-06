#transformer Karnaugh

def transfkgh(expr) :
    expr = expr.replace('A','(A)')
    expr = expr.replace('a','(-A)')
    expr = expr.replace('B','(B)')
    expr = expr.replace('b','(-B)')
    expr = expr.replace('C','(C)')
    expr = expr.replace('c','(-C)')
    return expr