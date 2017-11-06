from collections import Counter
from heapq import *
from collections import defaultdict
from itertools import chain

with open('C:\\Data Science\\time_machine.txt', 'r') as file:
    full_text = file.read().replace('\n', '')

eligible_text = []
eligible_symbols = [' ',',','.','!','?','\'']


for character in full_text:
 	if character.isalpha() or character in eligible_symbols:
 		eligible_text.append(character.lower())


eligible_text = "this is an example for huffman encoding"

counts = Counter(eligible_text)
counts = sorted(counts.items(), key=lambda v: v[1], reverse=False)
# print(counts)

def add_one(node):
	return '1' + node[1] 

def add_zero(node):
	return '0' + node[1]

# Create list of lists with [node value, [symbol, Huffman code]] from the frequency table
def make_node(symbol): 
	return [symbol[1], [symbol[0], ""]]

# Once the nodes have been put into the min heap, this will return the values below the node of interest
def lower_nodes(node):
	return node[1:]

# Sort the list by length, then by value (smallest Huffman codes first)
def huffman_sort(codes):
	return sorted(codes, key = lambda h: (len(h[1]),h))

def total_bytes_of_symbol(symbol,freq_table):
	return freq_table.get(symbol[0])*len(symbol[1])

# Code implemented from Cormen Introduction to Algorithms (3rd edition) p. 431
def huffman(freq_table):

	n = len(freq_table)
	Q = [make_node(i) for i in freq_table]

	# Create a min heap from this new list of lists
	heapify(Q)
	
	# Go through the frequency table heap until there are no elements left 
	while len(Q) > 1:

		# Take the lowest frequency symbol remaining
		x = heappop(Q)
		# Take the second lowest frequency symbol remaining
		y = heappop(Q)

		z_freq = x[0] + y[0]

		# Assign a 1 to the branch if the symbol is to the right (lowest frequency) and 
		# Assign a 0 if the symbol is to the left (2nd lowest frequency)
		for node in lower_nodes(x):
			# Add the one to the running code for this node
			node[1] = add_zero(node)

		for node in lower_nodes(y):
			# Add the zero to the running code for this node
			node[1] = add_one(node)

		heappush(Q, [z_freq] + (lower_nodes(x)+ lower_nodes(y)) )
		
		# Sort by the smallest Huffman codes for the output (keep only the part with the symbol and code - not root total)
	return huffman_sort(heappop(Q)[1:])

total_bytes = 0
dict_counts = dict(counts)

code_summary = dict()
symbol_bytes = dict()

# Print the results of Huffman coding
for symbol in huffman(counts):
	
	character = symbol[0]
	huffman_code = symbol[1]

	# Show Huffman codes by symbol 
	code_summary[character] = huffman_code

	# Show the bytes of each symbol
	symbol_bytes[character] = total_bytes_of_symbol(symbol, dict_counts)


print('\nSymbol Frequencies:')
for i in sorted(counts, key=lambda v: v[1], reverse=True): 
	print(i)

print('\nHuffman Codes:')
for k,v in code_summary.items():
	print(k + ':' + v)

print('\nBytes by Symbol:')
for k,v in symbol_bytes.items():
	print(k + ':' + str(v))	

total_bytes = sum(symbol_bytes.values())
old_bytes = len(eligible_text)*8

print('\nOriginal Total Bytes:', old_bytes)
print('New Total Bytes:', total_bytes)

print('\n Savings (%): ', '{:.2f}'.format(total_bytes/old_bytes*100))



# 	print(symbol[0] + ':' + symbol[1])

# 	# Show the bytes of each symbol
# 	print(symbol[0]+ ':' + str(total_bytes_of_symbol(symbol, dict_counts)))

# 	# Keep a running total to show at the end after calculating each symbol
# 	total_bytes += total_bytes_of_symbol(symbol, dict_counts)

# print(total_bytes)


# print(counts.get('n'))


# heapify(counts)
# print(counts)

# class TreeNode:
# 	def __init__(self, symbol, freq):
# 		self.symbol = symbol
# 		self.freq = freq

# 	def freq(self):
# 		return self.freq

# print(heappop(counts))


# from heapq import heappush, heappop, heapify
# from collections import defaultdict
 
# def encode(symb2freq):
#     """Huffman encode the given dict mapping symbols to weights"""
#     heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
#     print('This is the heap:', heap)
#     heapify(heap)
#     while len(heap) > 1:
#         lo = heappop(heap)
#         print(lo)
#         hi = heappop(heap)
#         print(hi)
#         for pair in lo[1:]:

        	
#         	pair[1] = '0' + pair[1]
#         for pair in hi[1:]:
#         	print(pair[1])
#         	pair[1] = '1' + pair[1]


#         heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
#     return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 




# txt = "this is an example for huffman encoding"
# symb2freq = defaultdict(int)
# for ch in txt:
#     symb2freq[ch] += 1
# # in Python 3.1+:
# # symb2freq = collections.Counter(txt)
# huff = encode(symb2freq)
# print("Symbol\tWeight\tHuffman Code")
# for p in huff:
#     print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))
