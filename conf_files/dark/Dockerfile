FROM debian:buster-slim

# -y & -q avoids answer questions in instalation process.
# Allow package managers to access metadata over https

RUN apt update
RUN apt upgrade -y -q
RUN apt install apt-transport-https 

WORKDIR /etc/apt/sources.list.d


RUN echo "deb     [arch=amd64] https://deb.torproject.org/torproject.org buster main" > tor.list
RUN echo "deb-src [arch=amd64] https://deb.torproject.org/torproject.org buster main" >> tor.list


RUN wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null

RUN wget -qO- https://archive.torproject.org/tor-package-archive/torbrowser/12.0.6/tor-expert-bundle-12.0.6-linux-x86_64.tar.gz


#WORKDIR /etc/ssh
#RUN sed -i -e '/^#Port 22/i Protocol 2' sshd_config
#RUN sed -i -e '/#Port 22/ s/#Port 22/Port 4242/' sshd_config
#RUN sed -i -e '/#PermitRootLogin/ s/#PermitRootLogin prohibit-password/PermitRootLogin no/' sshd_config
#RUN sed -i -e '/^PermitRootLogin no/a AllowUsers lcasado-' sshd_config
#RUN sed -i -e '/#PubkeyAuthentication yes/  s/#//' sshd_config
#RUN sed -i -e '/#AuthorizedKeysFile/  s/#//' sshd_config

#RUN sed -i -e '/#MaxAuthTries 6/  s/#MaxAuthTries 6/#MaxAuthTries 3/' sshd_config
#RUN sed -i -e '/#PermitEmptyPasswords no/ s/#//' sshd_config
#RUN sed -i -e '/#AllowTcpForwarding yes/ s/#AllowTcpForwarding yes/AllowTcpForwarding no/' sshd_config
#RUN sed -i -e '/X11Forwarding yes/ s/X11Forwarding yes/X11Forwarding no/' sshd_config
#RUN sed -i -e '/#ClientAliveInterval 0/ s/#ClientAliveInterval 0/ClientAliveInterval 120/' sshd_config
#RUN sed -i -e '/#Banner none/ s/#Banner none/Banner \/etc\/ssh\/banner.txt/' sshd_config

#COPY banner.txt banner.txt



ENV USER lcasado-
RUN adduser  -h /home/$USER -s /bin/bash -g "Luis Miguel Casado Díaz" $USER; echo -n $USER':1234' :chpasswd
WORKDIR /home/$USER/
RUN mkdir .ssh
RUN chmod 700 .ssh
WORKDIR /home/$USER/.ssh
#COPY id_rsa.pub id_rsa.pub
#COPY id_rsa id_rsa
#COPY authorized_keys authorized_keys
RUN chmod 600 authorized_keys

RUN service ssh start

WORKDIR /usr/share/nginx/html
COPY index.html index.html

EXPOSE 80
EXPOSE 22

CMD ["nginx", "-g", "daemon off;"]

# https://hub.docker.com/r/osminogin/tor-simple/



