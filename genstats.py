stats = open('stats.txt', 'r')
lines = stats.readlines()
weightedSum = 0
samples = 0
bufferuse = 0
detected = 0
accurate = 0
for line in lines:
    data=line.strip().split()
    frames = int(data[0])
    accuracy = int(data[1])
    weightedSum += frames*accuracy
    samples += frames
    bufferuse += int(data[2])
    detected += int(data[3])
    accurate += int(data[5])
netacc = weightedSum/samples
print("Calculated net accuracy: ", str(netacc)[0:5])
print("Actual accurate matches: ", accurate)
print("Buffered matches: ", bufferuse)
print("Invalid matches: ", detected-(accurate+bufferuse))
print("Total buffer use percentage: ", str(bufferuse*100/detected)[0:5])
