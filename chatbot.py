import streamlit as st
import openai  # Replace with Gemini API when available

# Set your API key for OpenAI or Gemini (if applicable)
# openai.api_key = 'your_openai_api_key'

# Streamlit UI layout settings for minimalistic chatbot design
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Centering the chatbot interface
st.markdown(
    """
    <style>
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 85vh;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.markdown("<h1 style='text-align: center;'>Minimal Chatbot</h1>", unsafe_allow_html=True)

# Input text bar
user_input = st.text_input("Type your message here:", "")

# Response placeholder
if 'response' not in st.session_state:
    st.session_state['response'] = ''

# Process the user input and fetch AI response when the input is submitted
if user_input:
    with st.spinner("Thinking..."):
        # You can replace the below block with Gemini API calls once available
        response = openai.Completion.create(
            engine="text-davinci-003",  # OpenAI's model, replace with "Gemini" when available
            prompt=user_input,
            max_tokens=150
        )
        # Save the response in session state
        st.session_state['response'] = response.choices[0].text.strip()

# Display the AI's response
if st.session_state['response']:
    st.markdown(f"**Bot:** {st.session_state['response']}")

# Clearing the input bar
if st.button("Clear"):
    st.session_state['response'] = ""
    st.experimental_rerun()
