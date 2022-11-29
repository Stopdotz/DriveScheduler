import  requests
import json
import Constants as C

class DistanceAPI():
    def __init__(self):
        pass

    def apiCall ():
        response = requests.get(C.TIME_FILTER)
        print (response.text)
        return response.text

    def apiToJSON (this):
        jsonData = this.apiCall()
        print (jsonData)
        times = json.loads(jsonData)
        with open("src/model/times.json", "w") as outfile:
            json.dump(this.apiCall(), outfile)

if __name__ == '__main__':
    Distance = DistanceAPI()
    Distance.apiToJSON()