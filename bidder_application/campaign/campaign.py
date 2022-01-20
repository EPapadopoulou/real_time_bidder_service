from flask_restful import Api, Resource
from flask import Blueprint
from bidder_application import db_api
import json

# Define the Flask Blueprint
campaign_api_bp = Blueprint('campaigns_api', __name__)

# Add the Blueprint to the Flask-restful Api
api = Api(campaign_api_bp)


class GetAllCampaigns(Resource):
    """ Define a Restful resource for the Campaign API."""
    def get(self):
        """ This endpoint will only support GET requests. """

        # retrieve campaigns from the campaign pool
        rows = db_api.get_campaigns()

        return {'campaigns': [i.get_json() for i in rows]}


# Add a resource to the flask-restful api
api.add_resource(GetAllCampaigns, '/campaigns/get')
