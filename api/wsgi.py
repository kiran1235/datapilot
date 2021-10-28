from dotenv import load_dotenv
# take environment variables from .env.
load_dotenv()


from server import app

if __name__ == "__main__":
    app.run()