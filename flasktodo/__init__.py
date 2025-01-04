
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '.env'
)

load_dotenv(dotenv_path=dotenv_path, verbose=True)

from flask import Flask, render_template

from flask_migrate import Migrate

migrate = Migrate()

def handle_401(e):
    return render_template('error/401.html'), 401

def handle_404(e):
    return render_template('error/404.html'), 404

def handle_500(e):
    return render_template('error/500.html'), 500

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_error_handler(401, handle_401)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)
    
    from flasktodo import todo
    
    app.register_blueprint(todo.bp)
    
    import requests
    
    @app.context_processor
    def instance_id():
        instance_id = ''
        try:
            response = requests.get('http://169.254.169.254/latest/meta-data/instance-id/', timeout=3)
            instance_id = response.content.decode('utf-8')
        except:
            pass
        return dict(instance_id=instance_id)
    
    return app
