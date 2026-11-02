
# colwidth=[0]* len(tableData)
def rjustTable(tableData):
	colwidth=[0]* len(tableData)
	for i in range (len(tableData)):
		colwidth[i]=len(max(tableData[i],key=len))
	for r in range (len(tableData[0])):
		for c in range(len(tableData)):
			print(tableData[c][r].rjust(colwidth[c]), end='   ')
		print()


tableData= [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
rjustTable(tableData)