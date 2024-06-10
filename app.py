from flask import Flask, request, render_template, send_file, jsonify
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    phone_number = data['phone_number']
    img_io = generate_call_qr(phone_number)
    return send_file(img_io, mimetype='image/png')

def generate_call_qr(phone_number):
    """
    Generate a QR code for a phone number to initiate a direct call.

    :param phone_number: The phone number to encode in the QR code.
    :return: A BytesIO object containing the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr_data = f'tel:{phone_number}'
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

if __name__ == '__main__':
    app.run(debug=True)

#*182*1*1*0788477727*3000#
