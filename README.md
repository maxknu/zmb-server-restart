# How to create Docker container from this Python Flask App

docker build -t damtrapa/zmb-restart-app .

docker run -it -p 5000:5000 -d damtrampa/zomboid-restart-app

docker push damtrapa/zmb-restart-app