#!/usr/bin/env Python
# -*- coding: utf8 -*-
# webscraper_glassdoor.py
# November 1, 2018
# Glenn Abastillas
# This script will be used to scrape data from www.glassdoor.com
# Design this script for use in a Jupyter Notebook.



"""
Must use this to Attribute Glassdoor for their results:
<a href='https://www.glassdoor.com/index.htm'>powered by 
<img src='https://www.glassdoor.com/static/img/api/glassdoor_logo_80.png' title='Job Search' /></a>

Parameters

Parameter	Explanation												Required?
v			The API version. The current version					Yes
			is 1 except for jobs, which is currently version 1.1
format		Either xml or json as you prefer						Yes
t.p			Your partner id, as assigned by Glassdoor				Yes
t.k			Your partner key, as assigned by Glassdoor				Yes
userip		The IP address of the end user to whom the API 
			results will be shown									Yes
useragent	The User-Agent (browser) of the end user to whom the 	Yes
			API results will be shown. Note that you can can 
			obtain this from the "User-Agent" HTTP request header 
			from the end-user
callback	If json is the requested format, you may specify a 		No
			jsonp callback here, allowing you to make cross-domain 
			calls to the glassdoor API from your client-side 
			javascript. See the JSONP wikipedia entry for more 
			information on jsonp.
action		Must be set to employers								Yes
q			Query phrase to search for - can be any combination 	No
			of employer or occupation, but location should be 
			in l param.
l			Scope the search to a specific location by specifying 	No
			it here - city, state, or country.
city		Scope the search to a specific city by specifying 		No
			it here.
state		Scope the search to a specific state by specifying 		No
			it here.
country		Scope the search to a specific country by specifying 	No
			it here.
pn			Page number to retrieve. Default is 1.					No
ps			Page size, i.e. the number of jobs returned on each 	No
			page of results. Default is 20.

Example URL:
	http://api.glassdoor.com/api/api.htm?
	t.p=5317&t.k=n07aR34Lk3Y&userip=0.0.0.0&useragent=&format=json&v=1&action=employers

Get code for text summarization written by Emily from Sian.
"""

# Initialize
# Define Search Terms
# Ping Glassdoor
# Summarize text
# Create DataFrames


