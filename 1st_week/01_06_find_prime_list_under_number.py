# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]
input = 20

# for - else 문법 사용하기
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for prime in prime_list: # n보다 작은 소수 목록이 else 구문에서 구해지므로 이런 식으로 쓸 수 있다.
            # N의 제곱근보다 크지 않은 어떤 소수로도 나누어떨어지지 않으면 소수이다.
            if prime * prime <= n and n % prime == 0: # 소수가 아닌 경우: n의 제곱근보다 작은 소수로 나누어 떨어질 때
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)
