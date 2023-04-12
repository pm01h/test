a = [] #a변수에 빈 리스트를 생성합니다.
total = 0#평균값을 구하기 위해 입력받은값의 총합을 total변수에 받을 준비를 합니다.


for i in range(10): #range(10)을 이용하여 총 10번의 반복을 합니다.
     num = int(input("숫자를 입력하세요: "))#num변수에 값을 입력받습니다.
     a.append(num)#append함수를 이용하여 입력받은 값을 a리스트에 차곡차곡 저장합니다.
     total = total+ num #total변수에 입력받은 값을 차근차근 더해줍니다.


minimum = a[0] #최소값을 구하기 위해 맨 처음 a리스트의 0번째 값을 저장합니다.
maximum = a[0] #최대값을 구하기 위해 맨 처음 a리스트의 0번째 값을 저장합니다.
for num in a: #num변수에 a리스트에 있는 10가지의 값을 차례대로 저장합니다.
     if num < minimum:#a리스트의 n번째 값이 이전 리스트의 값보다 작으면 minimum변수에 그 값을 저장하여 최소값을 구합니다.
          minimum = num
     if num > maximum:#a리스트의 n번째 값이 이전 리스트의 값보다 크면 maximum변수에 그 값을 저장합니다.
          maximum = num


average = total / 10#입력받은 모든 값의 합인 total변수를 10으로 나누어 평균을 구하여 average변수에 저장합니다.
print("최대값은: %d\n최소값은: %d\n평균값은: %0.1f" % (maximum, minimum, average))
#포매팅하여 각 자리에 알맞은 변수를 넣어 출력합니다.