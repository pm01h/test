import number10 #10개의 숫자를 구하는 파일을 가져옵니다.
import maxminavg#최대값,최소값,평균값을 구하는 파일을 가져옵니다.

a = number10.tennumber() #a변수에 10개의 숫자를 저장합니다.
max_number = int(maxminavg.max_number(a))#max_number변수에 최대값을 저장합니다.
#max_number함수에 10개의 값이 담긴 리스트 a를 인수로 하여 최대값을 구하도록 합니다.
min_number = int(maxminavg.min_number(a))#min_number변수에 최소값을 저장합니다.
#min_number함수에 10개의 값이 담긴 리스트 a를 인수로 하여 최소값을 구하도록 합니다.
avg = float(maxminavg.average(a))#avg변수에 평균값을 실수형으로 저장합니다.
#average함수에 10개의 값이 담긴 리스트 a를 인수로 하여 평균값을 구하도록 합니다.

print("최대값은 : %d" % max_number)
#포매팅을 사용하여 최대값이 담긴 max_number을 호출합니다.
print("최소값은 : %d" % min_number)
#포매팅을 사용하여 최소값이 담긴 min_number을 호출합니다.
print("평균값은 : %0.1f" % avg)
#포매팅을 사용하여 평균값이 담긴 avg을 호출하고 소수점 첫번쨰까지 출력합니다.

