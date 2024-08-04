# YouTube Video Summarizer

This versatile tool is designed to enhance your productivity and understanding by leveraging advanced AI technologies to process and extract valuable information from YouTube videos. It can run using **OpenAI**, **Anthropic** and **Groq** APIs and uses advanced prompts provided by [Fabric](https://github.com/danielmiessler/fabric). Here’s what this app can do:

- **Summarize YouTube Videos**: Easily create concise summaries of lectures, news, and other video content. Perfect for quick reviews and note-taking.
- **Extract Wisdom**: Generate meaningful insights and key takeaways from podcasts and discussions. Ideal for capturing the essence of lengthy content.
- **Generate Flashcards**: Create flashcards for efficient studying from educational and technical videos, helping you retain key concepts.
- **Custom Prompts**: Input your custom prompts to tailor the AI’s response to your specific needs, whether it’s for Q&A generation, detailed analysis, or any other purpose.


## Steps to run this locally (via command line)
1. Clone this repository
```
git clone https://github.com/gdevakumar/YouTube-Summarizer.git
cd YouTube-Summarizer
```


2. Create virtual environment to isolate your packages (*optional*)
- On Windows:
```
python -m venv env
env\Scripts\activate
```
- On Linux/Mac:
```
python -m venv env
source env/bin/activate
```


3. Install project dependencies/packages
```
pip install -r requirements.txt
```


4. Create `.env` file, add API key(s) and save the file. (*any one oAPI key is enough*)
```
OPENAI_API_KEY=sk-pr...
ANTHROPIC_API_KEY=sk-ant-aNOc0z...
GROQ_API_KEY=gsk_8K...
```


5. Launch the Web UI with streamlit application
```
streamlit run app.py
```


## Video

<div>
    <a href="https://www.loom.com/share/8c1151c953184406894b95bd52598bcc?sid=c6d3fb8d-dda9-4186-9b1c-7033fdfbc079">
      <p>Video URL</p>
    </a>
</div>
