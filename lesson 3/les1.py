a=int(input("정가를 입력하시오. : ")) # a변수에 정가를 입력받습니다.

gift=a/100
#사은품을 주기 위해 gift 변수에 a변수에 입력받은 정가를 100으로 나눈 값을 저장합니다.
if gift>=1:#gift에 저장된 값이 1보다 크거나 같을 시 아래 문장을 출력합니다.
     print("10층에서 사은품 %d만원을 받아가세요." %gift)#포맷팅하여 %d자리에 gift변수를 대입해서 사운픔 가격을 출력합니다.
if a<100:#정가가 100만원 미만일 시
     price=a*0.9 #price변수에 정가에 10%할인된 가격을 저장합니다.
else: #위 조건문에 해당이 안되면 100만원 이상이므로
     price=a*0.85 #price변수에 정가에 15%할인된 가격을 저장합니다.


print("상품의 가격 = %0.1f" % price)#price변수를 float으로 포매팅하여 소수점 첫번째 자리로 출력하게 합니다.