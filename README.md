# create images by going into directories and using these commands.
cd server
<!--  -->
sudo docker build -t server .
<!--  -->
cd ../client/
<!--  -->
sudo docker build -t client .

# open a terminal, RUN this command.
sudo docker run -it --rm --network=host --name localhost server bash

# open another terminal and RUN this command.
sudo docker run -it --rm --network=host client bash

# get back to first terminal and write this command
python3 server.py

# go to the second terminal and write this command
python3 client.py
