# fileparse.py
#
# Exercise 3.3

import csv
import logging

log=logging.getLogger(__name__)
logging.basicConfig(
	filename='app.log',
	filemode='a',
	level=logging.WARNING
	)
  

def parse_csv(lines, columnlist=None, types=[], has_headers=True, delimiter=',', silence_errors=False):

	if columnlist and not has_headers:
		raise RuntimeError('columnlist argument requires column headers')
		
	records=[]  
	rows=csv.reader(lines, delimiter=delimiter)

	headers= next(rows) if has_headers else []
	
	if columnlist and headers:
		indices = [headers.index(colname) for colname in columnlist]
		headers=columnlist
	else:
		indices=[]	
	
	for row in rows:
		#print (row)
		if not row:
			continue
	
		if indices:
			row = [row[index] for index in indices]
		
		if types:
			try:	
				#print (row[0], row[1], row[2])
				row = [func(val) for func, val in zip(types, row)]
				#print (row)				
			except (ValueError, TypeError) as e:
				if not silence_errors:
					log.warning("Couldn't convert : %s", row)
					log.debug("Reason : %s", e)
				continue	
			#print(row)				
		if has_headers:
			record = dict(zip(headers, row))      
		else:
			record =  tuple(row)
			
		records.append(record)  	  
	return records
