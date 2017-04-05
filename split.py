'''
Created on Apr 4, 2017

@author: david
'''
from getIDs import getIDs
#import Starter
import multiprocessing
from retrieve_sequence_inbatch import startSeqsaving

def splitjob(dict_geneGroups, path2groups):
    
    jobs = []
    for key in dict_geneGroups:
        p = multiprocessing.Process(target = startSeqsaving(dict_geneGroups[key], path2groups[key][0]))
        jobs.append(p)
        p.start()
    
    
    
    #for i in range(0, len(table_ID)):
        
     #   print table_ID
     
#Tester

#splitjob('/Users/david/Documents/Home/Studium/Master/in-silico/Gene_acd_ensemble_ID.csv')