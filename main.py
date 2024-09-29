import sqlite3
import os
import pickle

# 不安全的 SQL 查询（SQL 注入漏洞）
def get_user_data(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # 不安全的拼接 SQL 查询，可能会导致 SQL 注入
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()
    return result

# 不安全的命令执行（命令注入漏洞）
def run_command(cmd):
    # 使用 os.system 执行外部命令，存在命令注入的风险
    os.system(cmd)

# 不安全的反序列化（反序列化漏洞）
def unsafe_deserialization(serialized_data):
    # 直接反序列化未经过验证的数据，可能导致任意代码执行
    return pickle.loads(serialized_data)

# 主函数，用于测试漏洞代码
if __name__ == "__main__":
    # 模拟 SQL 注入
    user_id = input("Enter user ID: ")
    print(get_user_data(user_id))

    # 模拟命令注入
    cmd = input("Enter a shell command to run: ")
    run_command(cmd)

    # 模拟不安全的反序列化
    serialized_data = input("Enter serialized data: ")
    print(unsafe_deserialization(serialized_data))