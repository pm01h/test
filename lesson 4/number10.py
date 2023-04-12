def tennumber(): #함수 이름을 tennumber로 지정하였습니다.
    a=[] #a변수에 리스트를 초기화시켜줍니다.
    for i in range(1,11): #1부터 10까지의 반복을 시행합니다.
        a.append(int(input("%d번째 숫자를 입력하세요." % i)))
        # append함수에 int(input())을 입력하여 정수를 입력받습니다.(총 10번 반복)
    return a #a변수를 리턴합니다.