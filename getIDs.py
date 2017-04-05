'''
Created on Mar 17, 2017

@author: david
'''
#!/usr/bin/python

import os

def getIDs(path2Table):
    myrawtable = open(str(path2Table))
    table_ID = []
    for row in myrawtable:
        mytable =  row.split('\r')

    for i in range(0, len(mytable)):
        row = mytable[i].split(',')
        table_ID.append(row)
    myrawtable.close()
    dict_geneGroups = {}

    for i in range(0, len(table_ID[0])):
        dict_geneGroups[table_ID[0][i]] = []
    for i in range(0, len(table_ID[0])):
        #dict_geneGroups[str('group' + str(i+1))] = []
        for j in range(1, len(table_ID)):
            #print j, i
            dict_geneGroups[table_ID[0][i]].append(table_ID[j][i])
    
    print dict_geneGroups
            
    return dict_geneGroups

#list_ID = getIDs('/Users/david/Documents/Home/Studium/Master/in-silico/Gene_acd_ensemble_ID.csv')

#print list_ID

#===============================================================================
# def qualityCtrlID(table_ID):
#     for i in range(0, len(table_ID[0])):
#         temp={}
#         temp[table_ID[0][i]] = []
#         for j in range(1, len(table_ID)):  
#             temp[table_ID[0][i]].append(table_ID[j][i]) 
#         list_groups.append(temp)
#     
#     for i in range(0, len(list_groups)):
#         for key in list_groups[i]:
#             if len(list_groups[i][key]) > 100:
#===============================================================================
                

def create_folders(dict_geneGroups):
    path = os.path.dirname('./Output/groupedSequences')
    path2groups = {}
    if not os.path.exists(path):
        os.makedirs(path)
    for key in dict_geneGroups:
        pathGroup = path + '/' + key
        path2groups[key] = []
        if not os.path.exists(pathGroup):
            os.makedirs(pathGroup)
            print 'Folder %s created' %key
            print ''
        path2groups[key].append(pathGroup)
        
    print path2groups
    return path2groups
