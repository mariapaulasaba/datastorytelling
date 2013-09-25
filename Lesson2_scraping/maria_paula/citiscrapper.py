import urllib
import time



if __name__ == '__main__':
	citibike_url = "http://citibikenyc.com/stations/json/"


	counter = 0
	while(True):
		citi_handler = urllib.urlopen(citibike_url)
		citi_data = citi_handler.read()
		citi_handler.close()
		#print citi_data


		#f == that file
		f = open("citi_data" + str(counter) +".txt", 'w')
		f.write(citi_data)
		f.close()

		print counter
		counter += 1

		time.sleep(120)



