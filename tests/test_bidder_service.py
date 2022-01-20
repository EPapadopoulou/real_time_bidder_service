import pytest
import json
from bidder_application import init_app
from bidder_application.models import BidRequest, GeoLocation, DeviceInfo, MobileAppInfo, BidResponse, EmptyBidResponse, get_object_from_json

from bidder_application.common import BID_REQUEST_ENDPOINT, CAMPAIGN_API_ENDPOINT

bidRequestNapoli = BidRequest(bid_id=1, mobile_app_info=MobileAppInfo(app_id=1234, app_name='Sudoku'),
                              device_info=DeviceInfo(device_id=9876,device_os= "android",
                                    geolocation = GeoLocation(latitude=40.7969655, longitude=14.192431,
                                                    country="Italy")))

bidRequestMunich = BidRequest(bid_id=2, mobile_app_info=MobileAppInfo(app_id=1234, app_name='Sudoku'),
                              device_info=DeviceInfo(device_id=9876,device_os= "android",
                                    geolocation = GeoLocation(latitude=48.1548894, longitude=11.4716247,
                                                    country="Germany")))


bidRequestPatras = BidRequest(bid_id=3, mobile_app_info=MobileAppInfo(app_id=1234, app_name='Sudoku'),
                              device_info=DeviceInfo(device_id=9876,device_os= "android",
                                    geolocation = GeoLocation(latitude=38.246639, longitude=21.734573,
                                                    country="Greece")))

bidRequestPisa = BidRequest(bid_id=4, mobile_app_info=MobileAppInfo(app_id=23408034, app_name='PastaMaker'),
                              device_info=DeviceInfo(device_id=2345345,device_os= "iOS",
                                    geolocation = GeoLocation(latitude=43.7067804, longitude=10.3778686,
                                                    country="Italy")))

bidRequestSofia = BidRequest(bid_id=5, mobile_app_info=MobileAppInfo(app_id=23408034, app_name='Fakebook'),
                              device_info=DeviceInfo(device_id=2345345,device_os= "iOS",
                                    geolocation = GeoLocation(latitude=42.7000077, longitude=23.1955312,
                                                    country="Bulgaria")))



malFormedBidRequest = {"bid_id1":1,
"mobile_app_info":
  {"app_id":"1234",
  	"app_name":"Sudoku"
  },
"device_info":
 {"device_id":"9876",
 	"device_os":"android",
 	"geolocation":
 	{"latitude":38.246639,
 		"longitude":21.734573,
 		"country":"Greece"
 	}
 }
}


@pytest.fixture
def client():
    app = init_app(configuration="config.DevConfig")

    with app.test_client() as client:
        yield client


def test_empty_bid_request(client):
    rv = client.post(BID_REQUEST_ENDPOINT)

    assert rv.status_code == 400


def test_wellformed_bid_request(client):
    rv = client.post(BID_REQUEST_ENDPOINT, data=bidRequestPatras.get_json(), content_type='application/json')

    bidResponse = get_object_from_json(json.loads(rv.data))

    assert type(bidResponse) == BidResponse \
           and bidResponse.bid_id == bidRequestPatras.bid_id \
           and bidResponse.price == 11 \
           and bidResponse.campaign_id == 4


def test_malformed_bid_request(client):
    rv = client.post(BID_REQUEST_ENDPOINT, data=json.dumps(malFormedBidRequest), content_type='application/json')

    assert rv.status_code == 400


def test_campaign_no_target(client):
    rv = client.post(BID_REQUEST_ENDPOINT, data=bidRequestMunich.get_json(), content_type="application/json")

    bidResponse = get_object_from_json(json.loads(rv.data))

    assert bidResponse.bid_id == bidRequestMunich.bid_id and type(bidResponse) == EmptyBidResponse
