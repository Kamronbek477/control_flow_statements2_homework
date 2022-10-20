def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n%10
    n//=10

    b=n%10
    n//=10

    c=n%10
    n//=10

    d=n%10
    n//=10

    q=n%10
    n//=10

    if a>b and a>c and a>d and a>q:
        return  1
    if b>a and b>c and b>d and b>q:
        return  2
    if c>a and c>b and c>d and c>q :
        return  3
    if d>a and d>b and d>c and d>q :
        return  4
    if q>a and q>b and q>c and q>d:
        return  5
print(main(71945))