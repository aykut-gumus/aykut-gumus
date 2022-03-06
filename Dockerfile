FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD config/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT [ "/entrypoint.sh" ]
