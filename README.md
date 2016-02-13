# Pretio-Interview - James Stephaniuk

The high-level goal of this mini-project to make a simple server-side integration with the Pretio API that avoids issues with cross-domain restrictions, and automatically detects the country of the user.

Criteria:

Responds to the endpoint /ad
Translates the client's IP address into a two-letter country code
Makes an HTTP request to the Pretio API and parses the result
returns HTML, with the creative URL from the ad response templated in as the src attribute for a fullscreen iframe.
You can setup the project however you like and use whatever dependencies you see fit.

Deployed with Heroku at [https://limitless-caverns-16525.herokuapp.com/](https://limitless-caverns-16525.herokuapp.com/)
