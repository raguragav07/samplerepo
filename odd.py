# Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

def check_number(x):
    if x%2==0:
        return("even")
    return("odd")
print(check_number(5))