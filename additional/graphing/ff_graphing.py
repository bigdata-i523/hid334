import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import numpy as np
import statsmodels.api as sm

#Download the fantasy data
http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

main_site = 'http://fftoday.com/stats/playerstats.php?Season=2017&GameWeek=Season&PosID=30&LeagueID='

response = http.request('GET', main_site)
soup = BeautifulSoup(response.data,'lxml')

page_type = [i.get_text() for i in soup.select('.pageheader')][0][:-11]
df_headers = []
print(page_type)

#Stat table headers - the ones we care about are 'G','Att','Target','FPts/G'
fields = soup.select('b')

for field in fields: 
	df_headers.append(field.get_text()) 

# Of the tables on the page, this is the one with the player data
table = soup.find_all('table')[3]
output = pd.DataFrame(columns = df_headers, index = ['Player'])

# Read in the names of the players
players = table.findAll("td", {"class" : "sort1","align":"LEFT"})

df_players = []

for player in players: 

	name = player.get_text().split(' ')
	display_name = name[1] + ' ' +  name[2]
	df_players.append(display_name)

# Find the stats
stats = table.findAll("td", {"class" : "sort1","align":"center"})

g_loc = df_headers.index('G') 
att_loc = df_headers.index('Att')
rec_loc = df_headers.index('Rec')
fpt_loc = df_headers.index('FPts')

# This is the jump between data points we need - the data is read in 
# as a single column, so this is basically to re-create the rows 
# Use -1 than the total headers because we already did the player column
# above to remove the formatting on the site

jump = len(df_headers)-1
fields = ['g', 'att', 'rec', 'fpt']
locs = [g_loc, att_loc, rec_loc, fpt_loc] 
summary = {}

for i in range(0,len(fields)):
	summary[fields[i]]=[stats[i].get_text() for i in range(locs[i] - 1,len(stats),jump)]

# Add the player field into the dictionary
summary['player']=df_players

data = pd.DataFrame(summary)
data['touches'] = [int(i)+int(j) for i,j in zip(data['att'], data['rec'])]

#this is needed later because the OLS replaces the column with a constant
data['fpt'] = data['fpt'].apply(pd.to_numeric)
data['pos'] = page_type
graph_data = data[['player','fpt','touches']]


#Making the graph in Seaborn
sns.set()
buffer = 10
g = sns.jointplot(x="touches", y="fpt",data=graph_data, kind = "reg", 
                  xlim=(graph_data.touches.min()-buffer, graph_data.touches.max()+buffer), 
                  ylim=(graph_data.fpt.min()-buffer, graph_data.fpt.max()+buffer))

g.set_axis_labels("Touches", "Fantasy Points")

plt.title('Fantasy Football Production at ' + page_type)

#Find out which players are outperforming or underperforming the most 

data.con = sm.add_constant(data.touches)
model = sm.OLS(data.fpt, data.con, data = data)
results = model.fit()

data['res'] = results.resid

data = data.sort_values('res', ascending = False)

#how many large residuals do you want to highlight?
resid_num = 3

top_resid = data.res.head(resid_num)
bot_resid = data.res.tail(resid_num)

players_to_note = []

allresid = [top_resid,bot_resid]
for i in allresid: 
    for j in i:
        p = data[data.res == j].iloc[0,3] #Player Name
        x = data[data.res == j].iloc[0,5] #Touches
        y = data[data.res == j].iloc[0,1] #Points
        r = data[data.res == j].iloc[0,7] #Residual

        players_to_note.append((p,x,y,r))

#Add the results to the graph
for i in players_to_note: 
    plt.annotate(i[0],xy=(i[1],i[2]),xytext=(i[1],i[2]), ha = 'center', va = 'bottom')

    
#Find the highest scoring player 
data = data.sort_values('fpt', ascending = False)
tp = data.head(1) #tp = Top Player
tp_name = tp.iloc[0,3]
tp_touches = tp.iloc[0,5]
tp_pts = tp.iloc[0,1]

plt.annotate(tp_name,xy=(tp_touches,tp_pts),xytext=(tp_touches,tp_pts),color = 'green', ha = 'center', va = 'bottom')

#TODO: Modify this if you want to display the player names to the right - need 
#to figure out how to make it a relative reference rather than absolute
# inc = 0

# x_align = 75
# y_align = 60

# plt.text(x_align,y_align+15,'Bottom 5:',size = 'large', style = 'oblique')
# for i in players_to_note[5:]: 
#     plt.text(x_align,y_align+inc,i[0])
#     inc += 3

# y_align = y_align -5
# plt.text(x_align,y_align,'Top 5:',size = 'large', style = 'oblique')
# for i in players_to_note[0:5]: 
#     plt.text(x_align,y_align-inc,i[0])
#     inc -= 3

plt.show()
