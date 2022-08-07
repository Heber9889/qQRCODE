#import a bibliotteca pyqrcode
#import a biblioteca pypng

import pyqrcode
import png

code = input("#_APENAS_URL_AKI_# : ")

qr = pyqrcode.create(code)

qr.png("codigoQR.png", scale=6)


if qr !=0:
    print ("#Arquivo_Salvo_Com_Sucesso_#")


