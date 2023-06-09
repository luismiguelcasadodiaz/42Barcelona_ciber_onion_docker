FROM debian:bookworm-slim

# -y & -q avoids answer questions in instalation process.
# Allow package managers to access metadata over https

WORKDIR /etc/apt/sources.list.d
RUN echo "deb     [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org bookworm main" >  tor.list
RUN echo "deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org bookworm main" >> tor.list

RUN apt update
RUN apt upgrade -y -q
RUN apt install gpg  -y -q
RUN apt install apt-transport-https  -y -q
RUN apt install wget -y -q

WORKDIR /usr/share/keyrings
RUN wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor > tor-archive-keyring.gpg

RUN apt update
RUN apt install tor deb.torproject.org-keyring -y -q


RUN apt remove -y --purge gpg \
    && apt remove -y --purge apt-transport-https \
    && apt remove -y --purge wget \
    && apt auto-remove -y 

WORKDIR /etc/tor
COPY torrc torrc

RUN mkdir /var/lib/tor/hidden_service_bonus/
RUN chmod 700 /var/lib/tor/hidden_service_bonus/

RUN mkdir /var/lib/tor/hidden_service_static/
RUN chmod 700 /var/lib/tor/hidden_service_static/

VOLUME hidden_service_bonus
VOLUME hidden_

ENTRYPOINT [ "/bin/tor" ]








