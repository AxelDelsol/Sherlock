FROM python:3.6

ARG TextRazorKey
ENV TEXTRAZOR_API_KEY=${TextRazorKey}

COPY . app/
WORKDIR app

RUN pip install -r requirements.txt

ENV FLASK_APP="sherlock"

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]