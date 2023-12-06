#!/usr/bin/env bash
# Bash script that sets up web servers for web_static deployment
if [ -z "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

sudo mkdir -p "/data"
sudo mkdir -p "/data/web_static"
sudo mkdir -p "/data/web_static/releases"
sudo mkdir -p "/data/web_static/shared"
sudo mkdir -p "/data/web_static/releases/test"

echo "<html>
  <head>
  </head>
  <body>
    This is a test page
  </body>
</html>" > /data/web_static/releases/test/index.html

current_link="/data/web_static/current"
if [ -L "$current_link" ]; then
	sudo -rm "$current_link"
fi

sudo ln -s "/data/web_static/releases/test" "$current_link"

sudo chown -R ubuntu:ubuntu /data

echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	
	server_name _;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}" > /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
        sudo service nginx start
else
        sudo service nginx restart
fi
