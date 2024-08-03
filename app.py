import os
import streamlit as st
from markdown import markdown
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from prompts import summarize, extract_wisdom, flashcards
from summarize import get_gpt_response, get_claude_response, get_llama_response
load_dotenv()


# Initialize session state variables
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if 'response' not in st.session_state:
    st.session_state.response = None

st.title('YouTube Video Summarizer 📹')

st.info("""This app can help you with:
- **Summarizing** YouTube Videos
- **Extracting Wisdom** from your favorite podcast
- **Generating Flashcards** to help you in preparation
- Summarize in your way with Custom Prompting
""")

with st.sidebar:
    st.header('Configuration :hammer_and_wrench:')
    llm_engine = st.selectbox(":robot_face: Choose your LLM engine", ['OpenAI', 'Anthropic', 'Llama-3.1 405B (Groq)'])
    if llm_engine == 'OpenAI' and not os.environ.get('OPENAI_API_KEY', None):
        openai_api = st.text_input(':key: Paste OpenAI API Key')
        os.environ['OPENAI_API_KEY'] = openai_api
    if llm_engine == 'Anthropic' and not os.environ.get('ANTHROPIC_API_KEY', None):
        anthropic_api = st.text_input(':key: Paste Anthropic API Key')
        os.environ['ANTHROPIC_API_KEY'] = anthropic_api

task = st.selectbox(":clipboard: Choose the Task", ['Summarize', 'Extract Wisdom', 'Generate Flashcards', 'Custom Prompt'])

prompt = "You are a brilliant bot helping in summarizing huge information in the way user species it."
if task == 'Custom Prompt':
    st.info('Example: Summarize the text in less than 100 words to make it understandable to a 12 year old student.')
    prompt = st.text_area(":memo: Enter the prompt")

task_dict = {
    "Summarize": summarize,
    "Extract Wisdom": extract_wisdom,
    "Generate Flashcards": flashcards,
    "Custom Prompt": prompt
}

model_dict = {
    "OpenAI": get_gpt_response,
    "Anthropic": get_claude_response,
    "Llama-3.1 405B (Groq)": get_llama_response
}

URL = st.text_input(":link: Enter YouTube URL")

def submit():
    if not URL:
        st.warning("Enter a valid YouTube URL! :warning:")
        return
    if llm_engine == 'OpenAI' and not os.environ.get('OPENAI_API_KEY', None):
        st.warning(f"Please ensure {llm_engine} API key is set up!")
        st.session_state.submitted = False
    elif llm_engine == 'Anthropic' and not os.environ.get('ANTHROPIC_API_KEY', None):
        st.warning(f"Please ensure {llm_engine} API key is set up!")
        st.session_state.submitted = False
    elif llm_engine == '' and not os.environ.get('GROQ_API_KEY', None):
        st.warning(f"Please ensure {llm_engine} API key is set up!")
        st.session_state.submitted = False
    else:
        loader = YoutubeLoader.from_youtube_url(URL)
        transcript = loader.load()[0].page_content
        response = model_dict[llm_engine](transcript, task_dict[task])
        st.session_state.response = markdown(response)
        st.session_state.submitted = True

if st.button(":rocket: Submit"):
    submit()

if st.session_state.submitted:
    st.html(st.session_state.response)
    # Reset state after displaying the response
    st.session_state.submitted = False
    st.session_state.response = None
