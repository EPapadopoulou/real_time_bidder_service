from bidder_application import init_app
import logging
app = init_app(configuration='config.ProdConfig')

if __name__ == "__main__":
    logging.log("Application starting")
    app.run(host='0.0.0.0')