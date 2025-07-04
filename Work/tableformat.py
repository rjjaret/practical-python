#Table Formatter

class TableFormatter:
	def headings(self,headers):
		raise NotImplementedError()
	
	
	def row(self,rowdata):
		raise NotImplementedError()	
		
class TextTableFormatter(TableFormatter):		
	def headings(self,headers):
		for h in headers:	 
			print(f'{h:>10s}', end=' ')
		print()
		print(('-' * 10 + ' ') * len(headers))
  
	
	def row(self,rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()		
		
class CSVTableFormatter(TableFormatter):
	def headings(self, headers):
		print(','.join(headers))
		
	def row(self,rowdata):
		print(','.join(rowdata))
		
class HTMLTableFormatter(TableFormatter):
	def headings(self,headers):
		for h in headers:
			print("<tr><th>" + h + "</th></tr>", end='')
		print()
			
	def row(self, rowdata):
		for d in rowdata:
			print("<tr><td>" + d + "</td></tr>", end='')
		print()
	

class FormatException(Exception):
	pass
		
		
def create_formatter(format='txt'):
	if format=='txt':
		formatter=TextTableFormatter()
	elif format=='csv':
		formatter=CSVTableFormatter()
	elif format=='html':
		formatter=HTMLTableFormatter()
	else:
		raise FormatException(f'Unknown format: {format}')
	
	return formatter
		
def print_table(portfolio, columns, formatter):
	formatter.headings(columns)

	for row in portfolio:
		rowdata=[str(getattr(row, colname)) for colname in columns]
	
		formatter.row(rowdata)
