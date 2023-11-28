#Name- Sarthak Shinde
#Batch -B3
#Roll no- 57
#Assignment Name- Regular expression

import re

regex = r"([0-9]{2})/([0-9]{2})/([0-9]{4})"

test_str = "Today is 28/11/2023.My birth date is 22/05/2002"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


#OUTPUT-
#Match 1 was found at 9-19: 28/11/2023
#Group 1 found at 9-11: 28
#Group 2 found at 12-14: 11
#Group 3 found at 15-19: 2023
#Match 2 was found at 37-47: 22/05/2002
#Group 1 found at 37-39: 22
#Group 2 found at 40-42: 05
#roup 3 found at 43-47: 2002
