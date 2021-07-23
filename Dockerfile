FROM python:3.9.6-slim-buster
ENV PORT 5000

ADD . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE $PORT
RUN chmod +x ./start.sh
CMD ["./start.sh"]