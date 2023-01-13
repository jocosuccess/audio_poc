1. git clone https://github.com/jocosuccess/audio_poc.git
2. cd audio_poc
3. sudo docker build -t audio_poc
4. docker run \
    --rm \
    -i -t \
    -u $(id -u):$(id -g) \
    -v /dev/shm:/dev/shm \
    -v $(pwd):/home/app/build \
    -v $HOME:/home/app \
    -v /media:/media \
    -v /usr/local/lib64:/usr/local/lib64 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /etc/machine-id:/etc/machine-id \
    -v /run/user/$(id -u)/pulse:/run/user/$(id -u)/pulse \
    -v $HOME/.pulse:/home/app/.pulse \
    --env DISPLAY \
    --env HOME='/home/app' \
    --privileged \
    --group-add $(getent group audio | cut -d: -f3) \
    --name "app" \
    audio_poc bash