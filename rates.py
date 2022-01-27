import pandas as pd
import json
import time

last_updated=time.strftime('%Y-%m-%dT%H:%M', time.localtime())

mylist=[]

dfs2 = pd.read_html('https://sarafi.af/en/exchange-rates/sarai-shahzada')
dfs = dfs2[0]
print(dfs.columns)
def write_json(data,filename='AFN_rates.json'):
    with open (filename,'w') as f:
        json.dump(data,f,indent=4, ensure_ascii=False) 
    
result = dfs.to_json(orient="index")
#print(result)
parsed = json.loads(result)
for x in parsed:
    parsed[x]["last_updated"]=last_updated
    mylist.append(parsed[x])
    #print(parsed[x]) 
write_json(mylist)

listA=mylist[0]
listB=mylist[1]
# list1=listA['USD in Other Markets']+" Buy:",listA['Buy'],'**** Sell:',listA['Sell']
# print(listA['USD in Other Markets']+" Buy:",listA['Buy'],'**** Sell:',listA['Sell'])
# list2=listB['USD in Other Markets']+" Buy:",listB['Buy'],'**** Sell:',listB['Sell']
# print(list2)