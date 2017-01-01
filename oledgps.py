import sys
while True:
    line = sys.stdin.readline()
    if line == '':
        sys.exit(0)
    stripline = line.strip()
    fields = stripline.split(',')
    datestring = str(fields[1])
    hours = datestring[0:2]
    minutes = datestring[2:4]
    seconds = datestring[4:]
    print "%s:%s:%s" % (hours, minutes, seconds)
    lat = float(fields[2])
    fixlat = lat / 100.0
    longitude = float(fields[4])
    fixlongitude = longitude / 100.0
    print "%s %s, %s %s" % (fixlat, fields[3], fixlongitude, fields[5])
#    fixindicator = int(fields[6])
#    if fixindicator == 0:
#        print "No fix."
#    elif fixindicator == 1:
#        print "GPS fix."
#    elif fixindicator == 2:
#        print "Differential GPS fix."
#    print "Satellites used: %d" % int(fields[7])
#    print "MSL Altitude: %f" % round(float(fields[9]),4)
