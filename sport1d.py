from select import select
from requests_html import AsyncHTMLSession
from collections import defaultdict
import pandas as pd 



url = 'https://www.sport1.de/daten/fussball/bundesliga/live-ticker/opta_2215487'

asession = AsyncHTMLSession()

async def get_scores():
    r = await asession.get(url)
    await r.html.arender(timeout=20)
    return r



results = asession.run(get_scores)
results = results[0]



times = results.html.find("span.sc-bxivhb.hNtQhx")

home_teams = results.html.find("a.sc-htpNat.hQyhqL")
away_teams = results.html.find("a.sc-htpNat.hcBMCQ")
scores = results.html.find("div.sc-bdVaJa.kKbWlg")
home_team_sub = results.html.find("div.sc-iwsKbI.eYTWeY")
away_team_sub = results.html.find("div.sc-iwsKbI.eYTWeY")
player = results.html.find("div.sc-iwsKbI.QdWrS")
bench = results.html.find('span.sc-bxivhb.dXPzyE') 
away_bench=results.html.find('span.sc-bxivhb.eRZWLC') 
goal_scorer=results.html.find('div.sc-dnqmqq.AaHTm') 
away_goal_scorer=results.html.find('div.sc-dnqmqq.biNTjK') 
yellow_card=results.html.find('div.sc-iwsKbI.iDmdKr')



dict_res1 = defaultdict(list)



# for ind in range(len(times)):
   
   
#     #find date and team name
#     dict_res['Datum'].append(times[ind].text)
#     dict_res['paarung'].append(home_teams[ind].text)
#     dict_res['paarung_2'].append(away_teams[ind].text)
    
#     # #goal score
#     dict_res['Ergebnis'].append(scores[ind].text[0])
#     dict_res['Ergebnis_2'].append(scores[ind].text[4])
    
#     #home team player
#     dict_res['spieler1'].append(player[0].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler2'].append(player[1].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler3'].append(player[2].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler4'].append(player[3].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler5'].append(player[4].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler6'].append(player[5].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler7'].append(player[6].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler8'].append(player[7].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler9'].append(player[8].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler10'].append(player[9].text.encode('ascii','ignore').decode().replace('\n',' '))
#     dict_res['spieler11'].append(player[10].text.encode('ascii','ignore').decode().replace('\n',' '))
    
   
#     # #home team bench
# for i in range(len(bench)):
#     dict_res['spieler12'].append(bench[i].text.encode('ascii','ignore').decode().replace('\n',' '))
   
   
    
#     #away team player
# dict_res['spieler1a'].append(player[11].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler2a'].append(player[12].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler3a'].append(player[13].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler4a'].append(player[14].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler5a'].append(player[15].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler6a'].append(player[16].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler7a'].append(player[17].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler8a'].append(player[18].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler9a'].append(player[19].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler10a'].append(player[20].text.encode('ascii','ignore').decode().replace('\n',' '))
# dict_res['spieler11a'].append(player[21].text.encode('ascii','ignore').decode().replace('\n',' '))
    

   
    
#     # # #away team bench
# for i in range(len(away_bench)):
#     dict_res['spieler12a'].append(away_bench[i].text.encode('ascii','ignore').decode().replace('\n',' '))
   
from collections import defaultdict
import pandas as pd 

dict_res = defaultdict(list)

dict_res['Datum']
dict_res['paarung']
dict_res['paarung_2']
df_res = pd.DataFrame(dict_res)

print(dict_res)




df_res.to_csv('sportd1q.csv',mode='a', header=True)






