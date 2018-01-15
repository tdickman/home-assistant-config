This is my home-assistant configuration.

docker run -d --restart=always --name="home-assistant" -v /home/tom/.homeassistant:/config -v /etc/localtime:/etc/localtime:ro -v /etc/letsencrypt:/etc/letsencrypt:ro --net=host homeassistant/home-assistant:0.60.1
# docker run -d --restart=always --name="home-assistant" -v /home/tom/.homeassistant:/config -v /etc/localtime:/etc/localtime:ro -v /etc/letsencrypt:/etc/letsencrypt:ro --net=host hass-tom
docker run -d --restart=always -v /home/tom/.homeassistant/conf:/conf --name appdaemon acockburn/appdaemon:refactor

# Cert Renewal

sudo docker run -it --rm -p 80:80 --name certbot -v "/etc/letsencrypt:/etc/letsencrypt" -v "/var/lib/letsencrypt:/var/lib/letsencrypt"                 quay.io/letsencrypt/letsencrypt:latest certonly                 --standalone --standalone-supported-challenges http-01 --email tdickman@gmail.com -d home.epicconstructions.com
