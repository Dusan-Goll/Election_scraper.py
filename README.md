# Engeto_project_03

Third project to Engeto Python Academy.

## Project description

This project can scrape election data of Czech parliament elections from 2017.

More here: [VOLBY.CZ - výsledky 2017](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Libraries installation
Before you run the project, you need to install a few libraries/packages listed in **requirements.txt** 

I recommend installation to new virtual environment for this project, via pip install manager:

*$ pip3 --version

*$ pip3 install -r requirements.txt

## How to RUN the project

To run project in command prompt -> Election_scraper.py must be executed with 2 arguments:

*$ python Election_scraper.py <selected_district_web_link> <file_name>*

1. argument ... **web link of selected district**, from which you want to download election data, select one of 'X' in column "Výběr obce" from [https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

2. argument ... **file name** in format "results_<selected_district_name>.csv"

After executing the program you will recieve **output in csv file**.

## Example

> **Election results for district _Rychnov nad Kněžnou_:**

1. argument:  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5204

2. argument:  results_Rychnov nad Kněžnou.csv

> **Running the program:**

*$ python Election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5204" "results_Rychnov nad Kněžnou.csv"*

> **example of program processing:**

CHECKING URL AND FILE NAME

DOWNLOADING DATA FROM GIVEN URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5204

Downloading:   1.4%

. . . . . . . . .

Downloading: 100.0%

DATA SUCCESSFULLY DOWNLOADED AND SAVED TO "results_Rychnov nad Kněžnou.csv"

CLOSING Election_scraper.py

> **a bit of output:**

code,town,voters,envelopes,valid votes,Občanská demokratická strana,Řád národa - Vlastenecká unie, . . . 

576085,Bačetín,326,230,226,21,0,0,12,1,8,14,3,3,5,0,2,15,3,9,64,1,2,23,1,0,0,36,3

576093,Bartošovice v Orlických horách,161,115,112,11,0,0,4,0,6,15,2,0,2,0,0,3,1,7,24,0,0,31,0,0,0,6,0

576107,Bílý Újezd,517,356,354,33,1,0,13,0,16,19,1,7,5,0,0,23,0,10,133,0,0,42,0,1,0,49,1

576115,Bohdašín,198,141,140,11,0,0,2,0,6,11,0,0,6,1,0,12,0,8,24,0,0,44,2,0,0,12,1

. . .
