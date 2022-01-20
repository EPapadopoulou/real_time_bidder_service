import logging
from config import DevConfig
from flask import Flask, Blueprint


logging.basicConfig(filename=DevConfig.LOG_FILE, filemode='w', format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger()
config = None


def init_app(configuration='config.DevConfig'):
    """Initialize the core bidder_application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(configuration)
    global config
    config = app.config
    global logger
    logger = logging.getLogger()

    with app.app_context():
        # Include  Routes
        from .campaign import campaign
        from .bidder import bidder
        # Register Blueprints

        app.register_blueprint(campaign.campaign_api_bp)
        app.register_blueprint(bidder.bidder_api_bp)
        logger.info("init_app() finished execution")
        return app
