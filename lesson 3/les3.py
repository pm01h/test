f=open("./lesson 3/aaa.txt",'r')
#정렬 전 내용이 담겨있는 파일을 여는 코드입니다.


for line in f: #for문을 사용하여 line변수 안에 파일의 라인을 순서대로 저장합니다.
     a=line.split() #split함수를 이용하여 n번째 라인의 값을 리스트로 나타내어 a변수에 저장합니다.
     for i in range(5): #for문을 사용하여 총 5번의 반복으로 a변수의 i번째 자리 값을 정수형으로 받습니다.
          a[i]=int(a[i])
     a.sort() # 정수형으로 나타낸 n번째 줄의 값들을 오름차순으로 sort함수로 정렬합니다.
     for i in range(5): #for문을 다시 사용하여 정수형에서 문자형으로 변환합니다.
          a[i]=str(a[i])
     a=" ".join(a) #join함수를 이용하여 리스트를 문자열로 나타내서 a변수에 저장합니다.
     print(a) #n번째 라인의 정렬된 값을 정상적인 형태로 출력합니다.
 

f.close()#파일을 닫습니다.