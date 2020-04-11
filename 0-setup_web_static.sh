#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install nginx
sudo service nginx start
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "with simple content, to test your Nginx configuration" >> /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test /data/web_static/current
chown ubuntu:ubuntu -R /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
