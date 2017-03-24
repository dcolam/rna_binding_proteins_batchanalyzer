'''
Created on Mar 16, 2017

@author: david
'''
#!/usr/bin/python


from Bio import Entrez
from Bio import SeqIO
import mygene


#start_time = time.time()

def retrieve_seq(gene_id): #Function that retrieves genes from Entrez via a gene id
    print 'Sequence retrieved'
    Entrez.email = 'A.N.Other@example.com'
    handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=gene_id)
    seq_record = SeqIO.read(handle, "gb") #using "gb" as an alias for "genbank"
    handle.close()

    return seq_record

def batch_retrieve_seq(list_gene_id, singlefile, path): #give a list with gene id's, retrieve them and save them in a fasta file, singlefile boolean variable to define if there is only 1 output file per id or not (default = save in a singlefile)
    if singlefile == 'True':
        list_seq_rec = []
        for i in range(1, len(list_gene_id)):
            seq_record = retrieve_seq(list_gene_id[i])
            list_seq_rec.append(seq_record)
    
        SeqIO.write(list_seq_rec[:], path + '/%s.fasta' %list_gene_id[0], 'fasta')
        print'Single File saved of all isoforms of ', list_gene_id[0]
        print'-------------------------------------' 
    if singlefile == 'False':
        for i in range(1, len(list_gene_id)):
            seq_record = retrieve_seq(list_gene_id[i])
            SeqIO.write(seq_record, path + '%s.fasta' %list_gene_id[0], 'fasta')
        print 'Files saved'

        
def convert_ID_getAllIsoformsNM(ensemble_ID, boolSave, path, preffix = 'NM'): #define prefix, default = NM for mRNA transcript variants
    print 'Converting IDs'
    mg = mygene.MyGeneInfo()
    
    list_xli = mg.getgene(ensemble_ID, fields = 'all', as_dataframe = True)['accession']['rna']
    list_transcript = [mg.getgene(ensemble_ID, fields = 'all', as_dataframe = True)['symbol']]
    for i in range(0, len(list_xli)):
        if preffix == 'NM':
            if list_xli[i][:2] == preffix:
                list_transcript.append(list_xli[i])
        elif list_xli[i][:2] == preffix:
            list_transcript.append(list_xli[i])
    print 'ID converted'
    if boolSave == False:
        return list_transcript
    if boolSave == True:
        if len(list_transcript) != 0:
            batch_retrieve_seq(list_transcript, 'True', path)
        else:
            print 'No RefSeq Ids with the Prefix %s found' %preffix
    



def startSeqsaving(xli, path):
    for i in range(0, len(xli)):
        if xli[i]!= '':
            convert_ID_getAllIsoformsNM(xli[i], True, path, 'NM')
    

#timer = str(round((time.time() - start_time), 2))

#print 'Done'
#print 'Total sequence retrieving time was %s seconds' + timer
