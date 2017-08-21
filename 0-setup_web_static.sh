#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
#install nginx if not alreasy install
sudo apt-get update
sudo apt-get install -y nginx
# create given folders if not already exists
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# Create a fake HTML file in the given path just for testing the config
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give recursive ownership of the /data/ folder to ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
# restart nginx
sudo service nginx restart
