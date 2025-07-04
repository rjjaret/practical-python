# pcost.py
#
# Exercise 1.27

import sys
import report

def portfolio_cost(filename, delimiter=',', has_headers=True):
  
  portfolio=report.read_portfolio(filename)
  
  return portfolio.total_cost


  
def main (args):
	if len(args)==2:
	  filename=args[1]
	else:
	  filename="Data/portfolio.csv"
	  
	cost = portfolio_cost(filename)
	print('Total cost:', "$" + str(cost))
	
if __name__ == '__main__':
	if(len(sys.argv) !=2):
		SystemExit('Usage: ', sys.argv)
	main(sys.argv)
