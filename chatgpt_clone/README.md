# **GPT Clone Bot**

## **Description**

This is a GPT clone app built using streamlit and Fast API. 
It uses the following llms to generate responses alternatively:
1. Gemma2 - 2 billion
2. Qwen2.5 - 3 billion
3. Phi3.5 - 3 billion
4. Llama2 - 7 billion

## **Setup**
1. Clone the repository into a folder
   * `git clone --filter=blob:none --no-checkout https://github.com/tirthspace/llms.git`
   * `git sparse-checkout set --cone` (The sparse chekout works on git version 2.25.0)
   * `git checkout main`
   * Clone the specific folder
     `git sparse-checkout set llms/chatgpt_clone`

2. Create and activate environment
    `python -m venv <virtual environment path>`

   For mac OS
    `source <virtual environment path>/bin/activate`

   For windows
    `<virtual environment path>\Scripts\activate`

3. Install the required packages in the environment
    * Go into the cloned application folder
    * `pip install -r requirements.txt`

## **Running the app on your local**
1. Open a terminal in your IDE and go into the app folder
    `python routes.py`

2. Open another terminal
    `streamlit run app.py`

This will launch the application in your browser!!!








