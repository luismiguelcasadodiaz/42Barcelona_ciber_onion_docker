FROM nginx:latest

RUN apt update
RUN apt upgrade -y -q
RUN apt install openssh-server -y -q

WORKDIR /etc/ssh
#RUN sed -i -e '/^#Port 22/i Protocol 2' sshd_config
#RUN sed -i -e '/#Port 22/ s/#Port 22/Port 4242/' sshd_config
RUN sed -i -e '/#PermitRootLogin/ s/#PermitRootLogin prohibit-password/PermitRootLogin no/' sshd_config
RUN sed -i -e '/^PermitRootLogin no/a AllowUsers lcasado-' sshd_config
RUN sed -i -e '/#PubkeyAuthentication yes/  s/#//' sshd_config
RUN sed -i -e '/#AuthorizedKeysFile/  s/#//' sshd_config

#RUN sed -i -e '/#MaxAuthTries 6/  s/#MaxAuthTries 6/#MaxAuthTries 3/' sshd_config
#RUN sed -i -e '/#PermitEmptyPasswords no/ s/#//' sshd_config
#RUN sed -i -e '/#AllowTcpForwarding yes/ s/#AllowTcpForwarding yes/AllowTcpForwarding no/' sshd_config
#RUN sed -i -e '/X11Forwarding yes/ s/X11Forwarding yes/X11Forwarding no/' sshd_config
#RUN sed -i -e '/#ClientAliveInterval 0/ s/#ClientAliveInterval 0/ClientAliveInterval 120/' sshd_config
RUN sed -i -e '/#Banner none/ s/#Banner none/Banner \/etc\/ssh\/banner.txt/' sshd_config

COPY banner.txt banner.txt



ENV USER luis
RUN adduser  -h /home/$USER -s /bin/bash -g "Luis Miguel Casado Díaz" $USER; echo -n $USER':1234' :chpasswd
WORKDIR /home/$USER/
RUN mkdir .ssh
RUN chmod 700 .ssh
WORKDIR /home/$USER/.ssh
COPY id_rsa.pub id_rsa.pub
COPY id_rsa id_rsa
COPY authorized_keys authorized_keys
RUN chmod 600 authorized_keys

RUN service ssh start

WORKDIR /usr/share/nginx/html
COPY index.html index.html

EXPOSE 80
EXPOSE 22

CMD ["nginx", "-g", "daemon off;"]



