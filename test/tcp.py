import socket

def hex_to_bytes(hex_str): 
    # 确保十六进制字符串的长度为偶数 
    if len(hex_str) % 2 != 0: 
        hex_str = '0' + hex_str 
    # 将十六进制字符串转换为字节数组 
    byte_data = bytes.fromhex(hex_str) 
    return byte_data 
# 示例输入 
# hex_str = "00000000000601050000FF00" 
# byte_data = hex_to_bytes(hex_str) 
# print("Original hex string:", hex_str) 
# print("Byte data:", byte_data) 
# print("Length:", len(byte_data))

# 定义十六进制字符串
hex_str1 = "00000000000601050001FF00"
hex_str2 = "00000000000601050002FF00"

# 将十六进制字符串转换为整数
int1 = int(hex_str1, 16)
int2 = int(hex_str2, 16)

# 相加两个整数
result_int = int1 + int2

# 将结果转换回十六进制字符串，并去掉前缀 '0x'
result_hex = hex(result_int)[2:].upper()

# 如果结果长度不够，填充前导零
max_len = max(len(hex_str1), len(hex_str2))
result_hex = result_hex.zfill(max_len)

print("Result in hexadecimal:", result_hex)


# 目标 IP 和端口
host = "192.168.1.35"
port = 8080

# 十六进制字符串转换为字节
#hex_string = "48656c6c6f20544350"
#byte_data = bytes.fromhex(result_hex)
# data = """
#        0000000000060105000AFF00
#        0000000000060105000BFF00
#        0000000000060105000CFF00
#        0000000000060105000DFF00
#        0000000000060105000EFF00
#        0000000000060105000FFF00
#        00000000000601050010FF00
#        00000000000601050011FF00
#        00000000000601050012FF00
#        00000000000601050013FF00
#        00000000000601050014FF00
#        00000000000601050015FF00
#        00000000000601050016FF00
#        00000000000601050017FF00
#        00000000000601050018FF00
#        00000000000601050019FF00
#        0000000000060105001AFF00
#        0000000000060105001BFF00
#        0000000000060105001CFF00
#        0000000000060105001DFF00
#        0000000000060105001EFF00
#        0000000000060105001FFF00
#00000000000B0110000000020400000000
#        """
byte_data = hex_to_bytes("00000000000601050005FF00")
print("Byte data:", byte_data) 

# 创建 TCP 连接并发送数据
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(byte_data)
    print("Data sent:", byte_data)
