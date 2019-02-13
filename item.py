from smartround import to_nearest_cent

class Item:

	def __init__(self, name, cost, exempt = False):

		self.name = name
		self.cost = cost
		self.exempt = exempt
		self.price = cost * (1 if exempt else 1.07)

	def __str__(self):
		
		return self.name, to_nearest_cent(self.price)