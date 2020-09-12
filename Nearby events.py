import requests

gps_country = "US"  # gps data from Radar
country_code = "US"  # user input


def find_local_events(country_code,
                      api_key="7dgWAfMB16HWpBbGBSCXGHLqA71lNWsn",
                      base_url="https://app.ticketmaster.com/discovery/v2/events.json?"):
    global local_events

    request_url = base_url + "countryCode=" + country_code + "&apikey=" + api_key
    response = requests.get(request_url)
    local_events = response.json()["_embedded"]["events"]

    events_list = []
    for i in range(len(local_events)):
        event_data = "{}: {}".format(local_events[i]["name"], local_events[i]["dates"]["start"]["localDate"])
        events_list.append(event_data)
    return events_list


def get_event_details():
    for events in local_events:

        url = events["url"]
        date = events["dates"]["start"]["localDate"]
        genre = events["classifications"][0]["genre"]["name"]
        subgenre = events["classifications"][0]["subGenre"]["name"]

        try:
            time = events["dates"]["start"]["localTime"]
        except KeyError:
            time = ""
        try:
            min_price = events["priceRanges"][0]["min"]
        except KeyError:
            min_price = ""
        try:
            max_price = events["priceRanges"][0]["max"]
        except KeyError:
            max_price = ""
        try:
            currency = events["priceRanges"][0]["currency"]
        except KeyError:
            currency = ""

        print(events["name"])
        print(url)
        print(date + " " + time)
        print(genre + ", " + subgenre)
        print(str(min_price) + " - " + str(max_price) + " " + currency)
        print()


if __name__ == "__main__":

    try:
        country_code
    except NameError:
        country_code = None

    if country_code is None:
        country_code = gps_country

    find_local_events(country_code)
    get_event_details()
