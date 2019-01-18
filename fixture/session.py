import certifi


class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self):
        wd = self.app.wd
        from urllib.request import Request, urlopen
        req = Request('https://ga-s3-new.russian-lotteries.net/')
        with urlopen(req, cafile=certifi.where()) as response:
            print(response.read())
