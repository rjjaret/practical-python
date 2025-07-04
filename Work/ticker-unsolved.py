# ticker.py

from follow import follow
import csv
import tableformat	
import report
import time
	
def parse_stock_data(lines):
	rows = csv.reader(lines)
	return rows
	
def select_columns(rows, indices):
	for row in rows:
		yield[row[index] for index in indices]
		
	
def parse_stock_data(lines):
	rows = csv.reader(lines)
	rows= select_columns(rows, [0,1,4])
	rows=convert_types(rows, [str, float, float])
	rows=make_dicts(rows, ['name', 'price', 'change'])
	
	return rows

def convert_types(rows, types):
	for row in rows:
		yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
	for row in rows:
		yield(dict(zip(headers, row)))
		
def filter_symbols(rows, names):
	for row in rows:
		if row['name'] in names:
			yield row
			

# if __name__ == '__main__':
# 	portfolio= report.read_portfolio('Data/portfolio.csv')
# 	rows = parse_stock_data(follow('Data/stocklog.csv'))
# 	print (next(rows))
# 	rows=filter_symbols(rows, portfolio)
# 
# 	for row in rows:
# 		print(row)

	
def ticker(portfile, logfile, fmt):

	portfolio= report.read_portfolio(portfile)
	lines=follow(logfile)
	
	rows = parse_stock_data(follow(lines))
	# 	print (next(rows))
	rows=filter_symbols(rows, portfolio)
	
	# 	for row in rows:
	# 		print(row)
	columns = ['name','price','change']
	formatter = tableformat.create_formatter(fmt)
	# 	print(formatter)
	
	formatter.headings(['name','price','change'])
  #   for row in rows:
#         formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )	
tableformat.print_table(rows, columns, fmt)
	