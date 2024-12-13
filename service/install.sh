#!/bin/bash

# 创建日志目录
mkdir -p /var/log/sandtable
touch /var/log/sandtable/sandtable.log

# 设置合适的权限
chown nobody:nogroup /var/log/sandtable/sandtable.log
chmod 640 /var/log/sandtable/sandtable.log

# 拷贝配置文件 
mkdir -p /etc/sandtable 
cp config.conf /etc/sandtable/config.conf
cp lamp.json /etc/sandtable/lamp.json
# 设置配置文件的权限 
chown nobody:nogroup /etc/sandtable/config.conf 
chown nobody:nogroup /etc/sandtable/lamp.json 
chmod 640 /etc/sandtable/config.conf
chmod 640 /etc/sandtable/lamp.json

# 拷贝 sandtable 执行文件 
cp sandtable /usr/local/bin/sandtable
chown nobody:nogroup /usr/local/bin/sandtable 
chmod 755 /usr/local/bin/sandtable

# 复制服务文件到 systemd 目录
cp sandtable.service /etc/systemd/system/

# 重新加载 systemd 配置
systemctl daemon-reload

# 启动并启用服务
systemctl start sandtable
systemctl enable sandtable
