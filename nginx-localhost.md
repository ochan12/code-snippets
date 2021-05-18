# Create localhost reverse proxy with nginx (for developing)


1.  `brew install nginx`
2.  `sudo cat > /usr/local/etc/nginx/nginx.conf`


```sh
user YOUR_USER admin;

worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    sendfile        on;

    keepalive_timeout  65;

    server {
        listen       443 ssl;
        server_name  YOUR_SECURED_SITES;

        ssl_certificate      /usr/local/etc/nginx/cert.crt;
        ssl_certificate_key  /usr/local/etc/nginx/cert.key;

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;

        location / {
            proxy_pass YOUR_LOCALHOST_DEV_SERVER(localhost:3000, localhost:9000...);
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

3.  `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /usr/local/etc/nginx/cert.key -out /usr/local/etc/nginx/cert.crt`
4.  `sudo ngnix`
5.  Add entries to `/etc/hosts`

```
127.0.0.1 YOUR_SECURED_SITES;
```

6.  `npm run dev`
7.  Navigate to `YOUR_SECURED_SITES`
8.  If you get the *Privacy Error* tab, type right there on the open tab **thisisunsafe** and it will open
