print("python practice start")

print("1.변수 대입-------------------------------------------")
#1.변수 대입
user_id = "standard_user"
password = "secret_sauce"
count = 1

print(user_id)
print(password)
print(count)

print("2.if문(True)-------------------------------------------")
#2.if문(True)
login_success = True

if login_success:
    print("로그인 성공")
else:
    print("로그인 실패")       

#if문(False)
login_success = False

if login_success:
    print("로그인 성공")
else:
    print("로그인 실패")        

print("3.반목문(for)-------------------------------------------")
#3.반목문(for)
users = ["standard_user", "locked_out_user", "problem_user"]

for user in users:
    print(user)

print("4.함수-------------------------------------------")
#4.함수
def login():
    print("로그인 실행")

login()    

print("4.매개변수-------------------------------------------")
#4.매개변수(parameter) 사용하기 ex)로그인 정보를 함수에 전달
def login(user_id, password):
    print(user_id)
    print(password)

login("standard_user", "secert_sauce")

print("5.클래스-------------------------------------------")
 #5. 클래스
class LoginPage:
    def input_id(self):
        print("ID 입력")
    def input_password(self):
        print("비밀번호 입력") 
    def click_loin_button(self):
        print("로그인 버튼 클릭")           

login_page = LoginPage()

login_page.input_id()
login_page.input_password()
login_page.click_loin_button()