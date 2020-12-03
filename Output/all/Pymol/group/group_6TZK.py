from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6TZK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 744-746 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.562333424886067,7.669999917348226,81.70399983723958])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 783-798 & chain A, resi 803-817 & chain A, resi 820-832 & chain A, resi 854-875 & chain A, resi 878-885 & chain A, resi 891-904 & chain A, resi 907-918 & chain A, resi 943-953 & chain A, resi 959-972 & chain A, resi 978-994 & chain A, resi 997-1013 & chain A, resi 1029-1043 & chain A, resi 1046-1064 & chain A, resi 1084-1086 & chain A, resi 1089-1107 & chain A, resi 1110-1119 & chain A, resi 1125-1136 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[12.824142267355862,15.097451217048537,40.20576830705007])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 1024-1026 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[7.090999921162923,18.68999989827474,26.163333257039387])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 1067-1069 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[10.014000256856283,26.657000223795574,12.664999961853027])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 1140-1142 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[24.775333404541016,6.080333391825358,64.11533228556316])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
