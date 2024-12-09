import socket
import json
import struct

def connect_to_tcp_server(host='localhost', port=8899):
    # 创建一个复杂的结构化 JSON 数据
    data = {
        "method": "set",
        "lamp": {
            "id": 0,
            "action": 1,
            "mtime": -1
        }
    }
    json_data = json.dumps(data)

    try:
        # 创建 TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 连接到服务器
        client_socket.connect((host, port))
        print(f"Connected to TCP server {host}:{port}")
        
        # 发送 JSON 数据长度（4 字节的无符号整型）
        print(json_data)
        json_data_length = len(json_data)
        # client_socket.sendall(struct.pack('!I', json_data_length))

        # 发送 JSON 数据
        client_socket.sendall(json_data.encode())
        print(f"Sent structured JSON data to server : {json_data_length}")

        # 接收服务器响应
        response = client_socket.recv(1024)
        print("Received response from server:", response.decode())
        
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # 关闭连接
        client_socket.close()
        print("Connection closed.")

# 调用函数发送数据
connect_to_tcp_server(host='localhost', port=8899)



