import json

from flask import Blueprint, request, abort
from flask_restful import Api, Resource

from bidder_application.models import get_object_from_json
from .BidderService import process_request_for_bid

from bidder_application import logger
# Define the Flask Blueprint
bidder_api_bp = Blueprint('bidder_api', __name__)
# Add the Blueprint to the Flask-restful Api.
api = Api(bidder_api_bp)


class BidServiceEndpoint(Resource):
    """ Define a Restful resource for the Bidder Service. """
    def post(self):
        """ This endpoint will only support POST requests """

        # convert from JSON to bidder_application.models.BidRequest object

        # error checking
        if request.get_data() == b'':
            abort(400)
        try:
            bid_request = get_object_from_json(request.get_data())
            # process BidRequest and receive BidResponse
            response = process_request_for_bid(bid_request)
            if response is None:
                abort(500)

            #return BidResponse object as json
            return response.get_json()
        except Exception as e:
            logger.error(e, exc_info=True)
            abort(400)


# Add a resource to the flask-restful api
api.add_resource(BidServiceEndpoint, '/bid_service/request_for_bid')
