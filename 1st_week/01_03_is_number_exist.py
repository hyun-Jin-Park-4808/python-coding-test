def is_number_exist(number, array):
    for element in array: # array의 길이만큼 아래 연산 실행
        if element == number: # 비교 연산 1번 실행
            return True # 시간복잡도는 최악의 경우를 기준으로 구하므로 N만큼 걸린다.
    return  False

result = is_number_exist
# 운이 좋은 경우 1만큼의 연산이 소요된다.
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))

# 최악의 경우 N만큼의 연산이 소요된다.
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))

print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))