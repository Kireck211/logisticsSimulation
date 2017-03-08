f = open("locations.txt", "r")
output = open("maps.txt", "w")

entregas = []
firstComma = 0
secondComma = 0

deliveries = int(f.readline())

for i in range(0, deliveries + 1):
	line = f.readline()
	firstComma = line.index(',')
	secondComma = line.index(',', firstComma + 1)
	location = line[:firstComma] + "," +  line[firstComma + 1: secondComma]
	output.write("maps.google.com/?q=" + location+"\n")

output.close()
f.close()
