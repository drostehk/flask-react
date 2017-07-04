FROM python:2
EXPOSE 8000

RUN groupadd -r deploy && useradd -u 1000 --no-log-init -r -m -g deploy deploy

COPY pytest.ini setup.py setup.cfg gunicorn.py /home/deploy/app/
COPY src /home/deploy/app/src
WORKDIR /home/deploy/app

RUN chown -R deploy /home/deploy/app

RUN python setup.py install

USER deploy

#Logs
RUN mkdir -p /home/deploy/log
ENV LOGS '/home/deploy/log'
VOLUME /home/deploy/log

# Install application and requirements
VOLUME /home/deploy/app

CMD ["gunicorn", "--forwarded-allow-ips=*", "--config=gunicorn.py", "wsgi:app"]
