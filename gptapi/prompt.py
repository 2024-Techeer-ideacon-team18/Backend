import openai
from myproject.settings import API_KEY

openai.api_key = API_KEY

def resultGpt():
    messages = [
        {
            "role": "system",
            "content": "너는 자바 개발자야. 자바의 라이브러리, 클래스, 메소드에 대해 많은 지식을 가지고 있어서 너한테 질문하는 사람들에게 많은 지식을 전하고 싶어해."
        }
    ]
    content = input()
    print("content: ", content)

    messages.append({
        "role": "user",
        "content": "java.math 라이브러리에 대해서 최소 100글자를 채워서 설명해줘. 추가로 math 라이브러리에서 자주 사용되는 method를 15가지도 소개하고 어떤 기능과 어디서 사용되는지 설명해주라. 각 method당 설명은 최소 100글자정도로 해줘. 이 이상으로 설명 가능"
    })

    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=messages)

    chat_response = completion.choices[0].message.content
    return chat_response
