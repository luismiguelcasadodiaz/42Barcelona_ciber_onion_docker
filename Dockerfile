# Use Alpine Linux
FROM alpine:latest

# Maintainer
LABEL  42_Barcelona_Cibersecurity_Bootcamp = luismiguelcasadodiaz@gmail.com 
USER root

#install ft_onion required packages
# --no-cache avoid index dowload
RUN apk update && \
	apk upgrade && \
#	apk add --no-cache openrc && \
#	apk add --no-cache openssh && \
#	apk add --no-cache doas && \
	apk add --no-cache nginx 

# Preparation of daemons manager
#RUN openrc
#RUN touch /run/openrc/softlevel

# ssh config
#RUN rc-update add sshd
#EXPOSE 22

#RUN rc-service add nginx

RUN hostname -s nginx_server
ENV USER admin_nginx
#RUN echo 'rc_provide="loopback net"' >> /etc/rc.conf

#create user "admin_nginx- with home directory"
RUN adduser  -h /home/$USER -s /bin/ash -g "Administrador nginx" $USER; echo -n $USER':123' :chpasswd
RUN addgroup $USER wheel

RUN echo 'permit persist : wheel' >> /etc/doas.conf
RUN chown -c root:root /etc/doas.conf
RUN chmod -c 0400 /etc/doas.conf
RUN chmod o-rx /home/$USER

#RUN	cp /root/.bashrc /home/lcasado-/
#RUN	mkdir /home/lcasado-/infection
#RUN mkdir /home/lcasado-/randsonware
#	chown -R --from=root lcasado- /home/lcasado-

#create directory for page
#ENV WEBDIR /var/www/
#USER ${USER}
#RUN doas mkdir /var/www/
RUN touch /run/nginx.pid
WORKDIR /etc/nginx/
RUN mv nginx.conf nginx.conf.bck
COPY my_nginx.conf nginx.conf
#WORKDIR /etc/nginx/conf.d
#COPY www.lmcd.net.conf www.lmcd.net.conf
WORKDIR /var/www/html
COPY index.html index.html


#RUN rc-service start nginx

#COPY requirements.txt requirements.txt
#COPY . .

#ENTRYPOINT ["/bin/bash"]
#CMD ["Docker"]
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]

#install python
#RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python


#to see why openrc can not set hostmanem
#https://github.com/neeravkumar/dockerfiles/blob/master/alpine-openrc/Dockerfile
