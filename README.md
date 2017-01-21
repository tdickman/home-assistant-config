This is my home-assistant configuration.

docker run -d --name="home-assistant" -v /home/tom/.homeassistant:/config -v /etc/localtime:/etc/localtime:ro -v /etc/letsencrypt:/etc/letsencrypt:ro homeassistant/home-assistant
