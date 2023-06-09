FROM nginx:1.25.0-alpine-slim

# -y & -q avoids answer questions in instalation process.ls
RUN apk update
RUN apk upgrade -y -q
RUN apk add --no-cache openssh -y -q

WORKDIR /etc/ssh
RUN sed -i -e '/^#Port 22/i Protocol 2' sshd_config
RUN sed -i -e '/#Port 22/ s/#Port 22/Port 4242/' sshd_config
RUN sed -i -e '/#PermitRootLogin/ s/#PermitRootLogin prohibit-password/PermitRootLogin no/' sshd_config
RUN sed -i -e '/^PermitRootLogin no/a AllowUsers lcasado-' sshd_config
# SSHD Logging activation
RUN sed -i -e '/#SyslogFacility AUTH/  s/#//' sshd_config
RUN sed -i -e '/#LogLevel INFO/  s/#//' sshd_config

#RUN sed -i -e '/#PubkeyAuthentication yes/  s/#//' sshd_config
#RUN sed -i -e '/#AuthorizedKeysFile/  s/#//' sshd_config

RUN sed -i -e '/#MaxAuthTries 6/  s/#MaxAuthTries 6/#MaxAuthTries 3/' sshd_config
RUN sed -i -e '/#PermitEmptyPasswords no/ s/#//' sshd_config
RUN sed -i -e '/#AllowTcpForwarding yes/ s/#AllowTcpForwarding yes/AllowTcpForwarding no/' sshd_config
RUN sed -i -e '/X11Forwarding yes/ s/X11Forwarding yes/X11Forwarding no/' sshd_config
RUN sed -i -e '/#ClientAliveInterval 0/ s/#ClientAliveInterval 0/ClientAliveInterval 120/' sshd_config
RUN sed -i -e '/#Banner none/ s/#Banner none/Banner \/etc\/ssh\/banner.txt/' sshd_config

COPY banner.txt banner.txt



ENV USER lcasado-
RUN adduser  -h /home/$USER -s /bin/sh -g "Luis Miguel Casado Díaz" $USER; echo -n $USER':1234' | chpasswd
WORKDIR /home/$USER/
RUN mkdir .ssh
RUN chmod 700 .ssh
WORKDIR /home/$USER/.ssh

RUN ssh-keygen -A

# -A: This is a flag or option that is specific to the ssh-keygen command. 
# In this context, it instructs ssh-keygen to generate missing host keys for all available host 
# key algorithms.
# The -A flag is useful in scenarios where you have just installed SSH on a server and want 
# to generate host keys for all the available algorithms automatically. it overwrites any 
# existing host keys that might have already been generated



#COPY id_rsa.pub id_rsa.pub
#COPY authorized_keys authorized_keys
#RUN chmod 600 authorized_keys

#RUN /usr/sbin/sshd

# This is to ensure your server have a tiny fingerprint
# no specific headers or unique version number to track you down.
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /


#CMD ["/bin/sh"]
#ENTRYPOINT ["/usr/sbin/sshd", "-D", "-e", "$@"]
#ENTRYPOINT ["/usr/sbin/sshd"]

#exec /usr/sbin/sshd -D -e "$@"




