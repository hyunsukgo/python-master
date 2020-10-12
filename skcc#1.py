n = int(input("숫자를 입력"))
def solution(n):
    if n !=1:
        for f in range(2,n):
            if n % f == 0:
                return False
    else:
        return False
    n = int(input("숫자를 입력"))

    answer = 0
    return answer