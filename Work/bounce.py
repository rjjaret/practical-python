# bounce.py
#
# Exercise 1.5
height=100 #meters
bounce_pct=3/5
num_bounces=0

while num_bounces <10:
	num_bounces = num_bounces+1;
	height=height*bounce_pct
	print(num_bounces, round(height, 4))
	
