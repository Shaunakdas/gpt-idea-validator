# Importing required packages
import streamlit as st
import openai

st.title("ZigZog")
st.sidebar.header("Speed up your startup validation journey by 3x with Zigzog.")
st.sidebar.info(
    '''This is a web application that gives you elevator pitch based on your startup idea.
       Enter your **startup idea** in the **text box** and **press enter** to receive
       a **response** from the Zigzog
       '''
    )

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
# Get OpenAI API key and source text input
openai_api_key = st.text_input("OpenAI API Key", type="password")
openai.api_key = "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"

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter startup idea here, to exit enter :q", "Smart watch for older women")
    if not openai_api_key.strip() or not user_query.strip():
        st.error("Please provide the missing fields.")
    if user_query != ":q" or user_query != "":
        prompt = "Craft a 30-second elevator pitch for following startup idea that highlights its unique value proposition and leaves a lasting impression: "+ user_query
        # Pass the query to the ChatGPT function
        response = ChatGPT(prompt)
        return st.write(f"{user_query} {response}")

def ChatGPT(user_query):
    '''
    This function uses the OpenAI API to generate a response to the given
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response

# call the main function
main()

