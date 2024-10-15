import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

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

# Check if user_input is empty before sending to the API
if user_input:
    # Response placeholder
    if 'response' not in st.session_state:
        st.session_state['response'] = ''

    # Process the user input and fetch AI response when the input is submitted
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated model, replace with "Gemini" when available
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ]
            )
            st.session_state['response'] = response['choices'][0]['message']['content']

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please type a message to get a response.")

# Display the AI's response
if st.session_state.get('response'):
    st.markdown(f"**Bot:** {st.session_state['response']}")

# Clear button to reset the input and response
if st.button("Clear"):
    st.session_state['response'] = ""
    st.experimental_rerun()
