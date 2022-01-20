from bidder_application import common
from bidder_application.models import get_object_from_json, EmptyBidResponse, BidResponse
import requests

from bidder_application import logger, config



def filter_campaigns(bidRequest, campaigns):
    """ Bidder Service method to filter campaigns
     based on the target criteria (country and location coordinates) """
    filtered_campaigns = []

    # the target criteria
    bid_geolocation = bidRequest.device_info.geolocation

    # for each campaign in the campaign pool, it will check if the country in the bidRequest
    # is found in the list of countries that the campaign should run
    # If true, it will check if the coordinates in the bidRequest are within the specified
    # distance of the coordinates defined in the campaign geolocation data
    for campaign in campaigns:
        for target_geolocation in campaign.target_geolocations:
            # for each country and coordinates defined
            if target_geolocation.country == bid_geolocation.country:
                distance = common.haversine(
                    bid_geolocation.longitude, bid_geolocation.latitude,
                    target_geolocation.longitude, target_geolocation.latitude)
                if distance < target_geolocation.distance:
                    filtered_campaigns.append(campaign)
                    break  # breaks the inner loop only

    return filtered_campaigns


def find_campaign_with_highest_price(campaigns):
    """ method that receives a list of campaign objects
    and returns the one with the highest price. If the list
    of campaigns is empty, returns None. If more than one campaign
    have the same highest price, then it will
    return the first one on the list """
    highest_price = 0
    chosen_campaign = None
    for campaign in campaigns:
        if campaign.price > highest_price:
            chosen_campaign = campaign
            highest_price = campaign.price

    return chosen_campaign


def process_request_for_bid(bidRequest):
    """ Method that processes the received request for bids. """

    try:
        # First, the list of campaigns is retrieved from the Campaign API
        #  and converted from JSON to Campaign objects.

        bid_id = bidRequest.bid_id

        c_json = requests.get(config.get('CAMPAIGNS_API_URI')).json()

        campaign_list = c_json["campaigns"]

        campaigns = []
        for item in campaign_list:
            campaigns.append(get_object_from_json(item))


        # the list of campaigns is filtered against the geolocation criteria
        # defined in the BidRequest
        filtered_campaigns = filter_campaigns(bidRequest, campaigns)

        # if the method did not return a match, return an EmptyBidResponse object
        # otherwise, it will select the one with the highest price
        # and return a BidResponse object with the chosen campaign information

        if len(filtered_campaigns) == 0:
            return EmptyBidResponse(bid_id)
        else:
            campaign = find_campaign_with_highest_price(filtered_campaigns)
            return BidResponse(bid_id=bid_id,
                               campaign_id=campaign.campaign_id,
                               price=campaign.price,
                               ad_creative=campaign.ad_creative)

        # In the case of a malformed BidRequest, it will return a BadRequestResponse
        # that includes the bid_id if the bid_id information is not malformed itself.
    except AttributeError as ae:
        logger.error(ae, exc_info=True)
    except requests.exceptions.ConnectionError as ce:
        logger.error(ce, exc_info=True)
    except Exception as e:
        logger.error(e, exc_info=True)

    return None
