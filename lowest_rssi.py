import requests
import string
import time

my_devices = {
    "device_1" : "Mobile",
    "device_2" : "SmartWatch",
    "device_3" : "AirPods",
}

# url = "http://ec2-3-83-240-213.compute-1.amazonaws.com:64000/zone/best_zone"

zone1_rssi = requests.get("http://192.168.4.2").json()
zone1_rssi = int(zone1_rssi['rssi'])

zone2_rssi = requests.get("http://192.168.4.3").json()
zone2_rssi = int(zone2_rssi['rssi'])

zone3_rssi = requests.get("http://192.168.4.6").json()
zone3_rssi = int(zone3_rssi['rssi'])

def highest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The highest of the 3 RSSI values is : ", largest_num)
    
def lowest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    if (smallest_num == num1):
        zone = "Sofa"
    elif (smallest_num == num2):
        zone = "Kitchen"
    elif (smallest_num == num3):
        zone = "Bedroom"
    print(" -> Device is on the :", my_devices[zone])

    #print("The lowest of the 3 RSSI values is : " \
    #      + str(smallest_num) + " at " + zone)
    payload = {'name': 'best_zone', 'zname': zone}\
    # print(payload)
    # response = requests.put(url=url, data=payload)
    
#highest(zone1_rssi, zone2_rssi, zone3_rssi)

def find_devices(num1, num2, num3):
    while True:
        print(my_devices["device_1"], "RSSI value is", num1)
        print(my_devices["device_2"], "RSSI value is", num2)
        print(my_devices["device_3"], "RSSI value is", num3)
        time.sleep(1)
lowest(zone1_rssi, zone2_rssi, zone3_rssi)
find_devices(zone1_rssi, zone2_rssi, zone3_rssi)
