# 安装Nextcloud All-in-One并配置反向代理

2024-03-18 分类：[学无止境](https://lala.im/category/jiaocheng) 阅读(4225) 评论(4)

[![img](https://cdn.jsdelivr.net/gh/xiya233/cdn@1.1/storage/0062WjpGgy1fvftx9j0gnj30ms01ojs4.jpg)](https://bwh88.net/aff.php?aff=36696&pid=72)

官方介绍，Nextcloud All-in-One Included are:

> Nextcloud
> High performance backend for Nextcloud Files
> Nextcloud Office (optional)
> High performance backend for Nextcloud Talk and TURN-server (optional)
> Nextcloud Talk Recording-server (optional)
> Backup solution (optional, based on BorgBackup)
> Imaginary (optional, for previews of heic, heif, illustrator, pdf, svg, tiff and webp)
> ClamAV (optional, Antivirus backend for Nextcloud)
> Fulltextsearch (optional)

建议系统配置：流畅运行至少4GB内存，如果要使用ClamAV则可能需要更多。

系统Debian12，安装需要用到的包：

```
apt -y update
apt -y install curl nginx python3-certbot-nginx
```

安装Docker：

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

新建目录以及docker-compose文件：

```
mkdir -p /opt/nextcloud && cd /opt/nextcloud && nano docker-compose.yml
```

写入如下配置：

```
version: '3.8'
services:
  nextcloud-aio-mastercontainer:
    image: nextcloud/all-in-one:latest
    init: true
    restart: always
    container_name: nextcloud-aio-mastercontainer
    volumes:
      - nextcloud_aio_mastercontainer:/mnt/docker-aio-config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - 8080:8080
    networks:
      - nextcloud-aio
    environment:
      - APACHE_PORT=11000
      - APACHE_IP_BINDING=127.0.0.1
      - NEXTCLOUD_UPLOAD_LIMIT=20G
      - NEXTCLOUD_MAX_TIME=7200
      - NEXTCLOUD_MEMORY_LIMIT=1024M

volumes:
  nextcloud_aio_mastercontainer:
    name: nextcloud_aio_mastercontainer

networks:
  nextcloud-aio:
    name: nextcloud-aio
    driver: bridge
    enable_ipv6: true
    ipam:
      driver: default
      config:
        - subnet: fd12:3456:789a:2::/64
```

[备注1]

其他的可选配置：https://github.com/nextcloud/all-in-one/blob/main/compose.yaml

启动：

```
docker compose up -d
```

先配置反代，新建nginx站点配置文件：

```
nano /etc/nginx/sites-available/nextcloud
```

写入如下配置：

```
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    listen 80;
    listen [::]:80; 
    server_name nextcloud.example.com;

    location / {
        proxy_pass http://127.0.0.1:11000$request_uri;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Accept-Encoding "";
        proxy_set_header Host $host;
        client_body_buffer_size 512k;
        proxy_read_timeout 86400s;
        client_max_body_size 0;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}
```

启用站点：

```
ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/nextcloud
```

签发TLS证书：

```
certbot --nginx --email example@lala.im --agree-tos --no-eff-email
```

再次编辑nginx站点配置文件：

```
nano /etc/nginx/sites-available/nextcloud
```

增加http2的配置：

```
...
    listen [::]:443 ssl http2 ipv6only=on; # managed by Certbot
    listen 443 ssl http2; # managed by Certbot
...
```

重载nginx使其生效：

```
systemctl reload nginx
```

打开你的Nextcloud All-in-One管理界面，注意地址是https协议，使用的自签名证书：https://ip:8080

首次打开会回显一窜密码，用这个密码进行登录：

[![img](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-18_10-47-15.png)](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-18_10-47-15.png)

配置域名，填写之前反代用的域名即可，本文使用的是nextcloud.example.com

[![img](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-10-27.png)](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-10-27.png)

配置时区：

[![img](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-14-54.png)](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-14-54.png)

配置要安装的功能：

[![img](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-14-02.png)](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-14-02.png)

确认无误后开始部署，如果要使用当前最新版的话就勾选这个install nextcloud 28，否则安装的是27版本：

[![img](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-13-17.png)](https://lala.im/wp-content/uploads/2024/03/lala.im_2024-03-17_13-13-17.png)

这应该是目前搭建一个全功能nextcloud最简单、方便的方式了，并且还内置了备份功能，我试了一下这个备份功能也是正常可用的，对于nextcloud这种脆弱的软件来说，一个可靠的备份方案是非常重要的。。