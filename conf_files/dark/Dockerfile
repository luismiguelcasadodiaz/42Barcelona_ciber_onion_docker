FROM debian:bookworm-slim

# -y & -q avoids answer questions in instalation process.
# Allow package managers to access metadata over https

RUN apt update
RUN apt upgrade -y -q
RUN apt install gpg  -y -q
RUN apt install apt-transport-https  -y -q
RUN apt install wget -y -q
#RUN apt install software-properties-common  -y -q

WORKDIR /etc/apt/sources.list.d


RUN echo "deb     [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org bookworm main" >  tor.list
RUN echo "deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org bookworm main" >> tor.list

WORKDIR /usr/share/keyrings
RUN wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor > tor-archive-keyring.gpg
#RUN touch tor-archive-keyring.gpg
#RUN mv auxfile /usr/share/keyrings/tor-archive-keyring.gpg

RUN apt update
RUN apt install tor deb.torproject.org-keyring -y -q

WORKDIR /etc/tor
COPY torrc torrc

WORKDIR /var/lib/tor/hidden_service/
COPY index.html index.html
COPY hs_ed25519_public_key hs_ed25519_public_key
COPY hs_ed25519_secret_key hs_ed25519_secret_key


RUN chmod 700 /var/lib/tor/hidden_service/

EXPOSE 9050

ENTRYPOINT [ "/bin/tor" ]

#WORKDIR /etc/ssh
#RUN sed -i -e '/^#Port 22/i Protocol 2' sshd_config
#RUN sed -i -e '/#Port 22/ s/#Port 22/Port 4242/' sshd_config
#RUN sed -i -e '/#PermitRootLogin/ s/#PermitRootLogin prohibit-password/PermitRootLogin no/' sshd_config
#RUN sed -i -e '/^PermitRootLogin no/a AllowUsers lcasado-' sshd_config
#RUN sed -i -e '#HiddenServiceDir /var/lib/tor/hidden_service/  s/#//' torrc
#RUN sed -i -e '/#AuthorizedKeysFile/  s/#//' sshd_config

#RUN sed -i -e '/#MaxAuthTries 6/  s/#MaxAuthTries 6/#MaxAuthTries 3/' sshd_config
#RUN sed -i -e '/#PermitEmptyPasswords no/ s/#//' sshd_config
#RUN sed -i -e '/#AllowTcpForwarding yes/ s/#AllowTcpForwarding yes/AllowTcpForwarding no/' sshd_config
#RUN sed -i -e '/X11Forwarding yes/ s/X11Forwarding yes/X11Forwarding no/' sshd_config
#RUN sed -i -e '/#ClientAliveInterval 0/ s/#ClientAliveInterval 0/ClientAliveInterval 120/' sshd_config
#RUN sed -i -e '/#Banner none/ s/#Banner none/Banner \/etc\/ssh\/banner.txt/' sshd_config

#COPY banner.txt banner.txt







