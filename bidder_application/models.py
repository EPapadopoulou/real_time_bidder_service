import json

from json import JSONEncoder, JSONDecoder


class ComplexEncoder(JSONEncoder):
    """ Custom JSONEncoder to convert custom python objects
     into JSON format. This is required because I am using
     nested objects (jsonpickle doesn't work with custom nested types
     as well as JSON that has not been converted using jsonpickle.encode()"""
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


class ComplexDecoder(JSONDecoder):
    """ Custom JSONDecoder to convert data in JSON format into
        specific python objects. """
    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):

        #  Campaign object
        if "campaign_id" in dct and "campaign_name" in dct \
                and "price" in dct and "ad_creative" in dct and "target_geolocations" in dct:
            campaign = Campaign(campaign_id=dct['campaign_id'], campaign_name=dct['campaign_name'],
                                price=dct['price'], ad_creative=dct['ad_creative'],
                                target_geolocations=self.__get_geolocations(dct['target_geolocations']))
            return campaign

        # BidRequest object
        if "bid_id" in dct and "mobile_app_info" in dct and "device_info" in dct:
            bid_request = BidRequest(bid_id=dct['bid_id'],
                                     mobile_app_info=MobileAppInfo(app_id=dct['mobile_app_info']['app_id'],
                                                                   app_name=dct['mobile_app_info']['app_name']),
                                     device_info=DeviceInfo(device_id=dct['device_info']['device_id'],
                                                            device_os=dct['device_info']['device_os'],
                                                            geolocation=self.__get_geolocation(
                                                                dct['device_info']['geolocation'])))
            return bid_request
        # BidResponse object
        if "bid_id" in dct and "campaign_id" in dct and "price" in dct and "ad_creative" in dct:
            bid_response = BidResponse(bid_id=dct['bid_id'],
                                       campaign_id=dct['campaign_id'],
                                       price=dct['price'],
                                       ad_creative=dct['ad_creative'])
            return bid_response

        if "bid_id" in dct:
            return EmptyBidResponse(bid_id=dct['bid_id'])

        return dct

    def __get_geolocation(self, dct):
        if "latitude" in dct and "longitude" in dct and "country" in dct and "distance" in dct:
            return GeoLocation(latitude=dct["latitude"], longitude=dct['longitude'],
                               country=dct['country'], distance=dct['distance'])
        elif "latitude" in dct and "longitude" in dct and "country" in dct:
            return GeoLocation(latitude=dct["latitude"], longitude=dct['longitude'],
                               country=dct['country'])

    def __get_geolocations(self, dct_list):
        r_list = []
        for g_dct in dct_list:
            r_list.append(self.__get_geolocation(g_dct))
        return r_list


class JsonSerializable:
    """ Class that is inherited by all model classes to call get_json() method
        with the specific ComplexEncoder."""
    def get_json(self):
        return json.dumps(self, cls=ComplexEncoder)


class GeoLocation(JsonSerializable):
    def __init__(self, country, latitude, longitude, distance=50.0):
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.distance = distance

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(latitude=self.latitude, country=self.country, longitude=self.longitude, distance=self.distance)


class DeviceInfo(JsonSerializable):
    def __init__(self, device_id, device_os, geolocation):
        self.device_id = device_id
        self.device_os = device_os
        self.geolocation = geolocation

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(geolocation=self.geolocation, device_id=self.device_id, device_os=self.device_os)


class MobileAppInfo(JsonSerializable):
    def __init__(self, app_id, app_name):
        self.app_id = app_id
        self.app_name = app_name

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(app_id=self.app_id, app_name=self.app_name)


class BidRequest(JsonSerializable):
    def __init__(self, bid_id, mobile_app_info, device_info):
        self.bid_id = bid_id
        self.mobile_app_info = mobile_app_info
        self.device_info = device_info

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(bid_id=self.bid_id, mobile_app_info=self.mobile_app_info, device_info=self.device_info)


class BidResponse(JsonSerializable):
    def __init__(self, bid_id, campaign_id, price, ad_creative):
        self.bid_id = bid_id
        self.campaign_id = campaign_id
        self.price = price
        self.ad_creative = ad_creative

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(bid_id=self.bid_id, campaign_id=self.campaign_id, price=self.price, ad_creative=self.ad_creative)


class EmptyBidResponse(JsonSerializable):
    def __init__(self, bid_id):
        self.bid_id = bid_id

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(bid_id=self.bid_id)


class Campaign(JsonSerializable):

    def __init__(self, campaign_id, campaign_name, price, ad_creative, target_geolocations):
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.price = price
        self.ad_creative = ad_creative
        self.target_geolocations = target_geolocations

    """ method that is used by the ComplexEncoder """
    def reprJSON(self):
        return dict(campaign_id=self.campaign_id, campaign_name=self.campaign_name,
                    price=self.price, ad_creative=self.ad_creative, target_geolocations=self.target_geolocations)



def get_object_from_json(json_data):
    return json.loads(json_data, cls=ComplexDecoder)
