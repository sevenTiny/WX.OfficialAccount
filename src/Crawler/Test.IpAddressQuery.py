from IpAddressQuery import IpAddressQuery
import json


def getCurrentIp():
    obj = IpAddressQuery()

    result = obj.getCurrentIp()

    print(result)

try:
    getCurrentIp()

except Exception as e:
    print(str(e))
