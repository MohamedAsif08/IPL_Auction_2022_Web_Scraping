import pandas as pd
import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.iplt20.com/auction/2022"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Team
    team_table = soup.find_all('table', class_="ih-td-tab auction-tbl")[0]
    titles1 = team_table.find_all('th')
    title_list = []
    for title in titles1:
        title_list.append(title.text)
    data = team_table.find_all('tr')
    team_list = []
    for team in data[1:]:
        RF = team.find_all('td')[1].text.replace("₹", "")
        OP = team.find_all('td')[2].text
        TP = team.find_all('td')[3].text
        team_list.append([team.find('h2').text, RF, OP, TP])
    Team_tb = pd.DataFrame(team_list, columns=title_list, index = [x for x in range(1,len(team_list)+1)])
    Team_tb.to_csv('Team.csv')
    print(Team_tb)

    # Top Buyers
    top_buyer_table = soup.find_all('table', class_="ih-td-tab auction-tbl")[1]
    title_table = top_buyer_table.find('tr', class_="ih-pt-tbl")
    titles = title_table.find_all('th')
    title_list = []
    for title in titles:
        title_list.append(title.text)
    data = top_buyer_table.find('tbody', id="pointsdata")
    rows = data.find_all('tr')
    top_buy_list = []
    for row in rows:
        rows_data = row.find_all('td')
        team = row.find('h2').text
        player = rows_data[1].text
        p_type = rows_data[2].text
        price = rows_data[3].text.replace("₹", "")
        top_buy_list.append([team, player, p_type, price])
    Top_buy_tb = pd.DataFrame(top_buy_list, columns=title_list,index=[x for x in range(1,len(top_buy_list)+1)])
    Top_buy_tb.to_csv('Top_Buy.csv')

except Exception as Error:
    print(Error)

