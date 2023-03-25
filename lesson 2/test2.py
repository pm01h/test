studentList = {"Park": "Korea"} #studentList 변수에 딕셔너리 Park(key)와 Korea(value)를 저장합니다.

name="Park" #name 변수 안에 "Park"를 저장합니다.
nation=studentList[name] 
#studentList변수안에 Park가 저장된 name 변수를 이용하여 value값을 nation 변수에 저장합니다.

print("\"Hi! I'm %s , and I'm from %s\"" % (name,nation)) 
#포매팅을 이용하여 이름과 국적 자리에 변수 name 과 nation을 알맞게 삽입합니다.
