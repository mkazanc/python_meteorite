import requests
import math

def calc_dist(lat1, lon1):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(28.060411)
	lon2 = math.radians(-80.630360)
	h = math.sin((lat2 - lat1)/2 )**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2 - lon1)/2)**2
	return 6372.8 * 2 * math.asin(math.sqrt(h))
resp=requests.get('https://data.nasa.gov/resource/y77d-th95.json')
meteor_data=resp.json()

for hit in meteor_data:
	if not ('reclat' in hit and 'reclong' in hit):continue
	hit['distance']=calc_dist(float(hit['reclat']),float(hit['reclong']))

def get_dist(meteor): #gets distance from each record
	return meteor.get('distance',math.inf)
	
meteor_data.sort(key=get_dist)

for n in range(10):
	print(str(meteor_data[n]['distance'])+ "kms away in " + meteor_data[n]['year'][0:4])


