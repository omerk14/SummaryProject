FROM python:3.9-alpine
WORKDIR /app
ENV FLASK_APP=mainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8777
RUN ls -l /usr/local/bin
COPY / /app
CMD ["python", "mainScores.py"]