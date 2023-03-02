#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author h3st4k3r
# Version Mark.5

'''
---------------------
Librerias necesarias:
---------------------
html5lib
bs4
urlopen
---------------------
'''

'''
Esto es un crawler para Mastodon, metemos el usuario, lee los nuevos post y manda correo.
Se pueden monitorizar los usuarios que se quiera. Aconsejo seguir los comentarios a lo largo del mismo.
'''

# Imports

from urllib.request import urlopen
#from urllib2 import urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import sys
import re
import smtplib

class Mastodon():

    def __init__(self):
        # Objects
        print("INIT MASTON")

    def enviar_notificacion(self,message, user):
        msg = MIMEMultipart()
        # CHANGE THE VALUES
        password = "EMAIL PASSWD"
        msg['From'] = "EMAIL FROM"
        msg['To'] = "RECEIVER"
        msg['Subject'] = "[ALERT][Alerta Monitorizacion Mastodon]["+user+"]"
        print("SEND MAIL")
        print("\n------\n")
        print(message)
        print("\n------\n")
        try:
            # 
            msg.attach(MIMEText(message, 'plain'))
            # create server
            server = smtplib.SMTP('')
            server.starttls()
            # Login Credentials
            server.login(msg['From'], password)
            # SEND MAIL
            server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
            server.quit()
            print ("Envio correcto del correo a: " + msg['To'])
        except Exception as e:
            print("\nNo se pudo conectar con el servidor de correo\n")
            print(e)

    def crawler(
        self,
        user):

        print("Abriendo la url... https://mastodon.social/@"+str(user))
        html = urlopen("https://mastodon.social/@"+str(user))
        res = BeautifulSoup(html.read(),"html5lib");
        contenido = res.findAll("div", {"class": "status__content emojify"})
        esta_pineada = res.findAll("div", {"class": "status__prepend"})
        #foto = res.find("a", {"class": "media-gallery__item-thumbnail"})
        #foto = res.find("img")
        content = ""
        sum = 0

        # IF THE POST ITS PINED DOESNT REPEAT THE SEND
        fi = open("pined.txt", "r")
        cuantas_pined = fi.read()
        fi.close()

        for tag in esta_pineada:
            if str(tag.getText()).replace("\n","")=="Pinned toot":
                print("pineada")
                content += ''
                sum += 1
                print(cuantas_pined)
                if cuantas_pined != '' and sum > int(cuantas_pined):
                    print("Se ha pineado una nueva entrada")
                    # SAVE FOR THE FUTURE
                    fic = open("pined.txt", "w+")
                    fic.write(str(sum).replace("\n",""))
                    fic.close()
                    msg = "Nuevo pineado para "+user+".\nPara comprobarlo: https://mastodon.social/@"+user+"\n\nSaludos ;)\n"

                    self.enviar_notificacion(msg, user)
                    sys.exit()
                else:
                    print
            else:
                content += tag.getText()

        stripped = re.sub('', '', content)
        print(stripped)
        print(str(sum) + " -- num fijados \n")
        count =  0
        cont = 0
        content2 = ""
        for tag in contenido:
            if count < sum:
                print("_ _ excepción 1 _ _ :( esta pineada _ _")
                count += 1
                cont += 1
            else:
                if cont < (sum + 1):
                    cont += 1
                    content2 += tag.getText()
                else:
                    print("\n__\n")
                    break

        stripped = re.sub('', '', content2)
        print(stripped)

        file = open(user+".txt", "r")
        texto = file.read()
        file.close()

        #stripped_aux=stripped.encode('utf-8', errors='ignore')

        if texto != stripped:
            f = open(user+".txt", "w+")
            f.write(str(stripped))
            f.close()

            msg = "Nuevo post para "+str(user)+".\nPara comprobarlo: https://mastodon.social/@"+str(user)+"\n\nContenido de la publicación: "+str(stripped)+"\n"
            msg+="\n\n"
            msg+="\n\nSaludos ;)\n\n"
            self.enviar_notificacion(msg, user)
        else:
            print("\n__\n")
            print("son iguales, no hago nada, saludos :)")
            #enviar_notificacion("Se ha ejecutado el script perfectamente, pero no hay nada nuevo. Un saludo ;)",user)


    def run(self):
        # CHANGE THE VALUE
        usuario = "USER TO MONITOR"
        self.crawler(usuario)



if __name__ == '__main__':
    pass

