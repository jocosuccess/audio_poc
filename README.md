# 1) First Solution

1. git clone https://github.com/jocosuccess/audio_poc.git
2. cd audio_poc
3. sudo docker build -t audio_poc .
4. sudo docker run \
    --rm \
    -i -t \
    -u $(id -u):$(id -g) \
    -v $HOME:/home/developer \
    -v /dev/shm:/dev/shm:rw \
    -v /usr/local/lib64:/usr/local/lib64 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /etc/machine-id:/etc/machine-id \
    -v /run/user/$(id -u)/pulse:/run/user/$(id -u)/pulse \
    -v $HOME/.pulse:/home/developer/.pulse \
    -v /var/lib/dbus:/var/lib/dbus
    --ipc=host \
    --env HOME='/home/developer' \
    --env DISPLAY \
    --env JACK_NO_AUDIO_RESERVATION=1 \
    --privileged \
    --group-add $(getent group audio | cut -d: -f3) \
    --cap-add=sys_nice --ulimit rtprio=95 --ulimit memlock=-1 --shm-size=256m \
    --name "app" audio_poc bash
5. in docker terminal, run jack_-simple_client. If got a beep, successful.
    otherwise, python3 main.py. If you see jack device, successful.

#########################################################################

# 2) Second Solution

We can implement a connection between docker and host using netjack2.
https://github.com/jackaudio/jackaudio.github.com/wiki/WalkThrough_User_NetJack2

1. git clone https://github.com/jocosuccess/audio_poc.git
2. cd audio_poc
3. sudo docker build -t audio_poc .
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
    --cap-add=sys_nice --ulimit rtprio=95 --ulimit memlock=-1 --shm-size=256m \
    --name "app" \
    audio_poc bash
5. in docker terminal, run the following commands for slave jack server
    jackd -R -d net -a 225.3.19.154 -p 19000    
6. in host terminal, run the following commands for master jack server
    jackd -d alsa -P merge
    open new terminal and jack_load netmanager
#########################################################################    
