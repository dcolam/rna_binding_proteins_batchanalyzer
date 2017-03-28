'''
Created on Mar 23, 2017

@author: david
'''
import os


#Stores every filepath thats in a folder
def dir_checker(dirpath, list):
    a = list
    if os.path.isdir(dirpath):
        for filename in os.listdir(dirpath):
            if not '.DS_Store' in filename:
                if '.fasta' in dirpath:
                    a.append(dirpath + '/' + filename)
                elif os.path.isdir(dirpath + '/'+ filename):
                    dir_checker(dirpath + '/'+ filename, a)
                elif '.fasta' in filename:
                    a.append(dirpath + '/' + filename)
        
    return a



def load_file(filepath):

#Read input in a list
    seq_list = {}
    seq = open(filepath)
    numberOfIsoforms = 0
    
    #Retrieve filepath and filename
#######################################################
    filepath_list = filepath.split('/')
    filename_list = filepath_list[-1].split('.')
    filename = filename_list[0]

#Fill in seq_list and seq_list_diff
#######################################################
    for line in (seq):
        #line = line.strip()
        if '>' in line:
            numberOfIsoforms += 1
            seq_list[str(filename + '_Transcript%s' %numberOfIsoforms)] = ''
            
        if not '>' in line:
            seq_list[str(filename + '_Transcript%s' %numberOfIsoforms)] += (line)
    
    seq.close()

    return seq_list
#Read all fasta files in a folder (Dict of a dict)

def batch_load_files(path2folder):
    dict_GeneInFolder = {}
    filepaths = []
    filepaths = dir_checker(path2folder, filepaths)
    gene_names_list = []
    gene_name_list = []

    for i in range(0, len(filepaths)):
        dict_file = load_file(filepaths[i])
        gene_names_list = filepaths[i].split("/")


        gene_name_list = gene_names_list[-1].split('.')
        dict_GeneInFolder[gene_name_list[0]] = dict_file
    

    return dict_GeneInFolder

#Tester

seq_list = batch_load_files('/Users/david/Documents/Home/Studium/Master/in-silico/groupedSequences')
print seq_list

for key, value in seq_list.iteritems():
    print key
    print ''
    for keys, values in seq_list[key].iteritems():
        print values
        print 'Number of bp: %s\n' %len(values)

        

