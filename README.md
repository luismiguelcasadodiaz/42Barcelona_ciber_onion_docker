# 42Barcelona_ciber_Ft_onion
Serve a web page from a Tor network hidden service.

I would like to solve this challenge using Docker:

My approach want to set up three Docker;

1.- nginx Docker microservice
2.- Tor server microservice
3.- Python Dashboard micorservice (This is the Bonus part)



# Nginx docker

I use the official docker image with nginx

> docker pull nginx

From this image a Docker file will adapt it the the image i will use in this challenge.

## nginx config files


# Tor docker
## snowflake versus obfs
[source of info ](https://www.reddit.com/r/TOR/comments/scmdq4/snowflake_vs_obfs4_bridges_speed/?onetap_auto=true)


**obfs** bridges are hidden Tor relays with a static, non changing IP address that are running 24/7
**snowflake** they can have dynamic IP addresses. 

There are a lot more snowflakes than obfs bridges.

We will use for our project  snowflake

• Fortificación SSH. Se evaluará concienzudamente durante la evaluación.


• Una web interactiva, más impresionante que una triste página estática. Puedes utilizar librerías externas para ello, pero no un framework. Si no entiendes la diferencia entre ambos, no lo hagas.