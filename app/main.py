from flask import Flask
from views import views


def main():
    print("Hello from fe4-helper!")
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.run(debug=True, port=5050, host="0.0.0.0")


if __name__ == "__main__":
    main()
