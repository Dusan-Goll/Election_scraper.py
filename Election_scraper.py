"""
Election_scraper.py: third project to Engeto Online Python Academy

author: Dušan Goll
email: d.goll@seznam.cz
"""

import csv
import sys
import os

import requests
from bs4 import BeautifulSoup


def check_num_of_args(file_args):
    if len(file_args) not in range(3, 4):
        print('WRONG NUMBER OF ARGUMENTS!\n'
              'Must be given exactly 2 arguments when opening Election_scraper.py')
        quit()


def check_first_arg(first_arg):
    districts_url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    dist_html = requests.get(districts_url)
    dist_soup = BeautifulSoup(dist_html.text, 'html.parser')

    def iterate_td_headers():
        res_list = []
        tables_count = len(dist_soup.find_all('table', {'class': 'table'}))
        for i in range(1, tables_count + 1):
            res_list.extend(dist_soup.find_all('td', {'headers': f't{i}sa3'}))
        return res_list

    td_tags = iterate_td_headers()
    dist_list = ["https://volby.cz/pls/ps2017nss/" + (td_tag.a['href'])
                 for td_tag in td_tags]
    if first_arg not in dist_list:
        print('WRONG DISTRICT WEB LINK GIVEN.\n'
              'Try here: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ\n'
              'select some "X" of column "Výběr obce" and copy page link.')
        quit()


def region_soup():
    url = sys.argv[1]
    page_of_region = requests.get(url)
    return BeautifulSoup(page_of_region.text, 'html.parser')


def file_name():
    div_topline = region_soup().find('div', {'class': 'topline'})
    region_name_tag = div_topline.find_all('h3')[1]
    region_name_raw = region_name_tag.text
    region_name = region_name_raw.strip().lstrip('Okres: ')
    return f"results_{region_name}.csv"


def check_second_arg(sec_arg, name_of_file):
    if sec_arg != name_of_file:
        print("WRONG CSV FILE NAME GIVEN.\n"
              "Must be in format: 'results_<district_name>.csv'")
        quit()


def townships():
    div_inner = region_soup().find('div', {'id': 'inner'})
    tr_tags = div_inner.find_all('tr')
    return tr_tags


def stats(_tr_tag_, _town_tag_):
    link_tag = _tr_tag_.find('td', {'class': 'cislo'})
    town_link_tag = link_tag.a

    def town_soup(__town_link_tag__):
        town_link = __town_link_tag__["href"]
        town_url = f'https://volby.cz/pls/ps2017nss/{town_link}'
        page_of_town = requests.get(town_url)
        return BeautifulSoup(page_of_town.text, 'html.parser')

    def basic_stats(__town_tag__, _town_link_tag_):
        div_tag = town_soup(_town_link_tag_).find('div', {'id': 'publikace'})
        voters_stats = div_tag.table.find_all('td')

        town = __town_tag__.text
        town_code = _town_link_tag_.text
        voters = voters_stats[3].text
        envelopes = voters_stats[4].text
        valid_votes = voters_stats[7].text

        return {'code': town_code, 'town': town, 'voters': voters,
                'envelopes': envelopes, 'valid votes': valid_votes}

    def political_parties():
        div_inner = town_soup(town_link_tag).find('div', {'id': 'inner'})
        parties = [tag.text for tag in (div_inner.find_all
                                        ('td', {'class': 'overflow_name'}))]
        votes_1 = [tag.text for tag in (div_inner.find_all
                                        ('td', {'headers': 't1sa2 t1sb3'}))]
        votes_2 = [tag.text for tag in (div_inner.find_all
                                        ('td', {'headers': 't2sa2 t2sb3'}))]
        votes_for_parties = votes_1 + votes_2
        parties_and_votes = {parties[i]: votes_for_parties[i]
                             for i in range(len(parties))}
        return parties_and_votes

    stats_dict = {}
    stats_dict.update(basic_stats(_town_tag_, town_link_tag))
    stats_dict.update(political_parties())
    return stats_dict


def save_to_file(_stats_dict_):
    file = open(file_name(), mode='a', newline='\n')
    first_line = list(_stats_dict_.keys())
    writer = csv.DictWriter(file, first_line)
    if os.path.getsize(file_name()) == 0:
        writer.writeheader()
    else:
        writer.writerow(_stats_dict_)
    file.close()


def data_download_and_save():
    for i, tr_tag in enumerate(townships()):
        percentage = round((i + 1) * (100 / len(townships())), 1)
        os.system('cls')
        print(f"DOWNLOADING DATA FROM GIVEN URL: {sys.argv[1]}'\n"
              f"Downloading: {percentage:>5}%")
        town_tag = tr_tag.find('td', {'class': 'overflow_name'})
        if town_tag is None:
            continue
        else:
            save_to_file(stats(tr_tag, town_tag))


os.system('cls')
print('CHECKING URL AND FILE NAME')
check_num_of_args(sys.argv)
check_first_arg(sys.argv[1])
check_second_arg(sys.argv[2], file_name())

create_file = open(file_name(), mode='w')
create_file.close()

os.system('cls')
print(f'DOWNLOADING DATA FROM GIVEN URL: {sys.argv[1]}')
data_download_and_save()
print(f'DATA SUCCESSFULLY DOWNLOADED AND SAVED TO "{file_name()}"\n'
      'CLOSING Election_scraper.py')
