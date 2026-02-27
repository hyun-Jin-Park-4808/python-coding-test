# 문자의 아스킷 코드를 구하는 방법: ord('a') => 97
# 0번째 인덱스부터 'a' ~ 'z'를 넣으려면? (ord(문자) - ord('a')) 을 인덱스로 만들어서 넣어주면 된다!
# 아스킷 코드를 다시 문자로 바꾸는 방법: chr(97) => 'a'
# 문자가 알파벳인지 확인하는 방법: 'a'.isalpha() => True

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)
    max_occurred_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > alphabet_occurrence_array[max_occurred_alphabet_index]:
            max_occurred_alphabet_index = index

    return chr(max_occurred_alphabet_index + ord('a'))

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
