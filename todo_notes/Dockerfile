FROM python:3.9.2

RUN pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
RUN sed -i 's/force_text/force_str/g' /usr/local/lib/python3.9/site-packages/graphene_django/utils/utils.py
RUN pip install gunicorn
