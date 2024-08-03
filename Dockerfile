FROM python:3.12.3-alpine3.20

WORKDIR /app

COPY . /app/

EXPOSE 8501

ENV GROQ_API_KEY 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

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py"]
