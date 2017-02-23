This is my home-assistant configuration.

docker run -d --name="home-assistant" -v /home/tom/.homeassistant:/config -v /etc/localtime:/etc/localtime:ro -v /etc/letsencrypt:/etc/letsencrypt:ro -v /home/tom/.ssh:/root/.ssh:ro --net=host hass-dev
docker run -d -v /home/tom/.homeassistant/conf:/conf --name appdaemon appdaemon:latest
