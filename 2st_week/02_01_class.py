class Person:
    def __init__(self, name_param): # 생성자, self는 자기자신의 값
        self.name = name_param
        print("hi hi", self)

    def talk(self):
        print("hi hi", self.name, "입니다.")
#    pass # 아무런 내용이 없다는 의미

person_1 = Person("유재석") # 클래스 생성자를 통해 하나의 객체를 만들겠다는 의미, hi hi <__main__.Person object at 0x1024667b0>
print(person_1) # <__main__.Person object at 0x1024667b0>
print(person_1.name) # 유재석
person_1.talk() # hi hi 유재석 입니다.

person_2 = Person("박명수") # (): 생성자
print(person_2) # <__main__.Person object at 0x102680f50>
print(person_2.name)
person_2.talk()