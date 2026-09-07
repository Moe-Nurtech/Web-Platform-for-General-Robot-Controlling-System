import socket
import os
import io
import os.path
from motion import *

s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind(('0.0.0.0', port))



while True:
    s.listen(1)
    print("Waiting for a connection...")

    img_str =''
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(2)
        if not data:
            break
        if(data[0]==22):
            pololuSubLoop(data[1], 8)

    # blit


   # pygame.display.flip()
    print("Done.")
eye = Eye().start()
track = Track(eye, face_net, gender_net, age_net, object_net).start()

c.close()
s.close()

if __name__ == "__main__":
    Main()