from time import time
from requests_html import AsyncHTMLSession
from collections import defaultdict
import pandas as pd 



val_url='https://www.kicker.de/2-bundesliga/spieltag/2021-22/28'

if val_url:
    url = 'https://www.kicker.de/2-bundesliga/spieltag/2021-22/28'


    asession = AsyncHTMLSession()

    async def get_scores():
        r = await asession.get(url) 
        await r.html.arender(timeout=25)
        return r



    results = asession.run(get_scores)
    results = results[0]


    value=results.html.find("div.kick__v100-gameList.kick__module-margin")    
    date_val=[]
    list_val=[]
    all_value=[]
    list_val1=[]
    list_val2=[]
    list_val3=[]
    list_val4=[]
    list_val5=[]
    list_val6=[]
    list_val7=[]
    list_val8=[]
    all_url=[]
    dict_val={}
    list_team=[]
    list_teamB=[]
    list_teamC=[]
    list_teamD=[]
    
    for j in range (len(value)):
        if len(value[j].find('div.kick__v100-gameList__header'))>0:
            z= value[j].find('div.kick__v100-gameList__header')[0].text
            date_val.append(z)  
         
            
            if len(date_val)>0:
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[0]:
                    val22=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard")
                   
                    for i in range (len(val22)):
                        url_score=val22[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                       
                        url_date=value[j].find("div.kick__v100-gameList__header")[0]
                                           
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                            teamA=value[j].find("div.kick__v100-gameCell__team__name")
                           
                            
                        
                       
                        val1="kicker.de"+url_score["href"]
                        val_text=val1.replace("analyse","aufstellung") 
                        
                       # val_text2=val_text.replace("schema","aufstellung")
                        list_val1.append(val_text)       
                      
                        
                        all_url.append(val_text)
                        
                    for i in range (len(teamA)):
                        val_te=teamA[i].text
                        list_val1.append(val_te)
                   # print("we",list_team)
                        
                    #list_val1.insert(0,list_team)
                    # list_val1.insert(1,list_team[1])
                    dict_val[date_val[0]]=list_val1
                
                    
            if len(date_val)>1:
                    if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[1]:
                        val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard")
                        for i in range (len(val23)):
                            url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                            url_date1=value[j].find("div.kick__v100-gameList__header")[0]
                            if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamB=value[j].find("div.kick__v100-gameCell__team__name")
                                
                        
                            
                            
                            val2="kicker.de"+url_score["href"]
                            val_text=val2.replace("analyse","aufstellung")
                            #val_text2=val_text.replace("schema","aufstellung")
                            list_val.append(val_text)
                            
                            all_url.append(val_text)   
                            
                        for i in range (len(teamB)):
                                val_te=teamB[i].text
                            
                                list_val.append(val_te)
                        
                        dict_val[date_val[1]]=list_val
                       # print(dict_val[date_val[1]])
            
                    
            if len(date_val)>2:
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[2]:
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard")
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date1=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                            teamC=value[j].find("div.kick__v100-gameCell__team__name")
                            #print("action",teamC[0].text)
                            #print("action2",teamC[1].text)

                        
                        
                        val2="kicker.de"+url_score["href"]
                        val_text=val2.replace("analyse","aufstellung")
                        #val_text2=val_text.replace("schema","aufstellung")
                        list_val2.append(val_text)
                        
                        all_url.append(val_text)   
                        
                        
                    for i in range (len(teamC)):
                            val_te=teamC[i].text
                           
                            list_val2.append(val_te)
                      
                    dict_val[date_val[2]]=list_val2
                 
                  
                
           
                    

            if len(date_val)>3:
               
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[3]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamD=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val3.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[3]]=list_val3
                    for i in range (len(teamD)):
                            val_te=teamD[i].text
                           
                            list_val3.append(val_te)
                    dict_val[date_val[3]]=list_val3
                    
                    
            if len(date_val)>4:
                   
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[4]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamE=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val4.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[4]]=list_val4
                    for i in range (len(teamE)):
                            val_te=teamE[i].text
                           
                            list_val4.append(val_te)
                    dict_val[date_val[4]]=list_val4
                    
            if len(date_val)>5:
                   
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[5]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamF=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val5.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[5]]=list_val5
                    for i in range (len(teamF)):
                            val_te=teamF[i].text
                           
                            list_val5.append(val_te)
                    dict_val[date_val[5]]=list_val5        
                    
                    
            if len(date_val)>6:
                   
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[6]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamG=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val6.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[6]]=list_val6
                    for i in range (len(teamG)):
                            val_te=teamG[i].text
                           
                            list_val6.append(val_te)
                    dict_val[date_val[6]]=list_val6        
                    
            
            if len(date_val)>7:
                   
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[7]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamH=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val7.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[7]]=list_val7
                    for i in range (len(teamH)):
                            val_te=teamH[i].text
                           
                            list_val7.append(val_te)
                    dict_val[date_val[7]]=list_val7  
                    
            if len(date_val)>8:
                   
                if value[j].find('div.kick__v100-gameList__header')[0].text== date_val[8]: 
                    val23=value[j].find("div.kick__v100-gameCell.kick__v100-gameCell--standard") 
                    for i in range (len(val23)):
                        url_score=val23[i].find("a.kick__v100-scoreBoard.kick__v100-scoreBoard--standard")[0].attrs
                        url_date3=value[j].find("div.kick__v100-gameList__header")[0]
                        if len(value[j].find("a.kick__v100-gameCell__team ")[0].find("div.kick__v100-gameCell__team__name"))>0:
                                teamI=value[j].find("div.kick__v100-gameCell__team__name")
                            
                    
                       
                        val3="kicker.de"+url_score["href"]
                        val_text=val3.replace("analyse","aufstellung")
                        list_val8.append(val_text)
                        all_url.append(val_text)    
                        dict_val[date_val[8]]=list_val8
                    for i in range (len(teamI)):
                            val_te=teamI[i].text
                           
                            list_val8.append(val_te)
                    dict_val[date_val[8]]=list_val8
                    
                    
        
        

list_dict=(list(dict_val.keys())[0])
# print(list_dict)
ten=all_url[:9]

# print("llll",date_val)
val_url2=list_val1

