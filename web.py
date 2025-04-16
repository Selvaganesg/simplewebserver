from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<html>
    <body>
        <center>
        <img src="college.logo.png" style="width: 450px;">
        </center>
        <table border="1" align="center" cellpadding="5px" bgcolor="black">
            <caption>Protocol List</caption>
            <tr style="color: white;">
                <th>S.No</th><th>Layer</th><th>Protcols</th>
            </tr>
            <tr style="color: white;">
                <td>1</td><td>Application</td><td>HTTP, DNS, TELNET, SSH</td>
            </tr>
            <tr style="color: white;">
                <td>2</td><td>Transport Layer</td><td>TCP, UDP</td>
            </tr>
            <tr style="color: white;">
                <td>3</td><td>Internet Layer</td><td>IP, IMPC</td>
            </tr>
            <tr style="color: white;">
                <td>4</td><td>N/W Access Layer</td><td>Wi-Fi, MA</td>
            </tr>
        </table>
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8080)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
