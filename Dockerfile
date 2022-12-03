FROM python:2
# no default value
ENV OWNER=
ENV REPOSITORY=
ADD main.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
