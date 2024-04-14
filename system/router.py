class router:

    def __init__(self) -> None:
        pass

    def boot(self, request):
        pass

    def parse_request(self, reqest):
        pass

    def get_init_content(self):
        f = open('views/index.html')
        content = f.read()
        f.close()
        return content
