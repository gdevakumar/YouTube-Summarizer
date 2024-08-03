# YouTube Video Summarizer

This versatile tool is designed to enhance your productivity and understanding by leveraging advanced AI technologies to process and extract valuable information from YouTube videos. It can run using **OpenAI**, **Anthropic** and **Groq** APIs and uses advanced prompts provided by (Fabric)[https://github.com/danielmiessler/fabric]. Here’s what this app can do:

**Summarize YouTube Videos**: Easily create concise summaries of lectures, news, and other video content. Perfect for quick reviews and note-taking.
**Extract Wisdom**: Generate meaningful insights and key takeaways from podcasts and discussions. Ideal for capturing the essence of lengthy content.
**Generate Flashcards**: Create flashcards for efficient studying from educational and technical videos, helping you retain key concepts.
**Custom Prompts**: Input your custom prompts to tailor the AI’s response to your specific needs, whether it’s for Q&A generation, detailed analysis, or any other purpose.


## Steps to run this localy (via command line)
1. Clone this repository
```
git clone https://github.com/gdevakumar/YouTube-Summarizer.git
cd YouTube-Summarizer
```

2. Install Python from [here](https://www.python.org/downloads/) and project dependencies
```
pip install -r requirements.txt
```

3. Create `.env` file, add API keys and save the file. (*any one oAPI key is enough*)
```
OPENAI_API_KEY=sk-pr...
ANTHROPIC_API_KEY=sk-ant-aNOc0z...
GROQ_API_KEY=gsk_8K...
```

4. Launch the Web UI with streamlit application
```
streamlit run app.py
```

