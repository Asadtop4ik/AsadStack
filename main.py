from Asad_Stack.app import AsadStackApp
from Asad_Stack.middleware import Middleware
app = AsadStackApp()


@app.route("/home", allowed_methods=["get"])
def home(request, response):
    response.text = "That is home page"


@app.route("/about", allowed_methods=["put"])
def about(request, response):
    response.text = "That is about page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello {name}"


@app.route("/books")
class Books:
    def get(self, request, response):
        response.text = "That is books page"

    def post(self, request, response):
        response.text = "That is books post page"


def new_handler(request, response):
    response.text = "That is new handler"


app.add_route("/new", new_handler)

@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "home.html",
        context={"new_title": "Best Title", "new_body": "Best Body Asadbek"}
    )

@app.route("/json")
def json_handler(req, resp):
    response_data = {"name": "Asadbek", "type": "json"}
    resp.json = response_data


def on_exception(req, resp, exc):
    resp.text = str(exc)


app.add_exception_handler(on_exception)


@app.route("/exception")
def exception_throwing_handler(req, resp):
    raise Exception("This is an exception")


class LoggingMiddleware(Middleware):
    def process_request(self, req):
        print("request is being called")

    def process_response(self, req, resp):
        print("response has been generated")


app.add_middleware(LoggingMiddleware)

