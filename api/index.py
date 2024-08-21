from flask import Flask, request, Response, abort
import requests

app = Flask(__name__)

# Domain lengkap yang diizinkan untuk di-proxy
ALLOWED_DOMAIN = 'https://etslive-v3-vidio-com-tokenized.akamaized.net'

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/ternate')
def ternate():
    return 'ternate'

@app.route('/proxy/<path:subpath>')
def proxy(subpath):
    # Membuat URL target menggunakan ALLOWED_DOMAIN
    target_url = f'{ALLOWED_DOMAIN}/{subpath}'
    
    # Mendapatkan parameter query dari URL asli
    query_params = request.query_string.decode('utf-8')
    
    if query_params:
        target_url = f'{target_url}?{query_params}'
    
    # Header yang digunakan dalam permintaan
    headers = {
        'authority': 'etslive-v3-vidio-com-tokenized.akamaized.net',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://shaka-player-demo.appspot.com',
        'pragma': 'no-cache',
        'referer': 'https://shaka-player-demo.appspot.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    
    # Melakukan permintaan GET ke URL target
    resp = requests.get(target_url, headers=headers)
    
    # Mengembalikan respons dari URL target dengan header CORS
    return Response(
        resp.content,
        status=resp.status_code,
        content_type=resp.headers.get('Content-Type'),
        headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
    )

if __name__ == '__main__':
    app.run(debug=True, port=3000)
