## v[문제 1]
text = '''Example Page
Welcome to the Example Page
This is a sample paragraph with text.
Visit us at Example.com
'''

word = input("검색어 입력:")

if word in text:
	print(f'{word}단어는 문자열에 존재합니다.')
	word1 = input("변경 단어 입력:")
	text2 = text.replace(word, word1)
	print(text2)

else:
	print(f'{word}단어는 문자열은 존재하지 않습니다.')

## 문제 2
text = "I am studying Python Programming"

word_num = len(text.split())

text2 = text.upper()

text3 = text.lower()

slicing = text[14:20]

print(f'단어 개수 : {word_num}')
print(f'대문자로 변경 : {text2}')
print(f'소문자로 변경 : {text3}')
print(f'슬라이싱 : {slicing}')


## 문제 3
matrix = [[1, 2, 3],
		  [4, 5, 6],
		  [7, 8, 9]]

sum = 0
for row in matrix:
	for i in row:
		print(i, end = ' ')
		sum += i
	print()
print(f'전체합:{sum}')

## 문제 4
import random
value = random.sample(range(1, 50), 10)


print('랜덤 생성 리스트:', value)
value.sort()
print('정렬된 리스트:', value)
for num in value:
	print(f"{num}: {'*'* num}")

## 문제 5
text = 'Python is a high-level, general-purpose programming language.'

count = {}

for ch in text:
	if ch.isalpha():
		if ch in count:
			count[ch] += 1
		else:
			count[ch] = 1

for k in sorted(count.keys()):
    print(f"({k}: {count[k]})", end=' ')
