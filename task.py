import time
from decimal import Decimal


content = """ 
"1234567890": {"state":1}, "9876543210": {"state":2}, "4567890123": {"state":0}, "34235678": {"state":34},
"3730723682": {"state":0}, "4030330765": {"state":1}, "123456789": {"state":2},
"9876543210": {"state":1}, "111222333": {"state":2}, "444555666": {"state":1},
"777888999": {"state":0}, "88888888": {"state":1}, "9999999999": {"state":2},
"100200300": {"state":0}, "9999999": {"state":12}
"""

def parseString(content):
    keys = []
    states = []
    content_list = content.split(",")
   
    for i, item in enumerate(content_list):
        sep_pos = item.index(':')
        key_part = item[0:sep_pos].strip().strip('"')
        state_part = item[sep_pos+1:len(item)].strip().strip(':"state}{')
        
        keys.append(key_part)
        states.append(state_part)
    
    return keys,states


start_time = time.time()
ids, states = parseString(content)
end_time = time.time()
execution_time = round(Decimal(end_time - start_time)*1000, 5)

print(f'took {execution_time} ms\n')
print(f'ids:{ids} \nstates:{states}')
