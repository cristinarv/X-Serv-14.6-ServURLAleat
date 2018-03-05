#!/usr/bin/python3
# Cristina del Río Vergel
import webapp
import random
class UrlsAleats(Wa.webApp) :
    def process(self, parsedRequest):
        UrlsAleats = str(Ra.randint(0 , 10000000000 ))
        return("200 OK", "<html><body><h1>Hola:</h1>" +
                "<p><a href= " + UrlsAleats +
                ">Dame otra</a></p></body></html>")
if __name__ == '__main__':
    my_webapp = UrlsAleats("localhost", 1234)
