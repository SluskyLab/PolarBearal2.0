from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QOM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 1039-1051 & chain A, resi 1057-1069 & chain A, resi 1077-1092 & chain A, resi 1097-1112 & chain A, resi 1117-1133 & chain A, resi 1142-1160 & chain A, resi 1165-1182 & chain A, resi 1195-1215 & chain A, resi 1219-1235 & chain A, resi 1254-1268 & chain A, resi 1272-1282 & chain A, resi 1287-1294 & chain A, resi 1297-1300 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.697804199088187,7.364878264605684,16.85925397265052])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
