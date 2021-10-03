import pandas as pd
from datetime import datetime
currentMonth = datetime.now().month
currentYear = datetime.now().year

LOO=['land','ocean']
continents=['Northern Hemisphere','Southern Hemisphere','Africa','Asia','Europe','North America','Oceania','South America']
for loo in LOO:
    for conti in continents:
        f=open('dataset/OriginalNASA_temparature/'+loo+'_'+conti+'.csv')
        lines=f.readlines()
        lines=lines[5:]#Throw away the front 5 lines.
        l_year,l_month,l_temperature=[],[],[]
        for line in lines:
            li=line.split(',')
            l_year.append(li[0][:4])
            l_month.append(li[0][4:])
            l_temperature.append(float(li[1]))
        df=pd.DataFrame({'year':l_year,'month':l_month,'temperature':l_temperature})
        df.to_csv('dataset/NewNASA_temparature/'+loo+'_'+conti+'.csv',index=False)

