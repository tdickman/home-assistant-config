docker run --name=appdaemon -d -p 5050:5050 \
    --restart=always \
    -v /home/tom/.homeassistant/conf:/conf \
    -v /etc/localtime:/etc/localtime:ro \
    acockburn/appdaemon:latest
