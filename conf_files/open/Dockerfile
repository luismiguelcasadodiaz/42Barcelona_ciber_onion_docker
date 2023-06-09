FROM nginx:1.25.0-alpine-slim

# ------------------------        NGINX SERVICE SETUP
WORKDIR /etc/nginx
#RUN sed -i -e '/    keepalive_timeout  65;/a     server_tokens off;' nginx.conf

WORKDIR /etc/nginx/conf.d
     
COPY open.conf open.conf

WORKDIR /usr/share/nginx/html
COPY index.html index.html

WORKDIR /var/www/open
COPY index_open.html index_open.html
#EXPOSE 80
#EXPOSE 81
#EXPOSE 82
#EXPOSE 83
#EXPOSE 4242

# ------------------------        Container users creation
#I use this user at 42 Barcelona
ENV USER lcasado-

#I use this user at home
#ENV USER luis


RUN adduser  -h /var/www/open -s /bin/sh -g "Luis Miguel Casado Díaz" $USER; echo -n $USER':1234' |chpasswd
WORKDIR /home/$USER/
RUN mkdir .ssh
RUN chmod 700 .ssh
RUN chown $USER:$USER .ssh
WORKDIR /home/$USER/.ssh
COPY id_rsa.pub id_rsa.pub
COPY authorized_keys authorized_keys
RUN chmod 600 authorized_keys

# ------------------------        SSH SERVICE SETUP

# -y & -q avoids answer questions in instalation process.ls
RUN apk update
RUN apk upgrade -y -q
RUN apk add openssh-server -y -q

WORKDIR /etc/ssh
RUN sed -i -e '/^#Port 22/i Protocol 2' sshd_config
# Barcelona 42 Bootcamp challenge requirement
ENV PORT 4242
RUN sed -i -e '/#Port 22/ s/#Port 22/Port '$PORT'/' sshd_config
RUN sed -i -e '/#PermitRootLogin/ s/#PermitRootLogin prohibit-password/PermitRootLogin no/' sshd_config
RUN sed -i -e '/^PermitRootLogin no/a AllowUsers lcasado-' sshd_config
# SSHD Logging activation
RUN sed -i -e '/#SyslogFacility AUTH/  s/#//' sshd_config
RUN sed -i -e '/#LogLevel INFO/  s/#//' sshd_config
# SSHD logging with RSA KEYS
RUN sed -i -e '/#PubkeyAuthentication yes/  s/#//' sshd_config
RUN sed -i -e '/#AuthorizedKeysFile/  s/#//' sshd_config

RUN sed -i -e '/#MaxAuthTries 6/  s/#MaxAuthTries 6/#MaxAuthTries 3/' sshd_config
RUN sed -i -e '/#PermitEmptyPasswords no/ s/#//' sshd_config
RUN sed -i -e '/#AllowTcpForwarding yes/ s/#AllowTcpForwarding yes/AllowTcpForwarding no/' sshd_config
RUN sed -i -e '/X11Forwarding yes/ s/X11Forwarding yes/X11Forwarding no/' sshd_config
RUN sed -i -e '/#ClientAliveInterval 0/ s/#ClientAliveInterval 0/ClientAliveInterval 120/' sshd_config
RUN sed -i -e '/#Banner none/ s/#Banner none/Banner \/etc\/ssh\/banner.txt/' sshd_config

COPY banner.txt banner.txt

# via SSH this user will go directly to see html files
#RUN echo 'Match User '$USER >> sshd_config
#RUN echo '   ChrootDirectory /var/www/open' >> sshd_config
#RUN echo '   ForceCommand internal-sftp' >> sshd_config
# The ForceCommand internal-sftp line ensures that the user can only use 
# SFTP (SSH File Transfer Protocol) for file operations. 
# This further limits their capabilities to navigate the filesystem.

#RUN ssh-keygen -A
#RUN /usr/sbin/sshd -D -e "$@"
#RUN /usr/sbin/sshd  -e "$@"


#RUN /usr/sbin/sshd

# This is to ensure your server have a tiny fingerprint
# no specific headers or unique version number to track you down.

EXPOSE $PORT
ENTRYPOINT ["/entrypoint.sh"]
COPY entrypoint.sh /



