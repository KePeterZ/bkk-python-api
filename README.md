# bkk-python-api

Python bindings for the official BKK Futár API.


# Prerequisites

The following modules are required: requests, json, os, and datetime. They should be installed on most machines, if they are not howewer, you can install them like this:

```
pip install -r requirements.txt
```

# Functions

Search for a vehicle, or station.
```
search(query, includerefs="false")
```

Get stops for location, or query.
```
stopsForLocation(lon, lat, query="", radius="100", lonspan="", latspan="", includerefs="false")
```

Get arrivals and departures for stop.
```
arrivalsAndDeparturesForStop(stopId, limit="20", onlyDepartures="false", minutesBefore="2", minutesAfter="30")
```

Get real-time schedules for stop, by stopId.
```
scheduleForStop(stopId, onlyDepartures="true", date="20190606")
```

Get the details for a specified route, by routeId.
```
routeDetails(routeId, related="false")
```

Get the details of a specified trip, using a tripId.
```
tripDetails(vehicleId="", tripId="", date="20190609")
```

# Variables

Specified variables in the functions:
* **lat, long**: Latitudes and Longitudes (can be looked up on Google Maps.)
* **routeId**: The ID of a specific route. Example: BKK_3040 for Tram 4.
* **tripId**: The ID of a specific trip.
* **query**: Input, like Széll Kálmán Tér. Potentially from a user.
* **limit**: Limits output vehicles or stops to a specified value.
* **radius**: Specified radius, used for searching for vehicles or stops.

# Official API

All of the data above are gathered from the official [BKK API](https://bkkfutar.docs.apiary.io/).

# Contributing

If you built a custom function, or rebuilt one from scratch, please make a pull request.

## KePeterZ, 2019.