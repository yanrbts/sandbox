# sandtable
If not configured, use the default configuration file ‘config.conf’
```
git clone http://192.168.1.93:8888/kxyk/ai_sandbox.git
cd ai_sandbox
make
./sandtable /path/to/config.conf
```
**configure**:
```sh
tcpport 8899        # TCP 链接端口
udpip 192.168.1.18  # UDP 沙盘路由器地址
udpport 1000        # UDP 沙盘路由器端口
tcp-keepalive 300   # 是 TCP 协议的一项功能，用于在网络连接中保持连接的活动状态，特别是在没有数据传输时。它通过周期性发送探测报文（keepalive probes）来检测远程对等方是否仍然存活
tcp-backlog 511     # 是在 TCP 网络编程中用于定义 listen() 系统调用的     backlog参数的配置项。它表示内核为该端口的未完成连接队列（半连接队列）和已完成连接队列（全连接队列）所允许的最大挂起连接数。

# 灯开启关闭命令
D9999 D0000
A0001 B0001
A0002 B0002
A0003 B0003
A0004 B0004
```
