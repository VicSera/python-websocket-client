import websocket

ws_url = "wss://node-messaging-server.onrender.com"

def on_message(app, message):
    print(message)

if __name__ == '__main__':
    app = websocket.WebSocketApp(ws_url, on_message=on_message)
    app.run_forever()