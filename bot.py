import random

# 이 리스트에는 무작위 대답들이 들어있습니다 (원하시면 자신의 언어로 추가하거나 번역할 수 있습니다)
random_responses = ["정말 흥미롭군요, 더 말씀해주세요.",
                    "알겠습니다. 계속 말씀해주세요.",
                    "왜 그렇게 말씀하시나요?",
                    "요즘 날씨가 참 이상하죠?",
                    "주제를 바꿔볼까요?",
                    "어제 저녁 경기 보셨나요?"]

print("안녕하세요, 저는 마빈이라고 하는 간단한 로봇입니다.")
print("이 대화를 언제든지 '안녕'이라고 입력하면 종료할 수 있습니다")
print("답을 입력한 후 '엔터'를 누르세요")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자의 텍스트 입력을 기다립니다
    user_input = input("> ")
    if user_input == "안녕":
        # '안녕'을 입력하면 루프에서 벗어납니다
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화하게 되어 기뻤습니다, 안녕히 계세요!")
