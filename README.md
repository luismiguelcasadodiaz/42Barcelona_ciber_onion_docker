# 42Barcelona_ciber_Ft_onion
Serve a web page from a Tor network hidden service.

I would like to solve this challenge using Docker:

My approach want to set up three Docker;

1.- nginx Docker microservice
2.- Tor server microservice
3.- Python Dashboard micorservice (This is the Bonus part)



# Nginx official docker image

I use the official docker image with nginx

> docker pull nginx

I run the image an log in the container with a terminal to see if there is any update

> apt update
> apt list --upgradable

I get 

> libssl1.1/stable-security 1.1.1n-0+deb11u5 amd64 [upgradable from: 1.1.1n-0+deb11u4]
> openssl/stable-security 1.1.1n-0+deb11u5 amd64 [upgradable from: 1.1.1n-0+deb11u4]



> docker run --name some-nginx -d -p 8080:80 nginx



default directoris for the official nginx image are:

> logs /var/log/nginx/error.log
> root   /usr/share/nginx/html;
> index  index.html index.htm;

## nginx config files

### /etc/nginx.nginx.conf

```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```

###  /etc/nginx/conf.d/default.conf

```
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

}

```

Starting wiht this officeil immage i build the images for my the other three containers


# Nginx Docker wiht static html page

Docker file will adapt it the the image i will use in this challenge.



# Tor docker
## snowflake versus obfs
[source of info ](https://www.reddit.com/r/TOR/comments/scmdq4/snowflake_vs_obfs4_bridges_speed/?onetap_auto=true)


**obfs** bridges are hidden Tor relays with a static, non changing IP address that are running 24/7
**snowflake** they can have dynamic IP addresses. 

There are a lot more snowflakes than obfs bridges.

We will use for our project  snowflake

• Fortificación SSH. Se evaluará concienzudamente durante la evaluación.


• Una web interactiva, más impresionante que una triste página estática. Puedes utilizar librerías externas para ello, pero no un framework. Si no entiendes la diferencia entre ambos, no lo hagas.



# Static we page



![](./docs/dockerportmappping.png)


![Differences between python docker images](https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d)

# Lessons
Python package python depends on C libraries. 
No all Docker python images have tools to build Numpy python library

Alpine based images do not have. You must install missing building tools wiht APK add
Slim tagged images neither do have. you must install them using apt-get.

This is the reason why the Docker file for the Data Python Dash service Installs aditional packages
tht are removed after Numpy Instalation.