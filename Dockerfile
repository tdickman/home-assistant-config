FROM homeassistant/home-assistant


ADD https://github.com/tdickman/home-assistant/raw/1a8a44fb0472601b4717d148dbae7f0278c20c76/homeassistant/components/switch/flux.py /usr/src/app/homeassistant/components/switch/
ADD https://github.com/tdickman/home-assistant/raw/7d9de19443ada21a0ba65fff66e62ef60ac82e92/homeassistant/components/sensor/darksky.py /usr/src/app/homeassistant/components/sensor/
