Real Time Bidder Service Demo
========


Install
------------
1. Clone repository from https://github.com/EPapadopoulou/real_time_bidder_service.git
2. create an .env file in the project directory and add the following entries: 
  - SECRET_KEY = 'TXyXrxiIjΙ' #This should be changed to another random string
  - SESSION_COOKIE_NAME = 'auction_cookie'
  - LOG_FILE = 'auction.log'
  - PROD_CAMPAIGNS_URI = "http://localhost:5000/campaigns/get" (change accordingly)
  - DEV_CAMPAIGNS_URI = "http://localhost:5000/campaigns/get" (change accordingly)

3. create a virtualenv and activate it:
on windows: 
```
$ py -3 -m venv venv
$ venv\Scripts\activate
```
on linux:
```
$ python3 -m venv venv
$ . venv/bin/activate
```

install bidder
```
$ pip install -e .
```
In case there are still packages missing install the following :

```
$ pip install flask, flask-restful, requests
```

Run
------

```
$ venv\Scripts\python.exe -m flask run
```

Tests
-------
There are 4 test cases defined for the Bidder Service.
In the project directory run
```
$ pytest
```

Remote Deployment
------

The bidder service has been deployed on an IIS server using wsgi. 
The bidder exposes 2 REST API endpoints:
- the Campaigns API https://test.elisys.gr/campaigns/get 
  -   using GET method, it can be called from the browser
- the BidderService API https://test.elisys.gr//bid_service/request_for_bid 
  -   using POST, content_type='application/json'
  -   and supplying the data: 
```
{"bid_id":1, 
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
```
