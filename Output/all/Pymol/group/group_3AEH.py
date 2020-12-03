from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3AEH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 1116-1128 & chain A, resi 1134-1150 & chain A, resi 1153-1170 & chain A, resi 1173-1190 & chain A, resi 1194-1211 & chain A, resi 1217-1237 & chain A, resi 1242-1257 & chain A, resi 1279-1292 & chain A, resi 1296-1310 & chain A, resi 1331-1345 & chain A, resi 1349-1359 & chain A, resi 1364-1377 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[31.513167615960405,-2.1109895082824517,0.8157643995671996])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
