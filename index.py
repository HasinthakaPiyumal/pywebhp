import socket
import os

HOST = ''
print(int(os.environ.get("PORT", 5000)))
PORT = int(os.environ.get("PORT", 5000))

#Response Message Eka
response = """\
HTTP/1.1 200 OK

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""

print("Enter Url : 127.0.0.1:5000 in your browser \n\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
while True:

    conn, addr = s.accept()

    browser_request = conn.recv(2**10).decode('utf-8')  #Meken Wenne Browser Eken Ewana Message eka(HTTP Request Eka) Variable ekakata Aragena Decode Karagannawa
    print(browser_request)                              #Variable eka print karanawa
    print('Connected by', addr)                         #HTTP Request eka ewapu IP_address ekai Port ekai print karanwa
    
    conn.sendall(response.encode('utf-8'))                 #Response kiyana variable eke value eka aragena ENCODE karala Browser ekata yawanawa
    conn.close()

s.close()










# from flask import Flask
# app = Flask(__name__)




# @app.route('/')
# def index():
#     html = open('index.html','r').read()
#     return html

# if __name__ == "__main__":
#     app.run(debug=True)
