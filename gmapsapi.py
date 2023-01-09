import requests

googleApiKey= 'AIzaSyB2tQN6E8ujV_LslOAFU3ERgTgzO8dzKTc'

existingShops = []
f = open("addys.txt", "r").readlines()
for line in f:
    existingShops.append(line.strip().replace('\n', ''))
latExistingShops = []
lngExistingShops = []
#get lat and lng of existing shops
for shop in existingShops:
    print(shop)
    try:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+shop+'&key='+googleApiKey)
        resp_json_payload = response.json()
        latExistingShops.append(resp_json_payload['results'][0]['geometry']['location']['lat'])
        lngExistingShops.append(resp_json_payload['results'][0]['geometry']['location']['lng'])
    except:
        print("error")
#add lat and lng to file latlng.txt
f = open("latlng.txt", "w")
for i in range(len(latExistingShops)):
    f.write(str(latExistingShops[i]) + "," + str(lngExistingShops[i]) + "\n")