import requests

# llama2 response
def get_llama2_response(input_text):
    response = requests.post("http://localhost:8000/llama2/invoke",
                             json={"input":{
                                 "question":input_text
                             }})
    return response.json()["output"]

# gemma2 response
def get_gemma2_response(input_text):
    response = requests.post("http://localhost:8000/gemma2/invoke",
                             json={"input":{
                                 "question":input_text
                             }})
    return response.json()["output"]

# qwen2.5 response
def get_qwen25_response(input_text):
    response = requests.post("http://localhost:8000/qwen2.5/invoke",
                             json={"input":{
                                 "question":input_text
                             }})
    return response.json()["output"]

# phi3.5 response
def get_phi35_response(input_text):
    response = requests.post("http://localhost:8000/phi3.5/invoke",
                             json={"input":{
                                 "question":input_text
                             }})
    return response.json()["output"]


