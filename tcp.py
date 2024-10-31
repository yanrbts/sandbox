# import socket
# import json

# def connect_to_tcp_server(host='localhost', port=8899, message="Hello, TCP Server!"):
#     try:
#         # 创建一个 TCP socket
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
#         # 连接到服务器
#         client_socket.connect((host, port))
#         print(f"Connected to TCP server {host}:{port}")
        
#         # 发送消息
#         client_socket.sendall(message.encode())
#         print(f"Sent message to server: {message}")
        
#         # 接收服务器响应
#         response = client_socket.recv(1024)
#         print(f"Received message from server: {response.decode()}")
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # 关闭连接
#         client_socket.close()
#         print("Connection closed.")

# # 示例调用


# import json

# data = {
#     "company": "Tech Innovations Ltd.",
#     "address": {
#         "street": "123 Innovation Drive",
#         "city": "Silicon Valley",
#         "state": "CA",
#         "zip": "94043"
#     },
#     "employees": [
#         {
#             "id": 1,
#             "name": "Alice Johnson",
#             "age": 29,
#             "position": "Software Engineer",
#             "salary": 95000,
#             "projects": [
#                 {
#                     "project_id": 101,
#                     "project_name": "AI Development",
#                     "status": "Completed"
#                 },
#                 {
#                     "project_id": 102,
#                     "project_name": "Blockchain Integration",
#                     "status": "In Progress"
#                 }
#             ]
#         },
#         {
#             "id": 2,
#             "name": "Bob Smith",
#             "age": 34,
#             "position": "Data Scientist",
#             "salary": 105000,
#             "projects": [
#                 {
#                     "project_id": 103,
#                     "project_name": "Big Data Analysis",
#                     "status": "Completed"
#                 },
#                 {
#                     "project_id": 104,
#                     "project_name": "Machine Learning Model",
#                     "status": "In Progress"
#                 }
#             ]
#         },
#         {
#             "id": 3,
#             "name": "Carol White",
#             "age": 41,
#             "position": "Product Manager",
#             "salary": 120000,
#             "projects": [
#                 {
#                     "project_id": 105,
#                     "project_name": "Product Launch",
#                     "status": "Completed"
#                 },
#                 {
#                     "project_id": 106,
#                     "project_name": "Market Research",
#                     "status": "In Progress"
#                 }
#             ]
#         },
#         {
#             "id": 4,
#             "name": "David Brown",
#             "age": 37,
#             "position": "UX Designer",
#             "salary": 85000,
#             "projects": [
#                 {
#                     "project_id": 107,
#                     "project_name": "Website Redesign",
#                     "status": "Completed"
#                 },
#                 {
#                     "project_id": 108,
#                     "project_name": "Mobile App UI",
#                     "status": "In Progress"
#                 }
#             ]
#         },
#         {
#             "id": 5,
#             "name": "Eva Green",
#             "age": 26,
#             "position": "QA Engineer",
#             "salary": 70000,
#             "projects": [
#                 {
#                     "project_id": 109,
#                     "project_name": "Automated Testing",
#                     "status": "Completed"
#                 },
#                 {
#                     "project_id": 110,
#                     "project_name": "Performance Testing",
#                     "status": "In Progress"
#                 }
#             ]
#         }
#     ],
#     "departments": [
#         {
#             "department_id": 1,
#             "department_name": "Engineering",
#             "manager": "Alice Johnson",
#             "employees": [1, 2]
#         },
#         {
#             "department_id": 2,
#             "department_name": "Product",
#             "manager": "Carol White",
#             "employees": [3]
#         },
#         {
#             "department_id": 3,
#             "department_name": "Design",
#             "manager": "David Brown",
#             "employees": [4]
#         },
#         {
#             "department_id": 4,
#             "department_name": "Quality Assurance",
#             "manager": "Eva Green",
#             "employees": [5]
#         }
#     ],
#     "financials": {
#         "fiscal_year": 2023,
#         "revenue": 1500000,
#         "expenses": 850000,
#         "profit": 650000,
#         "assets": {
#             "cash": 300000,
#             "accounts_receivable": 200000,
#             "inventory": 150000,
#             "property_plant_equipment": 500000,
#             "intangible_assets": 350000
#         },
#         "liabilities": {
#             "accounts_payable": 100000,
#             "short_term_debt": 50000,
#             "long_term_debt": 200000,
#             "other_liabilities": 100000
#         },
#         "equity": {
#             "common_stock": 100000,
#             "retained_earnings": 450000
#         }
#     },
#     "board_of_directors": [
#         {
#             "id": 1,
#             "name": "Frank Thompson",
#             "age": 65,
#             "position": "Chairman"
#         },
#         {
#             "id": 2,
#             "name": "Grace Lee",
#             "age": 58,
#             "position": "Director"
#         },
#         {
#             "id": 3,
#             "name": "Henry Kim",
#             "age": 50,
#             "position": "Director"
#         }
#     ],
#     "company_policies": {
#         "vacation_days": 20,
#         "sick_leave": 10,
#         "remote_work": "true",
#         "health_benefits": "true",
#         "retirement_plan": "true"
#     }
# }

# json_data = json.dumps(data, indent=4)

# connect_to_tcp_server(host='localhost', port=8899, message=json_data)


import socket
import json
import struct

def connect_to_tcp_server(host='localhost', port=8899):
    # 创建一个复杂的结构化 JSON 数据
    data = {
        "method": "set",
        "lamp": {
            "id": 2,
            "action": 1,
            "mtime": 20
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