# print("Sss",all_url)
if val_url2 ==list_val1:   
   
    for q in range (len(ten)):
        
        url ="http://"+ten[q] 
        
        asession = AsyncHTMLSession()

        async def get_scores():
            r = await asession.get(url) 
            await r.html.arender(timeout=25)
            return r



        results = asession.run(get_scores)
        results = results[0]



        all_goal=results.html.find('div.kick__game-timeline__event-icon.kick__js_overlay-card-trigger.kick__game-timeline__event-icon--team-top',first=True)
        d1=all_goal.find('span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball')
        goal_scorer123=results.html.find('div.kick__game-timeline') 
        goal_scorer1=results.html.find('div.kick__game-timeline') 



        score_goal12=[]
        for j in range (len(goal_scorer1)):    
            if len(goal_scorer1[j].find('div.kick__game-timeline__event-icon.kick__js_overlay-card-trigger.kick__game-timeline__event-icon--team-top'))>0: 
                if len(goal_scorer1[j].find('div.kick__game-timeline__event-icon.kick__js_overlay-card-trigger.kick__game-timeline__event-icon--team-top')[0].find("span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball"))>0:
                    if len(goal_scorer1[j].find("div.kick__ticker-event-overlay-box.kick__js_overlay-card.kick__ticker-event-overlay-box--with-player"))>0:
                        if len (goal_scorer1[j].find("div.kick__ticker-event-overlay-box.kick__js_overlay-card.kick__ticker-event-overlay-box--with-player")[0].find("div.kick__ticker-event-overlay-box__header"))>0:
                            gold=goal_scorer1[j].find("div.kick__ticker-event-overlay-box.kick__js_overlay-card.kick__ticker-event-overlay-box--with-player")[0].find("div.kick__ticker-event-overlay-box__header")[0]
                            score_goal12.append(gold)                        
                            
        timed=[]          

        for z in range (len(score_goal12)): 
            timed.append(score_goal12[z].text)     

        goal_scorer=results.html.find('div.kick__lineup-field__field-half.kick__lineup-field__field-half--top',first=True) 
        if goal_scorer:
            kick_player=goal_scorer.find('a.kick__lineup-player-card')
        panther=results.html.find('div.kick__ticker-event-overlay-box.kick__js_overlay-card.kick__ticker-event-overlay-box--with-player') 
        time2=results.html.find('div.kick__game-timeline__event-icon.kick__js_overlay-card-trigger.kick__game-timeline__event-icon--team-top')
        checked=results.html.find('div.kick__ticker-event-overlay-box__header')
        checked2=results.html.find('div.kick__ticker-event-overlay-box__content')



        #home team goal time
        value=[]
        for i in range(len(checked)):    
            for a in checked[i].element.iterancestors():          
                if a.getprevious() is not None:          
                    for t in a.getprevious().getchildren():           
                        z=a.getprevious().attrib          
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--black kick__icon-Fussball' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":
                            ans=checked[i].element.text_content().split(" ")[2]
                            value.append(ans)
                                                
                break    
            
        #home team scorer name
        value1=[]
        for i in range(len(checked2)):  
            for a in checked2[i].element.iterancestors(): 
                if a.getprevious() is not None:
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--black kick__icon-Fussball' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":
                            if checked2[i].find("a"):        
                                ans=checked2[i].find('a')[0].text               
                                value1.append(ans)
                        
                            
                                                
                break        
                
                
                
        # home red card time
        home_red_value=[]
        for i in range(len(checked)):    
            for a in checked[i].element.iterancestors():          
                if a.getprevious() is not None:          
                
                    for t in a.getprevious().getchildren():           
                        z=a.getprevious().attrib          
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--red kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":
                            
                            ans=checked[i].element.text_content().split(" ")[2]
                            home_red_value.append(ans)
                            # print(home_red_value)
                                                
                break 
                    
                
                
                
        # away red card time
        away_red_value=[]
        for i in range(len(checked)):    
            for a in checked[i].element.iterancestors():          
                if a.getprevious() is not None:          
                
                    for t in a.getprevious().getchildren():           
                        z=a.getprevious().attrib   
                        ze=a.getprevious().getchildren()
                        for r in ze:

                            if r.attrib['class']=="kick__ticker-icon-array":
                                child=r.getchildren()
                        
                                for ch in child:
                                    if ch.attrib['class'] == "kick__ticker-icon kick__ticker-icon-color--yellow kick__ticker-icon-lower kick__icon-Gelb":
                                        
                                        mix=checked[i].element.text_content().split(" ")[2]
                                        
                                        away_red_value.append(mix)
                       # print("180",bo_yellow_value)
                        
                        away_cardtime=away_red_value[:-1] 
  
 
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--red kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom":
                            
                            ans=checked[i].element.text_content().split(" ")[2]
                            away_red_value.append(ans)
                          
                                                
                break 
            
            
        #home red card player name    
        home_red_value1=[]
        for i in range(len(checked2)):  
            for a in checked2[i].element.iterancestors(): 
                if a.getprevious() is not None:
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--red kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":
                            ans=checked2[i].find('a')[0].text               
                            home_red_value1.append(ans)
                        
                            
                                                
                break        
            
        #away red card payer name
        away_red_value1=[]
        for i in range(len(checked2)):  
            for a in checked2[i].element.iterancestors(): 
                if a.getprevious() is not None:
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib
                        ze=a.getprevious().getchildren()
                        for r in ze:

                            if r.attrib['class']=="kick__ticker-icon-array":
                                child=r.getchildren()
                        
                                for ch in child:
                                    if ch.attrib['class'] == "kick__ticker-icon kick__ticker-icon-color--yellow kick__ticker-icon-lower kick__icon-Gelb":
                                      
                                        mix=checked2[i].find('a')[0].text
                                        
                                        away_red_value1.append(mix)
                                        print("k2",away_red_value1)
                        
                        
                        away_cardname=away_red_value1[:-1]
                      
                    
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--red kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom":
                            print("enter")
                            if checked2[i].find('a'):
                                ans=checked2[i].find('a')[0].text               
                                away_red_value1.append(ans)
                    
                        print(away_red_value1)    

                break    
            
            
            
        #home yellow card player name
        yel_value1=[]
        for i in range(len(checked2)): 
            for a in checked2[i].element.iterancestors():      
                if a.getprevious() is not None:   
                    for t in a.getprevious().getchildren():      
                        z=a.getprevious().attrib     
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--yellow kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":      
                            if checked2[i].find("a"):
                                ans=checked2[i].find('a')[0].text                
                                yel_value1.append(ans)                                  
                break         

            
        #away yellow card player name
        bot_yel_value1=[]
        for i in range(len(checked2)): 
            for a in checked2[i].element.iterancestors():       
                if a.getprevious() is not None:  
                    for t in a.getprevious().getchildren():  
                        z=a.getprevious().attrib 
                        ze=a.getprevious().getchildren()
                        for r in ze:

                            if r.attrib['class']=="kick__ticker-icon-array":
                                child=r.getchildren()
                        
                                for ch in child:
                                    if ch.attrib['class'] == "kick__ticker-icon kick__ticker-icon-color--yellow kick__ticker-icon-lower kick__icon-Gelb":
                                        mix=checked2[i].find('a')[0].text
                                        
                                        bot_yel_value1.append(mix)
                        away_yelname=bot_yel_value1[:-1]
                       
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--yellow kick__icon-Gelb'  and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom" : 
                            if checked2[i].find('a'):
                                ans=checked2[i].find('a')[0].text        
                                bot_yel_value1.append(ans)       
                        print("sssss",bot_yel_value1)
                          
                        
                                            
                break  
        
        #home yellow card player name
        bot_value1=[]
        for i in range(len(checked2)):    
            for a in checked2[i].element.iterancestors():         
                if a.getprevious() is not None:    
                    for t in a.getprevious().getchildren():  
                        z=a.getprevious().attrib    
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--black kick__icon-Fussball' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom":     
                            ans=checked2[i].find('a')[0].text
                            #print(ans)                
                            bot_value1.append(ans)                
                                                
                break    
            


        #away scorer card player time

        bottom_value=[]
        for i in range(len(checked)):
            
            for a in checked[i].element.iterancestors():   
                if a.getprevious() is not None:   
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib   
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--black kick__icon-Fussball' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom":
                        # print("enter away")
                            ans=checked[i].element.text_content().split(" ")[2]
                            bottom_value.append(ans)
                                            
                break    
            
            

        #home yellow card time    
        yellow_value=[]
        for i in range(len(checked)):
            for a in checked[i].element.iterancestors():
                
                if a.getprevious() is not None:
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib
          
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--yellow kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-top":
                            
                            ans=checked[i].element.text_content().split(" ")[2]
                    
                            yellow_value.append(ans)
                        #print("ooo",yellow_value)
                                                
                break 
            
        #away yellow card time
        bo_yellow_value=[]
        for i in range(len(checked)):
            for a in checked[i].element.iterancestors():
                
                if a.getprevious() is not None:
                    for t in a.getprevious().getchildren():
                        z=a.getprevious().attrib
                        
                        ze=a.getprevious().getchildren()
                        for r in ze:

                            if r.attrib['class']=="kick__ticker-icon-array":
                                child=r.getchildren()
                        
                                for ch in child:
                                    if ch.attrib['class'] == "kick__ticker-icon kick__ticker-icon-color--yellow kick__ticker-icon-lower kick__icon-Gelb":
                                        
                                        mix=checked[i].element.text_content().split(" ")[2]
                                        
                                        bo_yellow_value.append(mix)
                       # print("180",bo_yellow_value)
                        
                        away_yeltime=bo_yellow_value[:-1]
                        
                        
                        if t.attrib['class']=='kick__ticker-icon kick__ticker-icon-color--yellow kick__icon-Gelb' and z["class"] == "kick__game-timeline__event-icon kick__js_overlay-card-trigger kick__game-timeline__event-icon--team-bottom":
                            
                            ans=checked[i].element.text_content().split(" ")[2]
                            bo_yellow_value.append(ans)
                        #print(bo_yellow_value)
                       # print("190",child_all22)
                                                
                break    

        goal_time=[]
        for j in range (len(time2)):   

            if len(time2[j].find('span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball'))>0:
            
                fine=results.html.find("div.kick__ticker-event-overlay-box.kick__js_overlay-card.kick__ticker-event-overlay-box--with-player")
            
                goal_time.append(fine)
            
        half_time_score=results.html.find('div.kick__v100-scoreBoard__scoreHolder.kick__v100-scoreBoard__scoreHolder--subscore')
        away_goal_scorer=results.html.find('div.kick__lineup-field__field-half.kick__lineup-field__field-half--bottom',first=True) 
        if away_goal_scorer:
            bottom_kick_player=away_goal_scorer.find('a.kick__lineup-player-card')
        score=results.html.find('div.kick__v100-scoreBoard__scoreHolder')
        home_team=results.html.find('div.kick__v100-gameCell__team__name')
    
        date=results.html.find('div.kick__v100-scoreboardInfo')
       
        spil=date[0].text.split(" ")
        check_date=spil[0]
        print(spil[3])
        player=results.html.find('span.kick__lineup-player-card__name')
        sub_2=results.html.find('div.kick__data-grid-tablet--gutter-right')
        print(sub_2)
      
        home_team1=sub_2[0].find('div.kick__ticker__cell-text')
        home_time=sub_2[0].find('div.kick__ticker__minute')

        home_goalssss=sub_2[0].find("div.kick__ticker__cell-text")
        home_team12=sub_2[0].find('div.kick__ticker__cell-text')

        striker=""
        for j in range (len(home_goalssss)): 
            if len(home_goalssss[j].find('p'))>0:
                if len(home_goalssss[j].find('p')[0].find("span.kick__badge"))>0:
                    if len(home_goalssss[j].find('p')[0].find("span.kick__badge")[0].find("span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball"))>0:
                        sub_goal=home_goalssss[j].find('p')[0].text.encode('ascii','ignore').decode().replace('\n',' ')
                        
                        striker=sub_goal.split(" ")[0]
                        
                        
        sub_enter=[]
        sub_out=[]            
        for j in range (len(home_goalssss)): 
            if len(home_goalssss[j].find('p'))>0:
                if len(home_goalssss[j].find('p')[0].find("a"))>0:
                    sub_in=home_goalssss[j].find('p')[0].find("a")[0].text
                    sub_enter.append(sub_in)
                    sub_outs=home_goalssss[j].find('p')[0].find("a")[1].text
                    sub_out.append((sub_outs))
                
                

                                        
                        

        foul=""
        for j in range (len(home_goalssss)): 
            if len(home_goalssss[j].find('p'))>0:
                if len(home_goalssss[j].find('p')[0].find("span.kick__badge"))>0:
                    if len(home_goalssss[j].find('p')[0].find("span.kick__badge")[0].find("span.kick__ticker-icon.kick__ticker-icon-color--yellow.kick__icon-Gelb"))>0:
                        sub_goal=home_goalssss[j].find('p')[0].text.encode('ascii','ignore').decode().replace('\n',' ')
                        
                        foul=sub_goal.split(" ")[0]
                        



        home_sub=[]
        sub_time=[]

        #home subsitute
        for i in range (len(home_team1)):    
            k=home_team1[i].text.encode('ascii','ignore').decode().replace('\n',' ')
            home_sub.append(k)
            
            
        #subsitute time
        for i in range (len(home_time)):    
            k=home_time[i].text.encode('ascii','ignore').decode().replace('\n',' ')
            zz=k.replace("'"," ")
          #  print(zz)
            sub_time.append(zz)
           # print(sub_time)


        #away_team subsiture
        if sub_2:
            away_team=sub_2[1].find('div.kick__ticker__cell-text')
            away_times=sub_2[1].find('div.kick__ticker__minute')
            away_goalssss=sub_2[1].find("div.kick__ticker__cell-text")


        striker1=""
        for j in range (len(away_goalssss)): 
            if len(away_goalssss[j].find('p'))>0:
                if len(away_goalssss[j].find('p')[0].find("span.kick__badge"))>0:

                    
                    if len(away_goalssss[j].find('p')[0].find("span.kick__badge")[0].find("span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball"))>0:
                    
                        sub_goal=away_goalssss[j].find('p')[0].text.encode('ascii','ignore').decode().replace('\n',' ') 
                        striker1=sub_goal.split(" ")[0]
                    

        away_sub_enter=[]
        away_sub_out=[]            
        for j in range (len(away_goalssss)): 
            if len(away_goalssss[j].find('p'))>0:
                if len(away_goalssss[j].find('p')[0].find("a"))>0:
                    sub_in=away_goalssss[j].find('p')[0].find("a")[0].text
                    away_sub_enter.append(sub_in)
                    sub_outs=away_goalssss[j].find('p')[0].find("a")[1].text
                    away_sub_out.append((sub_outs))
            



        foul1=""
        for j in range (len(away_goalssss)): 
            if len(away_goalssss[j].find('p'))>0:
            
                if len(away_goalssss[j].find('p')[0].find("span.kick__badge"))>0:
                    if len(away_goalssss[j].find('p')[0].find("span.kick__badge")[0].find("span.kick__ticker-icon.kick__ticker-icon-color--yellow.kick__icon-Gelb"))>0:      
                        sub_goal=away_goalssss[j].find('p')[0].text.encode('ascii','ignore').decode().replace('\n',' ')
                        foul1=sub_goal.split(" ")[0]
                    


        away_sub=[]
        for i in range (len(away_team)):  
            l=away_team[i].text.encode('ascii','ignore').decode().replace('\n',' ')
            away_sub.append(l)

        away_sub_time=[]
        for i in range (len(away_times)):    
            k=away_times[i].text.encode('ascii','ignore').decode().replace('\n',' ')
            z1=k.replace("'"," ")
            away_sub_time.append(z1)



        dict_res = defaultdict(list)

                    


        #home player scorer
        name=[]
        score_goal=[]
        for j in range (len(kick_player)): 
            if len(kick_player[j].find('div.kick__player-actions'))>0:
                if len (kick_player[j].find('div.kick__player-actions')[0].find('div.kick__badge'))>0:     
                    if len (kick_player[j].find('div.kick__player-actions')[0].find('div.kick__badge')[0].find('span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball'))>0:  
                        
                        #print(kick_player[j].find('div.kick__player-actions')[0].find('div.kick__badge')[0].find('span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball'))
                        
                        name=(kick_player[j].find('div.kick__lineup-player-card__name-holder')[0].find('span.kick__lineup-player-card__name')[0])            
                        score_goal.append(name)
                        
                        
                        
        home_scorer=[]          
        #print("goal",score_goal)
        for z in range (len(score_goal)): 
            home_scorer.append(score_goal[z].text)
        #print(home_scorer[1])

        #home player yellow_card
        yellow_data=[]
        for k in range (len(kick_player)): 
            if len(kick_player[k].find('div.kick__player-actions'))>0:
                if len (kick_player[k].find('div.kick__player-actions')[0].find('div.kick__badge'))>0:
                    if len (kick_player[k].find('div.kick__player-actions')[0].find('div.kick__badge')[0].find('span.kick__ticker-icon.kick__ticker-icon-color--yellow.kick__icon-Gelb'))>0:  
                        yellow_card1=(kick_player[k].find('div.kick__lineup-player-card__name-holder')[0].find('span.kick__lineup-player-card__name')[0])            
                        yellow_data.append(yellow_card1)


        ycard_name=[]          
        for z in range (len(yellow_data)): 
            ycard_name.append(yellow_data[z].text)

                        
        #away player scorer             
        bottom_name=[]  
        away_goal1=[]
        for i in range (len(bottom_kick_player)): 
            if len(bottom_kick_player[i].find('div.kick__player-actions'))>0:
                
                if len (bottom_kick_player[i].find('div.kick__player-actions')[0].find('div.kick__badge'))>0:
                    
                    if len (bottom_kick_player[i].find('div.kick__player-actions')[0].find('div.kick__badge')[0].find('span.kick__ticker-icon.kick__ticker-icon-color--black.kick__icon-Fussball'))>0:   
                        bottom_name=(bottom_kick_player[i].find('div.kick__lineup-player-card__name-holder')[0].find('span.kick__lineup-player-card__name')[0])            
                        away_goal1.append(bottom_name)
        away_scorer=[]          
        box=[]
        for z in range (len(away_goal1)): 
            away_scorer.append(away_goal1[z].text)
            box.append("away_score")
        #print(box)

        #away player yellowcard
        data1=[]
        for h in range (len(bottom_kick_player)): 
            if len(bottom_kick_player[h].find('div.kick__player-actions'))>0:
                if len (bottom_kick_player[h].find('div.kick__player-actions')[0].find('div.kick__badge'))>0:
                    if len (bottom_kick_player[h].find('div.kick__player-actions')[0].find('div.kick__badge')[0].find('span.kick__ticker-icon.kick__ticker-icon-color--yellow.kick__icon-Gelb'))>0:  
                        yellow_card=(bottom_kick_player[h].find('div.kick__lineup-player-card__name-holder')[0].find('span.kick__lineup-player-card__name')[0])              
                        data1.append(yellow_card)
           
        yellow_card_name=[]          
        for z in range (len(data1)): 
            yellow_card_name.append(data1[z].text)

        
        #find date and team name 
        if len(list(dict_val.keys()))>0:
        # if list(dict_val.keys())[0]:
            for i in dict_val[list(dict_val.keys())[0]]:
                
                if home_team[0].text in i:
                    
                    dict_res['Datum'].append(list(dict_val.keys())[0])    
                
        if len(list(dict_val.keys()))>1:
        # if list(dict_val.keys())[1]:
            for i in dict_val[list(dict_val.keys())[1]]: 
                if home_team[0].text in i:
                    
                    dict_res['Datum'].append(list(dict_val.keys())[1])     
           
                 
        #elif list(dict_val.keys())[2]:
        if len(list(dict_val.keys()))>2:
            for i in dict_val[list(dict_val.keys())[2]]: 
                if home_team[0].text in i:
                    print("hello3")
                    dict_res['Datum'].append(list(dict_val.keys())[2]) 
            
            
            
        # # elif list(dict_val.keys())[2]:    
        # if len(list(dict_val.keys()))>3:
        #     for i in dict_val[list(dict_val.keys())[3]]: 
        #         if home_team[0].text in i:
        #             dict_res['Datum'].append(list(dict_val.keys())[3]) 
                    
        # if len(list(dict_val.keys()))>4:
        #     for i in dict_val[list(dict_val.keys())[4]]: 
        #         if home_team[0].text in i:
        #             dict_res['Datum'].append(list(dict_val.keys())[4])             
                    
        # if len(list(dict_val.keys()))>5:
        #     for i in dict_val[list(dict_val.keys())[5]]: 
        #         if home_team[0].text in i:
        #             dict_res['Datum'].append(list(dict_val.keys())[5])     
                    
                    
        # if len(list(dict_val.keys()))>6:
        #     for i in dict_val[list(dict_val.keys())[6]]: 
        #         if home_team[0].text in i:
        #             dict_res['Datum'].append(list(dict_val.keys())[6])       
        
        
        
        # if len(list(dict_val.keys()))>7:
        #     for i in dict_val[list(dict_val.keys())[7]]: 
        #         if home_team[0].text in i:
        #             dict_res['Datum'].append(list(dict_val.keys())[7])      
                    
        
        dict_res['League'].append(date[0].text[0:18])
        if check_date == "Bundesliga":
            dict_res['Spieltag'].append(spil[2])
        else:
            dict_res['Spieltag'].append(spil[3])
       
        dict_res['paarung'].append(home_team[0].text)
        dict_res['paarung_2'].append(home_team[1].text)

        #half time goal scorer
        dict_res['half_time_Ergebnis'].append(half_time_score[0].text[0])
        dict_res['half_time_Ergebnis_2'].append(half_time_score[0].text[4])

        #goal score
        dict_res['Ergebnis'].append(score[0].text[0])
        dict_res['Ergebnis_2'].append(score[0].text[4])

        #home team player
        
        dict_res['spieler1'].append(player[0].text)
        dict_res['spieler2'].append(player[1].text)
        dict_res['spieler3'].append(player[2].text)
        dict_res['spieler4'].append(player[3].text)
        dict_res['spieler5'].append(player[4].text)
        dict_res['spieler6'].append(player[5].text)
        dict_res['spieler7'].append(player[6].text)
        dict_res['spieler8'].append(player[7].text) 
        dict_res['spieler9'].append(player[8].text)
        dict_res['spieler10'].append(player[9].text)
        dict_res['spieler11'].append(player[10].text)

        # #home team SUBSTITUTES
        if len(home_sub) >0:
            
            dict_res["sub_time1"].append(sub_time[0])
            dict_res['sub_in_a1'].append(sub_enter[0])
            dict_res['sub_out_a1'].append(sub_out[0])
            
            dict_res["sub_time2"].append("")
            dict_res['sub_in_a2'].append("")
            dict_res['sub_out_a2'].append("")
            
            dict_res["sub_time3"].append("")
            dict_res['sub_in_a3'].append("")
            dict_res['sub_out_a3'].append("")
            
            dict_res["sub_time4"].append("")
            dict_res['sub_in_a4'].append("")
            dict_res['sub_out_a4'].append("")
            
            dict_res["sub_time5"].append("")
            dict_res['sub_in_a5'].append("")
            dict_res['sub_out_a5'].append("")



        #away team player
       
        dict_res['spieler1a'].append(player[11].text)
        dict_res['spieler2a'].append(player[12].text)
        dict_res['spieler3a'].append(player[13].text)
        dict_res['spieler4a'].append(player[14].text)
        dict_res['spieler5a'].append(player[15].text)
        dict_res['spieler6a'].append(player[16].text)
        dict_res['spieler7a'].append(player[17].text)
        dict_res['spieler8a'].append(player[18].text)
        dict_res['spieler9a'].append(player[19].text)
        dict_res['spieler10a'].append(player[20].text)
        dict_res['spieler11a'].append(player[21].text)



        #away team SUBSTITUTES
        if len(away_sub) >0:
            dict_res["sub_away_time1"].append(away_sub_time[0])
            dict_res['sub_in_aa1'].append(away_sub_enter[0])
            dict_res['sub_out_aa1'].append(away_sub_out[0])
            
            dict_res["sub_away_time2"].append("")
            dict_res['sub_in_aa2'].append("")
            dict_res['sub_out_aa2'].append("")
            
            dict_res["sub_away_time3"].append("")
            dict_res['sub_in_aa3'].append("")
            dict_res['sub_out_aa3'].append("")
            
            dict_res["sub_away_time4"].append("")
            dict_res['sub_in_aa4'].append("")
            dict_res['sub_out_aa4'].append("")
            
            dict_res["sub_away_time5"].append("")
            dict_res['sub_in_aa5'].append("")
            dict_res['sub_out_aa5'].append("")


        #home scorrer

        if name and len(home_scorer)>0 :
            
            
            dict_res["time1"].append(value[0])
            dict_res['home_scorer1'].append(value1[0])
            dict_res["time2"].append("")
            dict_res['home_scorer2'].append("")
            dict_res["time3"].append("")
            dict_res['home_scorer3'].append("")
            dict_res["time4"].append("")
            dict_res['home_scorer4'].append("")
            dict_res["time5"].append("")
            dict_res['home_scorer5'].append("")
            dict_res["time6"].append("")
            dict_res['home_scorer6'].append("")
            dict_res["time7"].append("")
            dict_res['home_scorer7'].append("")
            dict_res["time8"].append("")
            dict_res['home_scorer8'].append("")
            dict_res["time9"].append("")
            dict_res['home_scorer9'].append("")
            dict_res["time10"].append("")
            dict_res['home_scorer10'].append("")
            dict_res["time11"].append("")
            dict_res['home_scorer11'].append("")
            dict_res["time12"].append("")
            dict_res['home_scorer12'].append("")
            dict_res["time13"].append("")
            dict_res['home_scorer13'].append("")
            dict_res["time14"].append("")
            dict_res['home_scorer14'].append("")
            dict_res["time15"].append("")
            dict_res['home_scorer15'].append("")
            dict_res["time16"].append("")
            dict_res['home_scorer16'].append("")
            dict_res["time17"].append("")
            dict_res['home_scorer17'].append("")
            dict_res["time18"].append("")
            dict_res['home_scorer18'].append("")
            
        else:
            dict_res["time1"].append("")
            dict_res['home_scorer1'].append("")
            dict_res["time2"].append("")
            dict_res['home_scorer2'].append("")
            dict_res["time3"].append("")
            dict_res['home_scorer3'].append("")
            dict_res["time4"].append("")
            dict_res['home_scorer4'].append("")
            dict_res["time5"].append("")
            dict_res['home_scorer5'].append("")
            dict_res["time6"].append("")
            dict_res['home_scorer6'].append("")
            dict_res["time7"].append("")
            dict_res['home_scorer7'].append("")
            dict_res["time8"].append("")
            dict_res['home_scorer8'].append("")
            dict_res["time9"].append("")
            dict_res['home_scorer9'].append("")
            dict_res["time10"].append("")
            dict_res['home_scorer10'].append("")
            dict_res["time11"].append("")
            dict_res['home_scorer11'].append("")
            dict_res["time12"].append("")
            dict_res['home_scorer12'].append("")
            dict_res["time13"].append("")
            dict_res['home_scorer13'].append("")
            dict_res["time14"].append("")
            dict_res['home_scorer14'].append("")
            dict_res["time15"].append("")
            dict_res['home_scorer15'].append("")
            dict_res["time16"].append("")
            dict_res['home_scorer16'].append("")
            dict_res["time17"].append("")
            dict_res['home_scorer17'].append("")
            dict_res["time18"].append("")
            dict_res['home_scorer18'].append("")
            
        #away scorrer
        if bottom_name and  len(away_scorer)>0:    
            dict_res["away_time1"].append(bottom_value[0])
            dict_res['away_scorer1'].append(bot_value1[0])
            dict_res["away_time2"].append("")
            dict_res['away_scorer2'].append("")
            dict_res["away_time3"].append("")
            dict_res['away_scorer3'].append("")
            dict_res["away_time4"].append("")
            dict_res['away_scorer4'].append("")
            dict_res["away_time5"].append("")
            dict_res['away_scorer5'].append("")
            dict_res["away_time6"].append("")
            dict_res['away_scorer6'].append("")
            dict_res["away_time7"].append("")
            dict_res['away_scorer7'].append("")
            dict_res["away_time8"].append("")
            dict_res['away_scorer8'].append("")
            dict_res["away_time9"].append("")
            dict_res['away_scorer9'].append("")
            dict_res["away_time10"].append("")
            dict_res['away_scorer10'].append("")
            dict_res["away_time11"].append("")
            dict_res['away_scorer11'].append("")
            dict_res["away_time12"].append("")
            dict_res['away_scorer12'].append("")
            dict_res["away_time13"].append("")
            dict_res['away_scorer13'].append("")
            dict_res["away_time14"].append("")
            dict_res['away_scorer14'].append("")
            dict_res["away_time15"].append("")
            dict_res['away_scorer15'].append("")
            dict_res["away_time16"].append("")
            dict_res['away_scorer16'].append("")
            dict_res["away_time17"].append("")
            dict_res['away_scorer17'].append("")
            dict_res["away_time18"].append("")
            dict_res['away_scorer18'].append("")
        else:
            dict_res["away_time"].append("")
            dict_res['away_scorer'].append("")
            dict_res["away_time1"].append("")
            dict_res['away_scorer1'].append("")
            dict_res["away_time2"].append("")
            dict_res['away_scorer2'].append("")
            dict_res["away_time3"].append("")
            dict_res['away_scorer3'].append("")
            dict_res["away_time4"].append("")
            dict_res['away_scorer4'].append("")
            dict_res["away_time5"].append("")
            dict_res['away_scorer5'].append("")
            dict_res["away_time6"].append("")
            dict_res['away_scorer6'].append("")
            dict_res["away_time7"].append("")
            dict_res['away_scorer7'].append("")
            dict_res["away_time8"].append("")
            dict_res['away_scorer8'].append("")
            dict_res["away_time9"].append("")
            dict_res['away_scorer9'].append("")
            dict_res["away_time10"].append("")
            dict_res['away_scorer10'].append("")
            dict_res["away_time11"].append("")
            dict_res['away_scorer11'].append("")
            dict_res["away_time12"].append("")
            dict_res['away_scorer12'].append("")
            dict_res["away_time13"].append("")
            dict_res['away_scorer13'].append("")
            dict_res["away_time14"].append("")
            dict_res['away_scorer14'].append("")
            dict_res["away_time15"].append("")
            dict_res['away_scorer15'].append("")
            dict_res["away_time16"].append("")
            dict_res['away_scorer16'].append("")
            dict_res["away_time17"].append("")
            dict_res['away_scorer17'].append("")
            dict_res["away_time18"].append("")
            dict_res['away_scorer18'].append("")
            
        #home yellow card

        if len(yel_value1)>0:
            dict_res['yellowcard_time1'].append(yellow_value[0])
            dict_res['yellowcard1'].append(yel_value1[0])
            dict_res['yellowcard_time2'].append("")
            dict_res['yellowcard2'].append("")
            dict_res['yellowcard_time3'].append("")
            dict_res['yellowcard3'].append("")
            dict_res['yellowcard_time4'].append("")
            dict_res['yellowcard4'].append("")
            dict_res['yellowcard_time5'].append("")
            dict_res['yellowcard5'].append("")
            dict_res['yellowcard_time6'].append("")
            dict_res['yellowcard6'].append("")
            dict_res['yellowcard_time7'].append("")
            dict_res['yellowcard7'].append("")
            dict_res['yellowcard_time8'].append("")
            dict_res['yellowcard8'].append("")
            dict_res['yellowcard_time9'].append("")
            dict_res['yellowcard9'].append("")
            dict_res['yellowcard_time10'].append("")
            dict_res['yellowcard10'].append("")
            dict_res['yellowcard_time11'].append("")
            dict_res['yellowcard11'].append("")
            dict_res['yellowcard_time12'].append("")
            dict_res['yellowcard12'].append("")
            dict_res['yellowcard_time13'].append("")
            dict_res['yellowcard13'].append("")
            dict_res['yellowcard_time14'].append("")
            dict_res['yellowcard14'].append("")
            dict_res['yellowcard_time15'].append("")
            dict_res['yellowcard15'].append("")
            dict_res['yellowcard_time16'].append("")
            dict_res['yellowcard16'].append("")
            dict_res['yellowcard_time17'].append("")
            dict_res['yellowcard17'].append("")
            dict_res['yellowcard_time18'].append("")
            dict_res['yellowcard18'].append("")
        else:
            dict_res['yellowcard_time1'].append("")
            dict_res['yellowcard1'].append("")
            dict_res['yellowcard_time2'].append("")
            dict_res['yellowcard2'].append("")
            dict_res['yellowcard_time3'].append("")
            dict_res['yellowcard3'].append("")
            dict_res['yellowcard_time4'].append("")
            dict_res['yellowcard4'].append("")
            dict_res['yellowcard_time5'].append("")
            dict_res['yellowcard5'].append("")
            dict_res['yellowcard_time6'].append("")
            dict_res['yellowcard6'].append("")
            dict_res['yellowcard_time7'].append("")
            dict_res['yellowcard7'].append("")
            dict_res['yellowcard_time8'].append("")
            dict_res['yellowcard8'].append("")
            dict_res['yellowcard_time9'].append("")
            dict_res['yellowcard9'].append("")
            dict_res['yellowcard_time10'].append("")
            dict_res['yellowcard10'].append("")
            dict_res['yellowcard_time11'].append("")
            dict_res['yellowcard11'].append("")
            dict_res['yellowcard_time12'].append("")
            dict_res['yellowcard12'].append("")
            dict_res['yellowcard_time13'].append("")
            dict_res['yellowcard13'].append("")
            dict_res['yellowcard_time14'].append("")
            dict_res['yellowcard14'].append("")
            dict_res['yellowcard_time15'].append("")
            dict_res['yellowcard15'].append("")
            dict_res['yellowcard_time16'].append("")
            dict_res['yellowcard16'].append("")
            dict_res['yellowcard_time17'].append("")
            dict_res['yellowcard17'].append("")
            dict_res['yellowcard_time18'].append("")
            dict_res['yellowcard18'].append("")
            
        #home red card
        if len(home_red_value)>0:
            dict_res['redcard_time1'].append(home_red_value[0])
            dict_res['redcard1'].append(home_red_value1[0])
            dict_res['redcard_time2'].append("")
            dict_res['redcard2'].append("")
            dict_res['redcard_time3'].append("")
            dict_res['redcard3'].append("")
        else:
            dict_res['redcard_time1'].append("")
            dict_res['redcard1'].append("")
            dict_res['redcard_time2'].append("")
            dict_res['redcard2'].append("")
            dict_res['redcard_time3'].append("")
            dict_res['redcard3'].append("")
            
            
            
        #away yellow_card
        if len(bot_yel_value1)>0:
            dict_res['away_yellowcard_time1'].append(bo_yellow_value[0])
            dict_res['away_yellowcard1'].append(bot_yel_value1[0])
            dict_res['away_yellowcard_time2'].append("")
            dict_res['away_yellowcard2'].append("")
            dict_res['away_yellowcard_time3'].append("")
            dict_res['away_yellowcard3'].append("")
            dict_res['away_yellowcard_time4'].append("")
            dict_res['away_yellowcard4'].append("")
            dict_res['away_yellowcard_time5'].append("")
            dict_res['away_yellowcard5'].append("")
            dict_res['away_yellowcard_time6'].append("")
            dict_res['away_yellowcard6'].append("")
            dict_res['away_yellowcard_time7'].append("")
            dict_res['away_yellowcard7'].append("")
            dict_res['away_yellowcard_time8'].append("")
            dict_res['away_yellowcard8'].append("")
            dict_res['away_yellowcard_time9'].append("")
            dict_res['away_yellowcard9'].append("")
            dict_res['away_yellowcard_time10'].append("")
            dict_res['away_yellowcard10'].append("")
            dict_res['away_yellowcard_time11'].append("")
            dict_res['away_yellowcard11'].append("")
            dict_res['away_yellowcard_time12'].append("")
            dict_res['away_yellowcard12'].append("")
            dict_res['away_yellowcard_time13'].append("")
            dict_res['away_yellowcard13'].append("")
            dict_res['away_yellowcard_time14'].append("")
            dict_res['away_yellowcard14'].append("")
            dict_res['away_yellowcard_time15'].append("")
            dict_res['away_yellowcard15'].append("")
            dict_res['away_yellowcard_time16'].append("")
            dict_res['away_yellowcard16'].append("")
            dict_res['away_yellowcard_time17'].append("")
            dict_res['away_yellowcard17'].append("")
            dict_res['away_yellowcard_time18'].append("")
            dict_res['away_yellowcard18'].append("")
        else:
            dict_res['away_yellowcard_time1'].append("")
            dict_res['away_yellowcard1'].append("")
            dict_res['away_yellowcard_time2'].append("")
            dict_res['away_yellowcard2'].append("")
            dict_res['away_yellowcard_time3'].append("")
            dict_res['away_yellowcard3'].append("")
            dict_res['away_yellowcard_time4'].append("")
            dict_res['away_yellowcard4'].append("")
            dict_res['away_yellowcard_time5'].append("")
            dict_res['away_yellowcard5'].append("")
            dict_res['away_yellowcard_time6'].append("")
            dict_res['away_yellowcard6'].append("")
            dict_res['away_yellowcard_time7'].append("")
            dict_res['away_yellowcard7'].append("")
            dict_res['away_yellowcard_time8'].append("")
            dict_res['away_yellowcard8'].append("")
            dict_res['away_yellowcard_time9'].append("")
            dict_res['away_yellowcard9'].append("")
            dict_res['away_yellowcard_time10'].append("")
            dict_res['away_yellowcard10'].append("")
            dict_res['away_yellowcard_time11'].append("")
            dict_res['away_yellowcard11'].append("")
            dict_res['away_yellowcard_time12'].append("")
            dict_res['away_yellowcard12'].append("")
            dict_res['away_yellowcard_time13'].append("")
            dict_res['away_yellowcard13'].append("")
            dict_res['away_yellowcard_time14'].append("")
            dict_res['away_yellowcard14'].append("")
            dict_res['away_yellowcard_time15'].append("")
            dict_res['away_yellowcard15'].append("")
            dict_res['away_yellowcard_time16'].append("")
            dict_res['away_yellowcard16'].append("")
            dict_res['away_yellowcard_time17'].append("")
            dict_res['away_yellowcard17'].append("")
            dict_res['away_yellowcard_time18'].append("")
            dict_res['away_yellowcard18'].append("")
            
        #away red card
        if len(away_red_value)>0 and  away_red_value1:
            dict_res['away_redcard_time1'].append(away_red_value[0])
            dict_res['away_redcard1'].append(away_red_value1[0])
            dict_res['away_redcard_time2'].append("")
            dict_res['away_redcard2'].append("")
            dict_res['away_redcard_time3'].append("")
            dict_res['away_redcard3'].append("")
        else:
            dict_res['away_redcard_time1'].append("")
            dict_res['away_redcard1'].append("")
            dict_res['away_redcard_time2'].append("")
            dict_res['away_redcard2'].append("")
            dict_res['away_redcard_time3'].append("")
            dict_res['away_redcard3'].append("")



        df_res = pd.DataFrame(dict_res)



        #update home_sub
        if len(home_sub) >1:
            df_res['sub_in_a2']=sub_enter[1]
            df_res['sub_out_a2']=sub_out[1]
            
            
        if len(home_sub) >2:
            df_res['sub_in_a3']=sub_enter[2]
            df_res['sub_out_a3']=sub_out[2]
            
            
        if len(home_sub) >3:
            df_res['sub_in_a4']=sub_enter[3]
            df_res['sub_out_a4']=sub_out[3]
            
        if len(home_sub) >4:
            df_res['sub_in_a5']=sub_enter[4]
            df_res['sub_out_a5']=sub_out[4]

        #update sub time
        if len(sub_time) >1:
            df_res['sub_time2']=sub_time[1]
        if len(sub_time) >2:
            df_res['sub_time3']=sub_time[2]
        if len(sub_time) >3:
            df_res['sub_time4']=sub_time[3]
        if len(sub_time) >4:
            df_res['sub_time5']=sub_time[4]


        #update away_sub    
        if len(away_sub) >1:
            df_res['sub_in_aa2']=away_sub_enter[1]
            df_res['sub_out_aa2']=away_sub_out[1]
            
            
        if len(away_sub) >2:
            df_res['sub_in_aa3']=away_sub_enter[2]
            df_res['sub_out_aa3']=away_sub_out[2]
            
        if len(away_sub) >3:
            df_res['sub_in_aa4']=away_sub_enter[3]
            df_res['sub_out_aa4']=away_sub_out[3]
        if len(away_sub) >4:
            df_res['sub_in_aa5']=away_sub_enter[4]
            df_res['sub_out_aa5']=away_sub_out[4]

        #update away_sub time
        if len(away_sub_time) >1:
            
            df_res['sub_away_time2']=away_sub_time[1]
        if len(away_sub_time) >2:
            df_res['sub_away_time3']=away_sub_time[2]
        if len(away_sub_time) >3:
            df_res['sub_away_time4']=away_sub_time[3]
        if len(away_sub_time) >4:
            df_res['sub_away_time5']=away_sub_time[4]
        #update home scorer
        if len(value1) >1:
            df_res['home_scorer2']=value1[1]
        if len(value1) >2:
            df_res['home_scorer3']=value1[2]
        if len(value1) >3:
            df_res['home_scorer4']=value1[3]
        if len(value1) >4:
            df_res['home_scorer5']=value1[4]
        if len(value1) >5:
            df_res['home_scorer6']=value1[5]
        if len(value1) >6:
            df_res['home_scorer7']=value1[6]
        if len(value1) >7:
            df_res['home_scorer8']=value1[7]
        if len(value1) >8:
            df_res['home_scorer9']=value1[8]
        if len(value1) >9:
            df_res['home_scorer10']=value1[9]
        if len(value1) >10:
            df_res['home_scorer11']=value1[10]
        if len(value1) >11:
            df_res['home_scorer12']=value1[11]
        if len(value1) >12:
            df_res['home_scorer13']=value1[12]
            
        #update _Time
        if len(value) >1:
            df_res['time2']=value[1]
        if len(value) >2:
            df_res['time3']=value[2]
        if len(value) >3:
            df_res['time4']=value[3]
        if len(value) >4:
            df_res['time5']=value[4]
        if len(value) >5:
            df_res['time6']=value[5]
        if len(value) >6:
            df_res['time7']=value[6]
        if len(value) >7:
            df_res['time8']=value[7]
        if len(value) >8:
            df_res['time9']=value[8]
        if len(value) >9:
            df_res['time10']=value[9]
        if len(value) >10:
            df_res['time11']=value[10]
        if len(value) >11:
            df_res['time12']=value[11]
        if len(value) >12:
            df_res['time13']=value[12]



        #update away_scorer  #bottom_value
        if len(bot_value1) >1:
            df_res['away_scorer2']=bot_value1[1]
        if len(bot_value1) >2:
            df_res['away_scorer3']=bot_value1[2]
        if len(bot_value1) >3:
            df_res['away_scorer4']=bot_value1[3]
        if len(bot_value1) >4:
            df_res['away_scorer5']=bot_value1[4]
        if len(bot_value1) >5:
            df_res['away_scorer6']=bot_value1[5]
        if len(bot_value1) >6:
            df_res['away_scorer7']=bot_value1[6]
        if len(bot_value1) >7:
            df_res['away_scorer8']=bot_value1[7]
        if len(bot_value1) >8:
            df_res['away_scorer9']=bot_value1[8]
        if len(bot_value1) >9:
            df_res['away_scorer10']=bot_value1[9]
        if len(bot_value1) >10:
            df_res['away_scorer11']=bot_value1[10]
        if len(away_scorer) >11:
            df_res['away_scorer12']=away_scorer[11]
        if len(away_scorer) >12:
            df_res['away_scorer13']=away_scorer[12]
            
        #away time update    
        if len(bottom_value) >1:
            df_res['away_time2']=bottom_value[1]
        if len(bottom_value) >2:
            df_res['away_time3']=bottom_value[2]
        if len(bottom_value) >3:
            df_res['away_time4']=bottom_value[3]
        if len(bottom_value) >4:
            df_res['away_time5']=bottom_value[4]
        if len(bottom_value) >5:
            df_res['away_time6']=bottom_value[5]
        if len(bottom_value) >6:
            df_res['away_time7']=bottom_value[6]
        if len(bottom_value) >7:
            df_res['away_time8']=bottom_value[7]
        if len(bottom_value) >8:
            df_res['away_time9']=bottom_value[8]
        if len(bottom_value) >9:
            df_res['away_time10']=bottom_value[9]
        if len(bottom_value) >10:
            df_res['away_time11']=bottom_value[10]
        if len(bottom_value) >11:
            df_res['away_time12']=bottom_value[11]
        if len(bottom_value) >12:
            df_res['away_time13']=bottom_value[12]
            
        #update home_yellow_card    

        if len(yel_value1) >1:
            df_res['yellowcard2']=yel_value1[1]
        if len(yel_value1) >2:
            df_res['yellowcard3']=yel_value1[2]
        if len(yel_value1) >3:
            df_res['yellowcard4']=yel_value1[3]
        if len(yel_value1) >4:
            df_res['yellowcard5']=yel_value1[4]
        if len(yel_value1) >5:
            df_res['yellowcard6']=yel_value1[5]
        if len(yel_value1) >6:
            df_res['yellowcard7']=yel_value1[6]
        if len(yel_value1) >7:
            df_res['yellowcard8']=yel_value1[7]
        if len(yel_value1) >8:
            df_res['yellowcard9']=yel_value1[8]
        if len(ycard_name) >9:
            df_res['yellowcard10']=ycard_name[9]
        if len(yel_value1) >10:
            df_res['yellowcard11']=yel_value1[10]
        if len(yel_value1) >11:
            df_res['yellowcard12']=yel_value1[11]
        if len(yel_value1) >12:
            df_res['yellowcard13']=yel_value1[12]
            
            
        #update home yellow card time
        if len(yellow_value) >1:
            df_res['yellowcard_time2']=yellow_value[1]
        if len(yellow_value) >2:
            df_res['yellowcard_time3']=yellow_value[2]
        if len(yellow_value) >3:
            df_res['yellowcard_time4']=yellow_value[3]
        if len(yellow_value) >4:
            df_res['yellowcard_time5']=yellow_value[4]
        if len(yellow_value) >5:
            df_res['yellowcard_time6']=yellow_value[5]
        if len(yellow_value) >6:
            df_res['yellowcard_time7']=yellow_value[6]
        if len(yellow_value) >7:
            df_res['yellowcard_time8']=yellow_value[7]
        if len(yellow_value) >8:
            df_res['yellowcard_time9']=yellow_value[8]
        if len(ycard_name) >9:
            df_res['yellowcard_time10']=yellow_value[9]
        if len(yellow_value) >10:
            df_res['yellowcard_time11']=yellow_value[10]
        if len(yellow_value) >11:
            df_res['yellowcard_time12']=yellow_value[11]
        if len(yellow_value) >12:
            df_res['yellowcard_time13']=yellow_value[12]    

        #update away_yellow card
        if len(bot_yel_value1) >1:
            df_res['away_yellowcard2']=bot_yel_value1[1]
        if len(bot_yel_value1) >2:
            df_res['away_yellowcard3']=bot_yel_value1[2]
        if len(bot_yel_value1) >3:
            df_res['away_yellowcard4']=bot_yel_value1[3]
        if len(bot_yel_value1) >4:
            df_res['away_yellowcard5']=bot_yel_value1[4]
        if len(bot_yel_value1) >5:
            df_res['away_yellowcard6']=bot_yel_value1[5]
        if len(bot_yel_value1) >6:
            df_res['away_yellowcard7']=bot_yel_value1[6]
        if len(bot_yel_value1) >7:
            df_res['away_yellowcard8']=bot_yel_value1[7]
        if len(bot_yel_value1) >8:
            df_res['away_yellowcard9']=bot_yel_value1[8]
        if len(bot_yel_value1) >9:
            df_res['away_yellowcard10']=bot_yel_value1[9]
        if len(bot_yel_value1) >10:
            df_res['away_yellowcard11']=bot_yel_value1[10]
        if len(bot_yel_value1) >11:
            df_res['away_yellowcard12']=bot_yel_value1[11]
        if len(bot_yel_value1) >12:
            df_res['away_yellowcard13']=bot_yel_value1[12]


        #update away time
        if len(bo_yellow_value) >1:
            df_res['away_yellowcard_time2']=bo_yellow_value[1]
        if len(bo_yellow_value) >2:
            df_res['away_yellowcard_time3']=bo_yellow_value[2]
        if len(bo_yellow_value) >3:
            df_res['away_yellowcard_time4']=bo_yellow_value[3]
        if len(bo_yellow_value) >4:
            df_res['away_yellowcard_time5']=bo_yellow_value[4]
        if len(bo_yellow_value) >5:
            df_res['away_yellowcard_time6']=bo_yellow_value[5]
        if len(bo_yellow_value) >6:
            df_res['away_yellowcard_time7']=bo_yellow_value[6]
        if len(bo_yellow_value) >7:
            df_res['away_yellowcard_time8']=bo_yellow_value[7]
        if len(bo_yellow_value) >8:
            df_res['away_yellowcard_time9']=bo_yellow_value[8]
        if len(bo_yellow_value) >9:
            df_res['away_yellowcard_time10']=bo_yellow_value[9]
        if len(bo_yellow_value) >10:
            df_res['away_yellowcard_time11']=bo_yellow_value[10]
        if len(bo_yellow_value) >11:
            df_res['away_yellowcard_time12']=bo_yellow_value[11]
        if len(bo_yellow_value) >12:
            df_res['away_yellowcard_time13']=bo_yellow_value[12]    



        #update home red card player
        if len(home_red_value)>1:
            dict_res['redcard2']=home_red_value1[1]
        if len(home_red_value)>2:
            dict_res['redcard3']=home_red_value1[2]
            
        #udpate home red card time
        if len(home_red_value1)>1:
            dict_res['redcard_time2']=home_red_value[1] 
        if len(home_red_value1)>2:
            dict_res['redcard_time3']=home_red_value[2] 
            
        #update away red card player

        if len(away_red_value1)>1:
            dict_res['away_redcard_time2']=away_red_value1[1]
        if len(away_red_value1)>2:
            dict_res['away_redcard_time3']=away_red_value1[2]
            # dict_res['away_redcard1'].append(away_red_value1[1])

        #update away red card player time
        if len(away_cardtime)>1:
            dict_res['away_redcard2']=away_red_value[1]

        if len(away_cardtime)>2:
            dict_res['away_redcard3']=away_red_value[2]
            
            
        #update date  
        
        if q==0:
            print("enter")
            df_res.to_csv('scrap221253334445.csv',mode='a', header=True)
        else:
            print("enter3")
            df_res.to_csv('scrap221253334445.csv',mode='a', header=False)


