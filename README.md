# 2021 NASA Hackathon
## CHALENGES: No.24 WARMING: THINGS ARE HEATING UP!
## Author: Chia-Lin,Chen(陳佳琳), Meng-Chuan, Lee(李孟娟)
## Description:

The motivation is saving sea turtles, whose extinct are dominated by temperature. 
Sea turtles' sexulity are affected by temperature. For example, over 31 degrees celsius, almost all turtles will become female.
People know that global warming will let temperature up, to slow down global warming, we can reduce carbon elimination.
To reduce it, we have two ideas, saving whales and forests.
Through protected whales and forests, it can reduce almost 200M tons of carbon.

Poseidon can notice fire forests before they burned, and find  best locations for reservoirs.
(Reservoirs can not only extinguishing but also keep place wet)
Poseidon can point out the routes of whales swimming, to avoid accidental injury by ships.

## Install:

pip freeze > requirements.txt #display packages

pip install -r requirements.txt #install essentials

## Poseidon tool:

### Poseidon default opened on localhost:5000 (or 127.0.0.1:5000 or your_ip:5000)

1. localhos:5000/homepage

![image](homepage.png)

2. localhost:5000/result_Reservoirs

![image](reservoir.png)

3. localhost:5000/FireForests

![image](sendMail.png)

4. localhost:5000/Whales

![image](whalesRoute.png)


* #### Develop Environment: MacBook Pro 2019(13''), Mac OS 11.6
* #### Coding Language: Python(3.6.10), HTML, CSS

Folders:

	root
	
	|-PoseidonAPI

	|-requirements.txt #help install

	|-Main.py #including features: homepage, forests(reservoir and high temperature warning mail, and whales routes.

	|-template

		|-homepage.html

		|-base.html

		|-xxx.html #all extends by base.html

		|-result_xxx.html # display folium maps

	|-static

		|-css #style

		|-fig #picture

	|-PoseidonWebCrawler

		|-CrawlerNASAtemparature.py #crawl NASA temperature data.

		|-crawlTransfer2dataset.py #Transfer original NASA temparature data to new ones.
		
		|-chromedriver # Selenium chrome driver
    
		|-dataset
