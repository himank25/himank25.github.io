

def main():
	myfile = open("Experiments.txt", 'wb')
	print myfile.name
	
	for i in range(100):
		myfile.write(str(i) + "\n")
 
if __name__ == '__main__' :
	main()