string = " 1,2 , 3 ,4,5" #string변수 안에 문자열을 삽입함

a=string.split(',') #a변수 안에 string변수에 담긴 문자열을 split을 사용하여 ,단위로 나눈 리스트를 삽임함

a[0]=a[0].strip() #a변수에 담긴 리스트의 각 자리에 strip을 사용하여 좌우 공백을 삭제함
a[1]=a[1].strip()
a[2]=a[2].strip()
a[3]=a[3].strip()
a[4]=a[4].strip()

print(a) #a변수에 담긴 모든 값을 출력함