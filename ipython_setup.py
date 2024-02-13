# ipython_setup.py to get access to database with context and models from 'models.py'

from app import create_app

app = create_app()
app.app_context().push()

def get_app():
    return app