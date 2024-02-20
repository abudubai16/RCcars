from RCcars import create_app, socketio
from RCcars.utils import create_db


app = create_app()

if __name__ == '__main__':
    try:
        create_db(app)
        app.run(debug=True)
        socketio.run(app)
    except ImportError:
        print("Check the text document regarding the libraries that need to be installed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Server closed successfully")
