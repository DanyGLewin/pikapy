from sys import argv

def pika_num(n=0):
	output = ' '.join(['pika pi' for i in range(n/2)])
	if n%2:
		output += ' pika'
	return output

if __name__ == '__main__':
	try:
		n = int(argv[1])
	except:
		n  = input('Number: ')
	print(pika_num(n))