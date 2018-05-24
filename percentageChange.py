import csv

def business_to_number(x):
    number = 0
    if 'K' in x:
        if len(x) > 1:
            number = float(x.replace('K', '')) * 1000 # convert K to a thousand
    elif 'M' in x:
        if len(x) > 1:
            number = float(x.replace('M', '')) * 1000000 # convert M to a million
    elif 'B' in x:
        number = float(x.replace('B', '')) * 1000000000 # convert B to a Billion
    else:
        number = int(x) # Less than 1000
    return int(number)

# this_month = ['19.7K']
# last_month = ['9.6K']
# this_month = ['19.7K','2.3M','5.9B','252.4K','451.6K','1.3M','1M','18.5M','26.8M','3.2B','96.1M']
# last_month = ['9.6K','4.5M','4.8B','466.9K','8.2M','679.8K','799.3K','18.5M','52.2M','2.8B','81.3M']

#with open('this_month.csv', 'rb') as f:
this_month = []
last_month = []
labels = []

with open('/Users/cnororis/Documents/Carlos/git/Percentage-Change-Calculator/this_month.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        this_month.append(row[0])

with open('/Users/cnororis/Documents/Carlos/git/Percentage-Change-Calculator/last_month.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        last_month.append(row[0])

with open('/Users/cnororis/Documents/Carlos/git/Percentage-Change-Calculator/labels.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        labels.append(row[0])

# print(this_month)
# print(last_month)
# print(labels)

for tm, lm, labels in zip(this_month, last_month, labels) :
    diff = business_to_number(tm) - business_to_number(lm)
    if business_to_number(lm) != 0 :
        if business_to_number(tm) != 0 :
            percentageChange = int(round(((diff* 1.0) / business_to_number(lm)) * 100))
            if percentageChange < 0 :
                print(labels+': '+str(percentageChange)+'% decrease of')
            if percentageChange >= 0 :
                print(labels+': '+str(percentageChange)+'% increase of')
        else :
            print(labels+': '+'Ooops, one of the values is zero :P')
    else :
        print(labels+': '+'Ooops, one of the values is zero :P')
    print tm, lm
