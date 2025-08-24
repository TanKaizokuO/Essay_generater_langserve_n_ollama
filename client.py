import requests
import streamlit as st

def get_response(input_text):
    response = requests.post("http://127.0.0.1:8000/essay/invoke",
                             json={'input':{'topic':input_text}})
    data = response.json()
    # print(data)
    return data['output']

st.title("Essay Generator")
topic = st.text_input("Enter a topic:")
if st.button("Generate Essay"):
    if topic:
        essay = get_response(topic)
        answer = essay.replace(essay[0:essay.rfind("</think>")+8],"Here is your essay \n")
        st.write(answer)
    else:
        st.warning("Please enter a topic.")



        #answer = essay.replace(essay[0:essay.rfind("</think>")+1],"Here is your essay \n")