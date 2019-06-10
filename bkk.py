import requests, json, os
from datetime import datetime

def example():
    result = call("")
    return json.loads(result)["data"]

def call(url):
    result = requests.get(url)
    return(result.content.decode("utf-8"))

def search(query, includerefs="false"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/search.json?key=apaiary-test&version=3&appVersion=apiary-1.0&includeReferences="+includerefs+"&query="+str(query))
    return json.loads(result)["data"]

def stopsForLocation(lon, lat, query="", radius="100", lonspan="", latspan="", includerefs="false"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/stops-for-location.json?key=apaiary-test&version=3&appVersion=apiary-1.0&includeReferences="+includerefs+"&lon="+str(lon)+"&lat="+str(lat)+"&lonSpan="+lonspan+"&latSpan="+latspan+"&radius="+radius+"&query="+query)
    return json.loads(result)["data"]

def arrivalsAndDeparturesForStop(stopId, limit="20", onlyDepartures="false", minutesBefore="2", minutesAfter="30"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/arrivals-and-departures-for-stop.json?key=key&version=version&appVersion=appVersion&includeReferences=false&stopId="+stopId+"&onlyDepartures="+onlyDepartures+"&limit="+limit+"&minutesBefore="+minutesBefore+"&minutesAfter="+minutesAfter)
    return json.loads(result)["data"]

def scheduleForStop(stopId, onlyDepartures="true", date="20190606"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/schedule-for-stop.json?key=apaiary-test&version=3&appVersion=apiary-1.0&includeReferences=false&stopId="+stopId+"&onlyDepartures="+onlyDepartures+"&date="+date)
    return json.loads(result)["data"]

def routeDetails(routeId, related="false"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/route-details.json?key=apaiary-test&version=3&appVersion=apiary-1.0&includeReferences=true&routeId="+routeId+"&related="+related)
    return json.loads(result)["data"]

def tripDetails(vehicleId="", tripId="", date="20190609"):
    result = call("http://futar.bkk.hu/bkk-utvonaltervezo-api/ws/otp/api/where/trip-details.json?key=apaiary-test&version=3&appVersion=apiary-1.0&includeReferences=true&tripId="+tripId+"&date="+date)
    return json.loads(result)["data"]

# stops = search("Raktár utca")["entry"]["stopIds"]
# for i in stops:
#     if arrivalsAndDeparturesForStop(i)["entry"]["stopTimes"] != []:
#         try:
#             for i in arrivalsAndDeparturesForStop(i)["entry"]["stopTimes"]:
#                 #print(i["stopHeadsign"], datetime.fromtimestamp(i["arrivalTime"]).strftime("%H:%m"))
#                 print(i, end="\n\n")
#         except:
#             print(end="")


megallok = search("Raktár utca")["entry"]["stopIds"]
megallo_data = []
for megallo in megallok:
    megallo_data.append(arrivalsAndDeparturesForStop(megallo, limit="10")["entry"]["stopTimes"])

jaratok = []
megallo_data = [e for e in megallo_data if e]
for megallo in megallo_data:
    for jarat in megallo:
        jaratok.append(jarat["tripId"])

print(tripDetails(tripId=jaratok[0])["entry"])
print(jaratok[0])
    