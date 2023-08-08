import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

today = date.today()
main_url=f"https://greyhoundracingsa.com.au/racing/meetings?state=SA&date=2023-07-07"


#Csv File Generator
def csv_maker(filename,race_number,track_names,new_list, box_data, last5, odds_data, besttime, trait, comment):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["Race Number","Track Name","Dogs_Name", "Box", "LAST 5", "Odds", "Best Time T/D", "S/A Trait", "Comment"])

        for row in zip(race_number,track_names,new_list, box_data, last5, odds_data, besttime, trait, comment):
            filled_row = [value if value else "null" for value in row]
            writer.writerow(filled_row)
            
   
#csv file name       
filename = "DogsRace2.csv"

race_number=[]
track_names=[]
comment_dictionary={}
comment_data=[]
odds_data=[]
box_data=[]
last5=[]
besttime=[]
trait=[]
dogs_name=[]
new_list = []
comment=[]



track_url=main_url

track_response = requests.get(track_url)
track_soup = BeautifulSoup(track_response.text, "html.parser")

dropdown_value=track_soup.find_all("select",{'id':'MeetingsStateSelection'})

for state in dropdown_value:
    option=state.findAll("option")
    for state_name in option:
        
        state_ur1=f"https://greyhoundracingsa.com.au/racing/meetings?state={state_name['value']}&date=2023-07-07"
        
        state_response = requests.get(state_ur1)
        state_soup = BeautifulSoup(state_response.text, "html.parser")


        info=state_soup.find_all("div",{"class":"form-links-cols"})

        for track in info:
            track_name=track.find("a",{"class":"form-link experts"}).get("href")
            

            url = f"https://greyhoundracingsa.com.au{track_name}"
            print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            racing_track=track_name.split("1")[0]

            fields=soup.findAll("span",{"class":"selector-note"})

            for i in range(len(fields)-1):

                url = f"https://greyhoundracingsa.com.au{racing_track}{i+1}"
                
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
    

                #Get Dogs name
                tab=soup.find_all('div',{'id':'CondensedFormTabPanel'})
                for data in tab:
                    if data.findAll('div',{'class':"name-details"}):
                        dog_value= data.findAll("h2")
                for dogs in dog_value:
                    a_tag = dogs.find('a')
                    value = a_tag.text.strip()
              
                    final_val=value.split("(")
                    if final_val:
                        new_list.append(final_val[0])


                #Race number
                
                selected_div = soup.find('div', {'class': 'slider-item race-selector-item d-flex flex-column clickable-card selected'})
                total_race=selected_div.find("span")
               
                if race_number== []:
                    for i in range(len(new_list)):
                        
                        race_number.append(total_race.text)
                        
                else:
                    calculate_length=len(new_list) -len(race_number)
                    for i in range(calculate_length):
                     
                        race_number.append(total_race.text)
                    
               
                # track_Name
                tracks=soup.find_all('div',{'class':'meeting-name-heading'})
            
                for race_track in tracks:
                    matching_track=soup.find("div",{"class":"name hide-in-pdf"})
                    track_data=matching_track.text
                    for i in range(len(new_list)):
                      
                        track_names.append(track_data)
                
                
                analytics_table=soup.find("div", attrs = {'id':"AnalystContents"})
            
                if analytics_table != None:
                    summary_table = soup.find("table", attrs = {'class':'data-table table-striped'})
                    rows = summary_table.findAll("tr")


                    td_elements = soup.find_all("td", attrs={"class":"text-center",'span':None})


                    #GET S/A TRAITS VALUE
                    for i in range(2, len(td_elements), 3):
                        traits = td_elements[i].text.strip()
                        trait.append(traits)


                    #GET BESTTIME VALUE
                    for i in range(1, len(td_elements), 3):
                        time = td_elements[i].text.strip()
                        besttime.append(time)


                    #GET LAST 5 VALUE
                    for data in rows:
                        lastfive=data.find("td",attrs = {'class':'',"colspan": None})
                        
                        if lastfive:
                            last5.append(lastfive.text)
                            
                            
                        #GET BOX VALUE   
                        box=data.find("td",attrs = {'class':'box-col box'})
                        if box:
                            box_value=box.find("img")["src"]
                            box_data.append(box_value)
                            
                            
                        #GET COMMENT VALUE
                        comment=data.find("td", attrs = {'class':'comments-col'})
                        if comment:
                            comment_data.append(comment.text)
                        
                        
                        #GET ODDS VALUE
                        odds=data.find("td",attrs = {'class':'text-center'})
                        if odds:
                            odds_data.append(odds.span.text)
                        

                    comment = [text.strip('\n\r ').strip() for text in comment_data]
                    final_best=[best.strip('\n').strip() for best in besttime]
            if comment == []:
                for i in range(len(new_list)):
                    box_data.append('')
                    last5.append('')
                    odds_data.append('')
                    besttime.append('')
                    trait.append('')
                    comment.append('')
                
            csv_maker(filename,race_number,track_names,new_list,box_data,last5,odds_data,besttime,trait,comment)
            new_list.clear()
            box_data.clear()
            last5.clear()
            odds_data.clear()
            besttime.clear()
            trait.clear()
            comment.clear()
            track_names.clear()
            race_number.clear()
