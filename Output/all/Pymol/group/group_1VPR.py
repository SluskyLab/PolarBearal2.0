from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VPR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 912-914 & chain A, resi 917-919 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[35.56183369954427,72.77350107828777,74.83916727701823])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 1028-1034 & chain A, resi 1071-1077 & chain A, resi 1080-1084 & chain A, resi 1094-1098 & chain A, resi 1162-1172 & chain A, resi 1150-1159 & chain A, resi 1137-1147 & chain A, resi 1124-1131 & chain A, resi 1112-1118 & chain A, resi 1102-1106 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[43.82326339420519,61.05771054719624,47.15206562845331])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
