# report.py
#
# Exercise 2.4

#!/usr/bin/env python3
# report.py

import csv
import sys

import fileparse
import stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):	
 
# 	fields=['name', 'shares', 'price']
# 	types=[str,int,float]
	with open(filename) as lines:
		port=Portfolio.from_csv(lines)
# 		portdicts= fileparse.parse_csv(lines, columnlist=[*fields], has_headers=True, types=[*types], **opts)
# 		portfolio=[stock.Stock(**d) for d in portdicts]
# 		return Portfolio(portfolio)
		return port

def read_prices(filename):
	with open(filename) as lines:
		return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

		

def compute_gains_losses(portfolio_filename, prices_filename):
	prices={}
	portfolio=[]
	
	prices=read_prices(prices_filename)
	portfolio=read_portfolio(portfolio_filename)
	total_gain_loss = 0.0
	total_value=0.0
	
	for s in portfolio:
		#print("this one:", s['name'], s['shares'], s['price'])
		try:
			name=s.name
			shares=s.shares
			price_paid=s.price
			
			current_price = float(prices[name])
			current_value = round(current_price * shares, 2)
			gain_loss = round(shares * (current_price - price_paid), 2)
			
			print("name:", name)
			print("shares:", shares)
			print("price_paid:", price_paid)
			print("current_price:", current_price)
			print("current_value:", current_value)
			print("gain_loss:", gain_loss)
			print("")

			
			total_gain_loss += gain_loss
			total_value += current_value
		except KeyError:
			print("Couldn't parse row", name, shares, price_paid)
			
# 	print("Total Value:", total_value)
# 	print("Total gain/(loss):", total_gain_loss)
	return portfolio
	

def make_report(portfolio, prices):
	report=[]


	for s in portfolio:

		holding={}
		try:
			name=s.name
			shares=s.shares
			price_paid=s.price
			current_price= float(prices[name])
			change=current_price - price_paid
	
			holding=(name, shares, current_price, change)
				
			report.append(holding)
		except KeyError:
			print("Couldn't parse stock", s)
			
	return report
				
  
def print_report(portfolio_filename, prices_filename, fmt='txt'):
	portfolio=read_portfolio(portfolio_filename)
	prices=read_prices(prices_filename)
	
	report=make_report(portfolio, prices)
	
	formatter=tableformat.create_formatter(fmt)
	formatter.headings(['Name','Shares','Price','Change'])
	
	
	for name, shares, price, change in report:
		rowdata=[name, str(shares), f'{price:0.2f}',f'{change:0.2f}']
		formatter.row(rowdata)
  	
	
def main(args):	
	if len(args)==3:
	  portfolio_filename=args[1]
	  prices_filename=args[2]
	else:
	  portfolio_filename="Data/portfolio.csv"
	  prices_filename="Data/prices.csv"
	  
	import logging
	logging.basicConfig(
		filename='app.log',
		filemode='w',
		level=logging.WARNING
		)
	  
	print_report(portfolio_filename, prices_filename)
	
if __name__ == '__main__':	
	if len(sys.argv) !=3:
		raise SystemExit(f'Usage: {sys.argv[0]}' ' portfolio pricefile')
		
	main(sys.argv)
	  	
  	
