from .models import Campaign, GeoLocation

__campaigns = (Campaign(campaign_id=1, campaign_name='Campaign Greece - Cyprus', price=10.2, ad_creative="",
                        target_geolocations=[
                            GeoLocation(country="Greece", latitude=37.983810, longitude=23.727539),
                            GeoLocation(country="Greece", latitude=40.640064, longitude=22.944420),
                            GeoLocation(country="Greece", latitude=38.246208, longitude=21.735069),
                            GeoLocation(country="Cyprus", latitude=34.7820568, longitude=32.4054525)
                        ]),
               Campaign(campaign_id=2, campaign_name='Campaign Greece - Cyprus - Bulgaria', price=6, ad_creative="",
                        target_geolocations=[
                            GeoLocation(country="Greece", latitude=37.983810, longitude=23.727539),
                            GeoLocation(country="Greece", latitude=40.640064, longitude=22.944420),
                            GeoLocation(country="Greece", latitude=38.246208, longitude=21.735069),
                            GeoLocation(country="Cyprus", latitude=34.7820568, longitude=32.4054525),
                            GeoLocation(country="Bulgaria", latitude=42.6954108, longitude=23.2539074),
                            GeoLocation(country="Bulgaria", latitude=41.8356993, longitude=23.4781605)
                        ]),
               Campaign(campaign_id=3, campaign_name='Campaign Greece only', price=7, ad_creative="",
                        target_geolocations=[
                            GeoLocation(country="Greece", latitude=37.983810, longitude=23.727539),
                            GeoLocation(country="Greece", latitude=40.640064, longitude=22.944420),
                            GeoLocation(country="Greece", latitude=38.246208, longitude=21.735069),
                            GeoLocation(country="Greece", latitude=39.6310074, longitude=22.4066366),
                            GeoLocation(country="Greece", latitude=40.9368864, longitude=24.3900626),
                            GeoLocation(country="Greece", latitude=40.8491341, longitude=25.8578008),
                            GeoLocation(country="Greece", latitude=37.0350616, longitude=22.1045358)
                        ]),
               Campaign(campaign_id=4, campaign_name='Campaign Greece - Italy', price=11, ad_creative="",
                        target_geolocations=[
                            GeoLocation(country="Greece", latitude=37.983810, longitude=23.727539),
                            GeoLocation(country="Greece", latitude=40.640064, longitude=22.944420),
                            GeoLocation(country="Greece", latitude=38.246208, longitude=21.735069),
                            GeoLocation(country="Cyprus", latitude=34.7820568, longitude=32.4054525),
                            GeoLocation(country="Italy", latitude=40.853586, longitude=14.1729676),
                            GeoLocation(country="Italy", latitude=43.8454165, longitude=10.9518666),
                            GeoLocation(country="Italy", latitude=38.1405228, longitude=13.2872492)
                        ]),
               Campaign(campaign_id=5, campaign_name="Campaign Cyprus - Italy - Bulgaria", price=3, ad_creative="",
                        target_geolocations=[
                            GeoLocation(country="Cyprus", latitude=34.7820568, longitude=32.4054525),
                            GeoLocation(country="Italy", latitude=40.853586, longitude=14.1729676),
                            GeoLocation(country="Italy", latitude=43.8454165, longitude=10.9518666),
                            GeoLocation(country="Italy", latitude=38.1405228, longitude=13.2872492),
                            GeoLocation(country="Bulgaria", latitude=42.6954108, longitude=23.2539074),
                            GeoLocation(country="Bulgaria", latitude=41.8356993, longitude=23.4781605)
                        ]))


def get_campaigns():

    return __campaigns
