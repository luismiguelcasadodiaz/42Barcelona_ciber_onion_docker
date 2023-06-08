import qrcode
from qrcode.image.pure import PyPNGImage
import subprocess
import PySimpleGUI as sg
from PIL import Image, ImageTk
import os


QR_SIZE = (300, 300)

services = [ 'hidden_service_bonus',  'hidden_service_static']


for service in services:
    service_path = '/var/lib/tor/' + service + '/hostname'
    cmd = ['docker', 'exec', 'dark', 'cat', service_path]

    cmd_return = subprocess.run(cmd, stdout= subprocess.PIPE)
    onion_addr = cmd_return.stdout.strip().decode()
    img = qrcode.make(onion_addr,image_factory=PyPNGImage)
    img.save(service + '.png')
    cwd = os.getcwd()
    imagepath = os.path.join(cwd, service + '.png')

    layout =[
        [sg.Image(key='-QRCODE-',source=imagepath)]
    ]
    window = sg.Window(title=service,
                        layout=[layout], margins=(15, 15))
    
    
    
    while True:
        event, values = window.read()    
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break



    
