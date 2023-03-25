a_E=int(input("A English : ")) 
#a_E변수에 a의 영어점수를 입력받음
a_M=int(input("A Mathematics : "))
#a_M변수에 a의 수학점수를 입력받음

b_E=int(input("b English : "))
#b_E변수에 b의 영어점수를 입력받음
b_M=int(input("b Mathematics : "))
#b_M변수에 b의 영어점수를 입력받음

ab_ES=a_E+b_E
#a의 영어점수와 b의 영어점수를 합한 값을 ab_ES변수에 저장함
ab_MS=a_M+b_M
#a의 수학점수와 b의 수학점수를 합한 값을 ab_MS변수에 저장함

ab_EA=(ab_ES) / 2
#a와 b의 영어점수를 합한 값에 2를 나누어 영어평균값을 ab_EA변수에 저장함
ab_MA=(ab_MS) / 2
#a와 b의 수학점수를 합한 값에 2를 나누어 수학평균값을 ab_MA변수에 저장함

print("%s\n\t\ta\tb\tSum\tAverage\n%s\nEnglish\t\t%d\t%d\t%d\t%0.2f\n%s\n\
Mathematics\t%d\t%d\t%d\t%0.2f\n%s" % ('-'*50,'-'*50,a_E,b_E,ab_ES,ab_EA,'-'*50,a_M,b_M,ab_MS,ab_MA,'-'*50,))
#포맷팅을 이용하여 '-'문자를 50번 곱하여 하나의 줄을 만들고 \n바로 앞에 계속 사용하여 표 모양을 만들음
#차례대로 a와 b의 영어점수,총합,평균을 출력하고 다음 줄에는 a와b의 수학정수 총합 , 평균을 출력함

