import json

from product_db import product_db
from sale_order_db import sale_order_db

def make_dict(queryset, dict_value_attr, dict_key):
	dictionary = {}

	# Write your solution here:

	return dictionary

# Create a function that convert a list of dictionaries into a custom dictionary.
# The output dictionary will have it's keys and values defined by the developer through function's input.
# For example, it will convert the variable a to b:
a = [
	{'product_id': 188086, 'full_price': 69.0, 'gross_cost': 33.15},
	{'product_id': 188027, 'full_price': 89.9, 'gross_cost': 33.58}
]
# b = make_dict(a, ['full_price'], 'product_id')
b = {
	188086: 69.0,
	188027: 89.9
}
# other example:
# c = make_dict(a, ['full_price', 'gross_cost'], 'product_id')
c = {
	188086: {
		'full_price': 69.0,
		'gross_cost': 33.15
	},
	188027: {
		'full_price': 89.9,
		'gross_cost': 33.58
	}
}
# other example:
# c = make_dict(a, None, 'product_id')
c = {
	188086: {
		'product_id': 188086,
		'full_price': 69.0,
		'gross_cost': 33.15
	},
	188027: {
		'product_id': 188027,
		'full_price': 89.9,
		'gross_cost': 33.58
	}
}

product_db_five_items = product_db[0:4]
print(json.dumps(make_dict(product_db_five_items, ['full_price'], 'product_id'), indent=4))
print(json.dumps(make_dict(product_db_five_items, ['full_price', 'gross_cost'], 'product_id'), indent=4))
print(json.dumps(make_dict(product_db_five_items, None, 'product_id'), indent=4))

sale_order_db_five_items = sale_order_db[0:4]
print(json.dumps(make_dict(sale_order_db_five_items, ['customer_id', 'purchased_products', 'is_canceled'], 'sale_order_id'), indent=4))