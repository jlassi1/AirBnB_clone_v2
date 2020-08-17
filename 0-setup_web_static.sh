#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.

sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
printf %s "
server {
    listen 80;
    listen [::]:80 default_server;
    server_name https://khawla.tech/
    root   /var/www//html;
    index index.nginx-debian.html index.nginx-debian.html;
    add_header X-Served-By 1391-web-01-1596560744;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    location /hbnb_static {
        alias  /data/web_static/current;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
