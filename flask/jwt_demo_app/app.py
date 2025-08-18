from flask import Flask
from extensions import db
from config import Config
from auth.routes import auth_bp
from market.routes import market_bp

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    #Blueprints will be registered later

    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(market_bp,url_prefix='/market')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
