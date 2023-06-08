FROM python:3.7-slim

#required to build numpy
RUN apt-get update \ 
    && apt-get install build-essential make gcc -y \
    && apt-get install dpkg-dev -y \ 
    && apt-get install libjpeg-dev -y

#install dependencies
RUN pip install --upgrade pip
RUN pip install dash
RUN pip install dash_bootstrap_components
RUN pip install numpy
RUN pip install pandas

#remove once numpy is ok
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get remove -y --purge dpkg-dev \
    && apt-get remove -y --purge libjpeg-dev \
    && apt-get auto-remove -y 

RUN rm -rf /var/lib/apt/lists/* \
    && find /usr/local/lib/python3.7 -name "*.pyc" -type f -delete

# move scipts and data into the container

COPY ./src ./
COPY ./data ./data

#the python app listens at app.run_server(debug=True, host= IPAddr, port=84)
ENTRYPOINT [ "/usr/local/bin/python3" ,"-m", "app"]