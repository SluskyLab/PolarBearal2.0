import os
#import numpy as np
#import glob
#import re



DB_file = "../MonoDBList.txt"
poly = False

def getPolyBarrelPDBs(pdb):
    os.system("curl https://files.rcsb.org/download/%s.pdb -o %s.pdb" %(pdb, pdb))
    filename = "%s.pdb"%(pdb)
    with open(filename, "r") as pdb_file:
        pdb_lines = pdb_file.readlines()
        chain_list = []
        for row in pdb_lines:
            if "ATOM" in row[0:4]: chain_list.append(row[21])
            chain_list = sorted(set(chain_list))
    if len(chain_list)<3:
        os.remove("%s.pdb" % pdb)
        os.system("curl https://files.rcsb.org/download/%s.pdb1 -o %s.pdb" %(pdb, pdb))
        filename2 = "%s.pdb2"%(pdb)
        alphabet=['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
        cur_chain_i=1
        with open(filename, "r") as pdb_file:
            with open(filename2, "w+") as pdb_file2:
                pdb_lines = pdb_file.readlines()
                chain_list = []
                for row in pdb_lines:
                    new_row=row
                    if "ATOM" in row[0:4]: new_row=row[:21]+alphabet[cur_chain_i]+row[22:]
                    if "ENDMDL" in row[0:6]:cur_chain_i+=1
                    elif "MODEL" in row[0:6]: continue
                    else: pdb_file2.write(new_row)
        os.system("mv %s.pdb2 %s.pdb"%(pdb, pdb))

with open(DB_file, "r") as DBlist:
    for line in DBlist:
        line = line.strip()
        pdb = line.upper()
        if os.path.isfile("%s.pdb" %pdb)==True:
            #print("File exists")
            continue
        else:
            ## use for poly barrels (issue of the state)
            if(poly==True):getPolyBarrelPDBs(pdb)
            ## use for everything else 
            else: os.system("curl https://files.rcsb.org/download/%s.pdb -o %s.pdb" %(pdb, pdb))



