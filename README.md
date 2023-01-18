We can implement a connection between docker and host using netjack2.
https://github.com/jackaudio/jackaudio.github.com/wiki/WalkThrough_User_NetJack2

1. git clone https://github.com/jocosuccess/audio_poc.git
2. cd audio_poc
3. sudo docker build -t audio_poc
4. docker run \
    --rm \
    -i -t \
    -u $(id -u):$(id -g) \
    -v /dev/shm:/dev/shm \
    -v /usr/local/lib64:/usr/local/lib64 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /etc/machine-id:/etc/machine-id \    
    --env DISPLAY \    
    --privileged \
    --group-add $(getent group audio | cut -d: -f3) \
    --name "app" \
    audio_poc bash
5. in docker terminal, run the following commands for slave jack server
    jackd -R -d net -a 225.3.19.154 -p 19000    
6. in host terminal, run the following commands for master jack server
    jackd -d alsa -P merge
    open new terminal and jack_load netmanager
