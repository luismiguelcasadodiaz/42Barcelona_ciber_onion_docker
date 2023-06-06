FROM python:3.7-slim

RUN apt-get update \ 
    && apt-get install build-essential make gcc -y \
    && apt-get install dpkg-dev -y \ 
    && apt-get install libjpeg-dev -y

# when i tried wiht Alpine....
#RUN apk update
#RUN apk add build-essential
#RUN apk make 
#RUN apk gcc
#RUN apk add dpkg-dev
#RUN apk add libjpeg-dev

RUN pip install --upgrade pip
RUN pip install dash
RUN pip install dash_bootstrap_components
RUN pip install numpy

RUN pip install pandas

RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get remove -y --purge dpkg-dev \
    && apt-get remove -y --purge libjpeg-dev \
    && apt-get auto-remove -y 

     
RUN rm -rf /var/lib/apt/lists/* \
    && find /usr/local/lib/python3.7 -name "*.pyc" -type f -delete


#COPY requirements.txt ./requirements.txt

COPY ./src ./
COPY ./data ./data

EXPOSE 1234
ENTRYPOINT [ "/usr/local/bin/python3" ,"-m", "app"]
#CMD /bin/bash