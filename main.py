import hashlib
import os
import flask
from flask import request, render_template_string

app = flask.Flask(__name__)

# 硬编码的敏感信息（敏感信息泄露）
API_KEY = "12345-ABCDE"  # 这种硬编码的敏感信息在生产环境中非常危险

# 文件路径遍历漏洞
def read_file(filename):
    base_dir = "/var/www/uploads/"
    # 直接将用户输入作为文件路径的一部分，可能导致路径遍历攻击
    with open(base_dir + filename, 'r') as file:
        return file.read()

# 不安全的密码哈希（使用 MD5 进行哈希）
def hash_password(password):
    # 使用不安全的 MD5 哈希算法，容易被破解
    return hashlib.md5(password.encode()).hexdigest()

# Flask 应用中的 XSS 漏洞
@app.route("/greet", methods=["GET"])
def greet_user():
    user = request.args.get("name")
    # 直接将用户输入嵌入到 HTML 响应中，存在 XSS 风险
    template = "<h1>Hello, {}!</h1>".format(user)
    return render_template_string(template)

# 主函数
if __name__ == "__main__":
    # 模拟文件路径遍历
    filename = input("Enter filename to read: ")
    print(read_file(filename))

    # 模拟密码哈希
    password = input("Enter a password to hash: ")
    print("Hashed password: ", hash_password(password))

    # 启动 Flask Web 应用程序
    app.run(debug=True)