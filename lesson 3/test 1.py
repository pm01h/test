total=int(0) #y로 얼마나 대답했는지 알기위해 total변수를 만듭니다.
print("초식남 테스트를 시작합니다.(대답은 y or n)")#테스트의 시작을 알립니다.
A=input("격투기가 왜 재밌는지 모르겠다. :")#질문을 하고 A변수에 대답을 입력받습니다.
if A=="y": #y로 대답했을 시 total변수에 1을 더합니다. 그러지 않을 시 변화 없이 다음 질문으로 넘어갑니다.
     total=total+1
A=input("회식에 건배할 때도 음료수도 OK :") #계속해서 테스트를 이어 나갑니다.
if A=="y":
     total=total+1
A=input("고백을 받으면, 일단 누군가에게 상담한다. :")
if A=="y":
     total=total+1
A=input("소녀취향의 만화가 싫지 않다.")
if A=="y":
     total=total+1
A=input("여자친구들과 잘 어울리지만, 연애로 발전하는 경우가 거의 없다.:")
if A=="y":
     total=total+1
A=input("편의점 신제품에 항상 관심을 가지다. :")
if A=="y":
     total=total+1
A=input("일할 때, 간식(특히 과자)를 옆에 둔다. :")
if A=="y":
     total=total+1
A=input("외출보다 집에 있는 것을 더 좋아한다. :")
if A=="y":
     total=total+1
A=input("이성을 위해 돈을 쓰는 것보다 다양한 취미생활을 즐기는 인생을 산다. :")
if A=="y":
     total=total+1


print("초식남 테스트가 끝났습니다.")#테스트가 끝났음을 알려줍니다.
if total>=6: # total값이 6보다 크거나 같을 시 아래 문장을 출력합니다.
     print("당신의 초식도는 90% 입니다.")
elif total>=3:# total값이 3보다 크거나 같을 시 아래 문장을 출력합니다.
     print("당신의 초식도는 60% 입니다.")
else: #위 조건문보다 숫자가 낮을 시 아래 문장을 출력합니다.
     print("당신의 초식도는 20% 입니다.")