FROM python:3
# no default value
ENV OWNER=ranazrad
ENV REPOSITORY=pr-notifier
ADD main.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
