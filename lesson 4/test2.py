def factorial(n): #함수명을 factorial로 지정하고 n을 인수로 저장했습니다.
    if n==1: #n이 1이면
        return 1 # 1을 리턴하여 종료합니다.
    else: #1이 아니면
        return factorial(n-1)*n
    #n-1하여 n이1이 될때까지 자기 자신을 계속 호출하게 만들고 그 전의 값과 계속 곱하게 합니다.


n=int(input("숫자를 입력하세요 : ")) # 숫자를 정수형으로 입력받고 n변수에 저장합니다.
result=factorial(n) #result변수에 factorial(n)값을 저장합니다.
print("%d의 팩토리얼 값 : %d"%(n,result)) #각 자리에 알맞게 포매팅하여 출력합니다.