# 2021 NASA Hackathon
## CHALENGES: No.24 WARMING: THINGS ARE HEATING UP!
### Author: Chia-Lin,Chen(陳佳琳), Meng-Chuan, Lee(李孟娟)



#### Develop Environment: MacBook Pro 2019(13''), Mac OS 11.6
#### Coding Language: Python(3.6.10), HTML, CSS


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
    
