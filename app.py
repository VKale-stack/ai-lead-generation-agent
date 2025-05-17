import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def qualify_lead(lead_info):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Qualify this lead: {lead_info}"}
        ]
    )
    return response['choices'][0]['message']['content']

st.title("AI Lead Generation Agent")
lead_info = st.text_area("Enter lead information:")
if st.button("Qualify Lead"):
    if lead_info:
        result = qualify_lead(lead_info)
        st.success(result)
    else:
        st.error("Please enter lead information.")
