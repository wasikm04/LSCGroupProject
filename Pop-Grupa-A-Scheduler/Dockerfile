FROM python:3.7-alpine

WORKDIR /app

#Copy list of libraries needed to install
COPY requirements.txt .
COPY entrypoint.sh .

#upgrade pip and install libraries
RUN apk update && apk add gcc libffi-dev python3-dev musl-dev
RUN pip install --upgrade --quiet pip --no-cache-dir -r requirements.txt

#expose port 5000
EXPOSE 5555

RUN chmod a+x entrypoint.sh

CMD [ "/bin/sh", "entrypoint.sh" ]



