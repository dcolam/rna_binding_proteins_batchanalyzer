'''
Created on Mar 17, 2017

@author: david
'''
#!/usr/bin/python



def getIDs(path2Table):
    myrawtable = open(str(path2Table))
    table_ID = []
    for row in myrawtable:
        mytable =  row.split('\r')

    for i in range(0, len(mytable)):
        row = mytable[i].split(',')
        table_ID.append(row)
    myrawtable.close()
    #print table_ID[:50]
    return table_ID

#list_ID = getIDs('/Users/david/Documents/Home/Studium/Master/in-silico/Gene_acd_ensemble_ID.csv')

#print list_ID

