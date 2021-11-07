#FROM python:3.8
#COPY ./ /app
#RUN python -m pip install --upgrade pip
#RUN pip install -r /app/requirements.txt
#WORKDIR /app/myprojec/
#CMD python infra_project/manage.py runserver 0:5000

FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python infra_project/manage.py runserver 0:5000