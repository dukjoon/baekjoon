def get_a_b(num):
    return 100 - num


def get_c(a, b):
    return 100 - (a+b)


def get_d(a, b):
    return a * b


def get_q(d):
    return d // 100


def get_r(d):
    return d % 100


def calculate_two_digits(c, q, r):
    return c + q, r



def pooang_and_jongyoon(num1, num2):
    a, b = get_a_b(num=num1), get_a_b(num=num2)
    c = get_c(a=a, b=b)
    
    d = get_d(a=a, b=b)
    q = get_q(d=d)
    r = get_r(d=d)
    
    first_two_digit, last_two_digit = calculate_two_digits(c=c, q=q, r=r)
    
    return f"{a} {b} {c} {d} {q} {r}", f"{first_two_digit} {last_two_digit}"


def print_answer(answer):
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    
    answer = pooang_and_jongyoon(num1, num2)
    
    print_answer(answer=answer)