'''
Created on Mar 15, 2017

@author: david
'''

#!/usr/bin/python

import csv 
import os

def dir_checker_csv(dirpath, list):
    a = list
    if not 'output' in dirpath:
        if os.path.isdir(dirpath):
            for filename in os.listdir(dirpath):
                if not '.DS_Store' in filename:
                    if '.csv' in dirpath:
                        a.append(dirpath + '/' + filename)
    
                    elif os.path.isdir(dirpath + '/'+ filename):
                        dir_checker_csv(dirpath + '/'+ filename, a)
                    elif '.csv' in filename:
                        a.append(dirpath + '/' + filename)
    #print a
    return a

def load_csv(filepath):

    dict_rbp_per_gene = {}
    list_probenames = []
    all_rbp_names_dict = {}

    f = open(filepath, 'r')
    reader = csv.reader(f)
    #reader = f.read()
    rbp_list = []
    rbp_name_list = []
    name = ''
    filename_list = filepath.split('/')
    filename = filename_list[-1].replace('.csv', '')
    list_probenames.append(filename)
    #print filename
    for row in reader:
        #print row
        if len(row) > 1 and 'ENSMUS' in row[3]:
            if ',' in row[4]:
                #print row[4]
                row[4] = row[4].replace(',', ' ')
                print row[4]
            rbp_list.append(row)
            rbp_name_list.append(row[1]) #extract more data here
    dict_rbp_per_gene[filename] = rbp_list
    #all_rbp_names_dict[filename] = rbp_name_list
    f.close()
                 
    return dict_rbp_per_gene 


def load_csv_in_batch(path2allgroups):
    filepaths = []
    filepaths = dir_checker_csv(path2allgroups, filepaths)
    #print filepaths
    
    dict_all_genes = {}
    dict_all_groups = {}
    list_all_groups = []
    
    #dict_all_genes = load_csv('/Users/david/Documents/Home/Studium/Master/in-silico/try2/groupedSequences/Circadian-Syn/Lingo1.csv')
    #print (filepaths)
    #print dict_all_genes
    for i in range(0, len(filepaths)):
        filename_l = filepaths[i].split('/')
        filenamegroup = filename_l[-2]
        dict_all_groups[filenamegroup] = []
        
    for i in range(0, len(filepaths)):

        filename_l = filepaths[i].split('/')
        filenamegroup = filename_l[-2]
        #dict_all_groups[filenamegroup] = []
        filename_gene =  filename_l[-1].replace('.csv', '')
        dict_all_genes = load_csv(filepaths[i])
        #print (dict_all_genes)
        #list_all_groups = list_all_groups.append(dict_all_genes)
        dict_all_groups[filenamegroup].append(dict_all_genes)
    
    print dict_all_groups
    for key in dict_all_groups: 
        print key
        for keys in dict_all_groups[key]:
            print keys
    save_csv_of_allrbp(dict_all_groups, path2allgroups)
    return dict_all_groups

def save_csv_of_allrbp(dict_from_loadcsv, destpath):
    #creat csvfile in path
    #destpath = raw_input('Where do you want to save your output csv file with all rbps?')
    #fieldnames =  ['RBP ID', 'Name', 'Motif ID', 'GeneID', 'Family', 'Sequence', 'From', 'To', 'Score']
    '''with open(destpath, 'w+') as csvfile:
        filewriter = csv.write(csvfile, delimiter=',', quotechar='|')
        for key in dict_from_loadcsv.items():
            filewriter.writerow(key)
            for keys, value in dict_from_loadcsv[key].items():
                filewriter.writerow([keys, value])
    csvfile.close()'''
    if os.path.isdir(destpath):
        if not os.path.isdir(destpath + '/output'):
            os.makedirs(destpath + '/output')
            
    for filename in os.listdir(destpath + '/output'):
         if '.csv' in filename:
             numofprevioustrials = len(os.listdir(destpath + '/output')) + 1
         else:
            numofprevioustrials = 0
    
    save_csv = open(destpath + '/output/allrpbsaved%s.csv'% numofprevioustrials , 'w+')
    for key in dict_from_loadcsv:
            save_csv.write(str(key) + ',\n')
            print key
            for k in range(0, len(dict_from_loadcsv[key])):
                for keys in dict_from_loadcsv[key][k]:
                    save_csv.write(str(keys) + ',\n')
                    #print (dict_from_loadcsv[key][keys])
                    for i in range(0, len(dict_from_loadcsv[key][k][keys])):
    
                        for j in range(0, len(dict_from_loadcsv[key][k][keys][i])):
                           save_csv.write(dict_from_loadcsv[key][k][keys][i][j] + ',')
                        save_csv.write('\n')
                
                    
    save_csv.close()
    
    
    
    '''else:
        
        with open(destpath, 'w+') as csvfile:
            filewriter = csv.DictWriter(csvfile, delimiter=',', )
            for key in dict_from_loadcsv:
                filewriter.writerow(key)
                for keys, value in dict_from_loadcsv[key]:
                    filewriter.writerow(keys)
                    filewriter.writerow(value)
        csvfile.close()'''
        
        
#Tester
#dict_allrpb = load_csv_in_batch('/Users/david/Documents/Home/Studium/Master/in-silico/Gene')

#print dict_allrpb

#
#/Users/david/Documents/Home/Studium/Master/in-silico/try2/all.csv
   
