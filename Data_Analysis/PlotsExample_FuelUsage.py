import matplotlib.pyplot as plt # Graphs
import pandas as pd #Data analysis
import numpy as np #Numerical calculations.

fuel = pd.read_csv("fuel_usage.csv")
fifa = pd.read_csv("fifa_data.csv")

# print(fifa.head(10))
# print(fuel)

# plt.plot(fuel.Year, fuel.USA, 'b.-', label="United States")
# plt.plot(fuel.Year, fuel.Canada, 'r.-', label="Canada")
# plt.plot(fuel.Year, fuel['South Korea'], 'g.-', label="South Korea")
# plt.plot(fuel.Year, fuel.Australia, 'y.-', label="Australia")

# filter = ['Australia', 'USA', 'Canada', 'South Korea', 'France']
# for country in fuel:
#     if country in filter:
#         plt.plot(fuel.Year, fuel[country], marker='.', label=country)
#
# plt.title("Fuel Prices over Time(Since 1990) in USD")
# plt.xticks(fuel.Year[::3])
# plt.xlabel('Year')
# plt.ylabel("US Dollars")
# plt.legend()
# plt.show()

#########################FIFA Data Visualization##############################
#histogram example
# bins = [40, 50, 60, 70, 80,90, 100] #bins defines the column structure of the Histogram.
# plt.figure(figsize=(8,5))
# plt.hist(fifa.Overall, color='red', bins=bins)
# plt.xlabel("Skill levels")
# plt.ylabel("Number of players")
# plt.xticks(bins)
# plt.title("Distribution of Player skills in FIFA 2020")
# plt.show()

###############Top 10 players in overall rating##################
# top_players = fifa.nlargest(20, 'Overall')
# plt.figure(figsize=(8,6))
# plt.bar(top_players['Name'], top_players['Overall'], color='skyblue')
# plt.xlabel("Rating")
# plt.title("Top 10 FIFA Players by overall rating")
# plt.show()

######################Player positioning graph######################
# position_counts = fifa['Position'].value_counts()
# plt.pie(position_counts, labels=position_counts.index, autopct='%1.1f%%')
# plt.title("Distribution of players by position")
# plt.show()

##########################Scatter plots for comparing skills vs.ratings###############
# plt.figure(figsize=(10,10))
# plt.scatter(fifa['SlidingTackle'], fifa['Overall'])
# plt.title("SlidingTackle vs. Rating")
# plt.xlabel("Skill Moves")
# plt.ylabel("Rating")
# plt.show()
###################Create a pie chart for players with left and right foot comparision
# left = fifa[fifa['Preferred Foot'] == 'Left'].count()[0]
# right = fifa[fifa['Preferred Foot'] == 'Right'].count()[0]
# plt.figure(figsize=(10,10))
# labels =['left', 'right']
# colors =['red', 'blue']
#
# plt.pie([left, right], labels=labels, colors=colors, autopct='%.1f %%' )
# plt.show()

######################pie chart example 2#############################
plt.figure(figsize=(8,5), dpi=100)

fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

weights = [light,light_medium, medium, medium_heavy, heavy]
label = ['under 125', '125-150', '150-175', '175-200', 'over 200']
explode = (.4,.2,0,0,.4)

plt.title('Weight of Professional Soccer Players (lbs)')

plt.pie(weights, labels=label, explode=explode, pctdistance=0.8,autopct='%.2f %%')
plt.show()