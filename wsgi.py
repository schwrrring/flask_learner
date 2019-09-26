from application import create_app
import os

environment=os.environ['CONFIG']

app = create_app(environment)
if __name__ == "__main__":
    app.run(host='0.0.0.0')