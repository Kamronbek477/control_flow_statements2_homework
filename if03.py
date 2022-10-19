def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a<c or a>c and a<b:
        return a
    if b>a and b<c or b>c and b<a:
        return b
    if c>a and c<b or a>b and a<a:
        return c

print(main(23,34,28))