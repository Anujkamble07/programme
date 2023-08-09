import json
file=open("D:\\employee.json","r")
y=file.read()
final=json.loads(y)
print(final)
print(type(final))

for x in final:
    print(x,final[x])
# state={}
# state["punjab"]=[{"name":"punjab","capital": "lahor"}]
# state["maharashtra"]=[{"name":"maharashtra","capital": "mumbai"}]
# state["uttar pradesh"]=[{"name":"uttar pradesh","capital": "lucknow"}]
# state["odisa"]=[{"name":"odisa","capital": "bhuneshwar"}]
# state["tamil nadu"]=[{"name":"tamil nadu","capital": "chennai"}]
# state["andra pradesh"]=[{"name":"andra pradesh","capital": "amravati"}]
# state["chattisgarh"]=[{"name":"chattisgarh","capital": "raipur"}]

# print(state)
# with open("employee.json","w") as f:
#     json.dump(state,f)
# print(json.dumps(state, indent =4)) 



