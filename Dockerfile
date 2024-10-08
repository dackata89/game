FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8777
CMD [ "gunicorn","-b","0.0.0.0:8777","MainScores:app" ]
