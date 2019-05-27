from settings import http

if __name__ == '__main__':
    app = http.createApp()
    app.run(debug = True)