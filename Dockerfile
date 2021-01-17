FROM python:3.8-slim

ENV DASH_DEBUG_MODE False
COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "app.py"]