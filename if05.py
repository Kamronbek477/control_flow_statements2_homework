def main(n):
    """Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    
    """
    a=n%10
    b=n%100//10
    c=n%1000//100
    d=n%10000//1000
    q=n//10000
    if a>b and a>c and a>d and a>q:
        return a
    if b>a and b>c and b>d and b>q:
        return b
    if c>a and c>b and c>d and c>q:
        return c
    if d>a and d>b and d>c and d>q:
        return d
    if q>a and q>b and q>c and q>d:
        return q
print(main(98345))