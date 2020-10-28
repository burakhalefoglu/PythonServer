import socket
#from flask import Flask, render_template

host = "104.197.76.207"
port = 6060

#app = Flask(__name__)


#if __name__ == "__main__":
##    app.run()
    

#@app.route("/")
#def index():
#  return render_template("index.html")




try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host,port))
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)
    print("socket dinleniyor")

except socket.error as msg:
    print("Hata:", msg)

while True:

   # Client ile bağlantı kurulursa
   c, addr = s.accept()
   print('Gelen bağlantı:', addr)

   # Bağlanan client tarafına hoşgeldin mesajı gönderelim.
   mesaj = "0"
   c.send(mesaj.encode('utf-8'))

   data = c.recv(1024)
   print(data.decode("utf-8"))

   # Bağlantıyı sonlandıralım
   c.close()


   
