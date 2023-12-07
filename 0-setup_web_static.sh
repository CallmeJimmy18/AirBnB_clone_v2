#!/usr/bin/env bash
# Bash script that sets up web servers for web_static deployment
#!/usr/bin/env bash
# Bash script that sets up web servers for web_static deployment
if [ -z "$(command -v nginx)" ]; then
        sudo apt-get update
        sudo apt-get -y install nginx
fi

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

echo "<html>
  <head>
  </head>
  <body>
    This is a test page
  </body>
</html>" > /data/web_static/releases/test/index.html

current_link="/data/web_static/current"
if [ -L "$current_link" ]; then
        sudo rm "$current_link"
fi

sudo ln -s "/data/web_static/releases/test" "$current_link"

chown -R ubuntu:ubuntu /data
chmod -R 755 /data

echo 'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
                add_header X-Served-By \$hostname;
                alias /data/web_static/current/;
                index index.html;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
                index index.html;
        }
}' | sudo tee /etc/nginx/sites-available/default > /dev/null

if [ "$(pgrep -c nginx)" -le 0 ]; then
        sudo service nginx start
else
        sudo service nginx restart
fi
