FROM python:3.9

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
# Uncomment when model file is available
#COPY model.pkl model.pkl

EXPOSE 5000

CMD ["flask", "run"]