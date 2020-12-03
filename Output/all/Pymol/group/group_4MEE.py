from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MEE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 1005-1017 & chain A, resi 1023-1039 & chain A, resi 1047-1066 & chain A, resi 1072-1089 & chain A, resi 1097-1115 & chain A, resi 1120-1144 & chain A, resi 1150-1168 & chain A, resi 1187-1200 & chain A, resi 1214-1222 & chain A, resi 1242-1253 & chain A, resi 1258-1268 & chain A, resi 1274-1284 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-7.829484084343656,3.1580159407346806,-20.684468074047818])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 1178-1182 & chain A, resi 1227-1230 & chain A, resi 1235-1237 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-6.836166754364967,21.704416751861572,-2.5502499838670096])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
