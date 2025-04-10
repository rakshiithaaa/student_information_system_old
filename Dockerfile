FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask

ENV flask_app=app.py
ENV flask_run_host=0.0.0.0
ENV flask_run_port=5000

EXPOSE 5000
 
CMD ["flask", "run"]