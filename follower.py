
#https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
#https://www.geeksforgeeks.org/read-json-file-using-python/


import json
  



def loadFileToList(filename, following = False):
	usedFileName = filename + ".json"
	file = open(usedFileName)
	data = json.load(file)
	valueList = []
	if not following:
		for i in data['string_list_data']:
		    valueList.append(i['value'])
	else:
		for i in data['relationships_following']:
			for j in i['string_list_data']:
				print(j['value'])
				valueList.append(j['value'])
	file.close()
	return valueList

followers = loadFileToList("followers_1")
following = loadFileToList("following", True)

print(followers)
print(following)

followDiff = {}

for fol in following:
	followDiff[fol] = followDiff.get(fol, 0) + 1

for fol in followers:
	followDiff[fol] = followDiff.get(fol, 0) - 1

youOnlyFollowThem, theyOnlyFollowYou, followBothWays = [],[], []


for account in followDiff:
	if followDiff[account] == 0:
		followBothWays.append(account)
	else if followDiff[account] == 1:
		youOnlyFollowThem.append(account)
	else if followDiff[account] == -1:
		theyOnlyFollowYou.append(account)
	else:
		print("ERROR. SHOULD NOT OCCUR")

print("You follow them, they follow you: ", followBothWays)
print("You follow them, they don't follow you: ", youOnlyFollowThem)
print("You don't follow them, they follow you: ", theyOnlyFollowYou)


