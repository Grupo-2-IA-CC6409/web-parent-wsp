
import io
from django import template
import requests
import qrcode
from base64 import b64encode
register = template.Library()

@register.simple_tag(name='get_qr')
def get_qr():
    
    qrCode = requests.get("http://localhost:3000/get-qr")
    img = qrcode.make(qrCode.json()['qr'])
    image_io = io.BytesIO()
    img.save(image_io, 'PNG')
    dataurl = 'data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii')
    return dataurl
