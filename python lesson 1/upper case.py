a=ord(input("Enter the undercase alphabet : ")) # a변수에 소문자를 입력받고 ord함수를 이용해 아스키 코드로 변환하여 저장함

z=ord("a")-ord("A") # z변수에 아스키코드 a와 A의 값을 빼서 소문자에서 대문자로 변환할 수 있는 차이값을 저장함

a_un=chr(a) #a_un변수에 1행에 입력받은 아스키코드를 chr함수를 이용해 문자로 변환하여 저장함
a_up=chr(a-z) 
#a_up변수에 1행에 입력받은 아스키코드와 3행에서 만든 차이값을 구하는 아스키코드를 뺸 후 chr함수를 이용해 문자로 변환하여 저장함

print("Under case : %s\nUpper case : %s" % (a_un,a_up))#만들어두었던 a_un변수와 a_up변수를 포매팅하여 각각 알맞게 출력함