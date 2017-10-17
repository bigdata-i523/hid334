### Fantasy Football Production Visualization 
* Mainly to familiarize myself with the Seaborn graphing library, this script will pull in the most recent fantasy football data and graph a player's production against their opportunities (touches). 
* The data source is http://fftoday.com/ and the top 50 RBs and WRs are used
* TODO: 
  * Combine the results to see how different the slope is between the different types of players
  * Graph text box labeling as a relative reference and not absolute
  * TEs don't have Att on site - add functionality for that
  * Find a way to highlight individual data points with Seaborn

#### URLs for the different positions (included in the code as well):
* RB: http://fftoday.com/stats/playerstats.php?Season=2017&GameWeek=Season&PosID=20&LeagueID=
* WR: http://fftoday.com/stats/playerstats.php?Season=2017&GameWeek=Season&PosID=30&LeagueID=
* TE: http://fftoday.com/stats/playerstats.php?Season=2017&GameWeek=Season&PosID=40&LeagueID=

#### Running Back (through Week 6): 

![untitled](https://user-images.githubusercontent.com/31293179/31685235-3c376f1c-b350-11e7-93ce-f5d5b612d24f.png)

#### Wide Receiver (through Week 6): 

![untitled_2](https://user-images.githubusercontent.com/31293179/31685236-3c40a6ea-b350-11e7-98d1-941f18ef6ab2.png)


#### Tight End (through Week 6): 

![untitled3](https://user-images.githubusercontent.com/31293179/31685237-3c4a4f92-b350-11e7-99bb-9dc05fc3465f.png)
