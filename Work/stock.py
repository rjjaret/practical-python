from typedproperty import String, Integer, Float

class Stock:

# 	name = String('name')
# 	shares = Integer('shares')
# 	price = Float('price')

	__slots__=('name', 'shares', 'price')
	
	def __init__(self, name, shares, price):
		self.name=  String('name') 
		self.shares= String('shares')
		self.price= String('price')
		
		self.name = name
		self.shares = shares
		self.price = price
		
		
		
	@property
	def cost(self):
		return self.shares * self.price	
	
	def sell(self, noShares):
		self.shares-=noShares
		
	def __repr__(self):
		return f'Stock: ({self.name}, {self.shares}, {self.price})'