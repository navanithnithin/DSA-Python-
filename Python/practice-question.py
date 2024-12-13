weatherSearch={ }
with open("nyc_weather.csv","r") as f:
    for line in f:
         tokens=line.split(',')
         day=tokens[0]
         try:
             temp=int(tokens[1])
             weatherSearch[day]=temp
         except:
             print("invalid temperaturn . ignore the row")
             

print(weatherSearch['Jan 9'])
print(weatherSearch)

dist1={}
with open("poem.txt",'r')as g:
    for line in g:
        poems=line.split(' ')
        for poem in poems:
            poem=poem.replace("/n",'')
            if poem in dist1:
                dist1[poem]+=1
            else:
                dist1[poem]=1

print(dist1)
            
        
        