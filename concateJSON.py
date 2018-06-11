import json
import io

hashMap = {}
stressMap = {}
valid_states_map = {}
arr = []
HR_limit = 84
with io.open('Steps_D1.json', encoding="utf-8") as json_file:
	data = json.load(json_file)
	index = 0
	for item in data:
        	hashMap[item['time']] = item['value']
		arr.append([])
		arr[index].append(item['time'])
		arr[index].append(item['value'])
		valid_states_map[item['time']] = 1
		index = index + 1
threshold = 119
slot_size = 25
min_rest = 3
for i in range(0,len(arr)):
	if arr[i][1] == 0:
		continue
	step_count = min(arr[i][1],threshold)
	next_invalid_slot = (step_count/slot_size) + min_rest
	print next_invalid_slot
	for j in range(0,next_invalid_slot+1):
		if(i+j>=len(arr)):
			break
		valid_states_map[arr[i+j][0]] = 0
		
#print valid_states_map
exit()
output = open("HR_Steps_D1.csv","w")
output.write("time,heartrate,steps,stress\n") 
with io.open('HR_D1.json', encoding="utf-8") as json_file:
	data = json.load(json_file)
	for item in data:
		stress_value = 0
		if item['value'] > HR_limit:
			stress_value = (item['value'] - HR_limit) * valid_states_map[item['time']]
		output.write(item['time']+","+str(item['value'])+","+str(hashMap[item['time']])+","+str(stress_value)+"\n")
	output.close()
        	
