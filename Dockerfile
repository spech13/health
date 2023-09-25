FROM ubuntu

WORKDIR /django/apps

COPY . .

RUN apt clean && apt update && apt -qy install python3-pip && pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]