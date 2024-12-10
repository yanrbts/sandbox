import socket
import json
import struct
import pandas as pd
from tabulate import tabulate

def process_and_display_data(response_json):
    try:
        # 确保 response_json 是字典
        if isinstance(response_json, str):
            response_json = json.loads(response_json)
        
        # 检查是否包含 "lamps" 键
        if "lamps" not in response_json:
            raise KeyError("响应数据中没有找到 'lamps' 键。")

        # 提取 lamps 数据
        lamps_data = response_json["lamps"]
        
        # 确保 lamps 是列表
        if not isinstance(lamps_data, list):
            raise ValueError("'lamps' 键的值不是列表，请检查数据格式。")

        # 将数据转换为 DataFrame
        df = pd.DataFrame(lamps_data)

        # 如果需要对状态为 1 的行显示绿色
        def highlight_row(row):
            if row["status"] == 1:
                return [f"\033[92m{val}\033[0m" for val in row]
            return row

        # 应用高亮逻辑
        colored_data = df.apply(highlight_row, axis=1).values.tolist()

        # 使用 tabulate 打印表格
        print(tabulate(colored_data, headers=df.columns, tablefmt="grid"))

    except Exception as e:
        print("处理数据时发生错误:", e)
def connect_to_tcp_server(host='localhost', port=8899):
    # 创建一个复杂的结构化 JSON 数据
    data = {
        "method": "get",
        "id": 0
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
        # 接收服务器响应
        response = client_socket.recv(1024*16)
        response_str = response.decode()

        try:
            # 将接收到的响应格式化为 JSON
            response_json = json.loads(response_str)
            formatted_response = json.dumps(response_json, indent=4, ensure_ascii=False)
            print("Received response from server (formatted JSON):")
            # print(formatted_response)
            
            process_and_display_data(formatted_response)
        except json.JSONDecodeError:
            print("Failed to decode response as JSON. Raw response:")
            print(response_str)
        
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # 关闭连接
        client_socket.close()
        print("Connection closed.")

# 调用函数发送数据
connect_to_tcp_server(host='localhost', port=8899)