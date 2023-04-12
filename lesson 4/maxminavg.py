def max_number(a):
#함수이름을 max_number로 지정하고 a를 인수로 지정합니다.
    max_n=a[0] #max_n변수에 a리스트의 처음 값을 저장합니다.
    for i in a: #i변수에 a[n]번째 숫자를 저장하며 a리스트의 끝까지 반복합니다.
        if i>max_n: #만약 변수 i가 max_n보다 크면
            max_n=i #max_n변수에 i값을 갱신합니다.
    return max_n #max_n 변수를 리턴합니다.


def min_number(a):
#함수이름을 min_number로 지정하고 a를 인수로 지정합니다.
    min_n=a[0] #min_n변수에 a리스트의 처음 값을 저장합니다.
    for i in a: #i변수에 a[n]번째 숫자를 저장하며 a리스트의 끝까지 반복합니다.
        if i<min_n: #만약 변수 i가 min_n보다 작으면
            min_n=i #min_n변수에 i값을 갱신합니다.
    return min_n #min_n 변수를 리턴합니다.


def average(a):#average를 함수명으로 사용합니다.
    sum_n=0 #sum_n변수에 값을 초기화합니다.
    for i in a: #i변수에 a[n]번째 숫자를 저장하며 a리스트의 끝까지 반복합니다.
        sum_n=sum_n+i #sum_n값에 i변수를 더하여 총 10가지의 숫자의 합을 구합니다.
    avg=sum_n/len(a)#avg변수에 sum_n변수(총합)와 len함수로 a의 리스트 공간(10)을 나누어 평균값을 저장합니다.
    return avg#avg 변수를 를 리턴합니다.