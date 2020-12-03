from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GR7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 1046-1055 & chain A, resi 1058-1068 & chain A, resi 1074-1083 & chain A, resi 1089-1097 & chain A, resi 1046-1055 & chain B, resi 1058-1068 & chain B, resi 1074-1083 & chain B, resi 1089-1097 & chain B, resi 1046-1055 & chain C, resi 1058-1068 & chain C, resi 1074-1083 & chain C, resi 1089-1097 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.183691654602686,19.04037495056788,57.57119998931885])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 1046-1055 & chain D, resi 1058-1068 & chain D, resi 1074-1083 & chain D, resi 1089-1097 & chain D, resi 1046-1055 & chain E, resi 1058-1068 & chain E, resi 1074-1083 & chain E, resi 1089-1097 & chain E, resi 1046-1055 & chain F, resi 1058-1068 & chain F, resi 1074-1083 & chain F, resi 1089-1097 & chain F, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[32.40921665827433,-9.109491696332892,57.382291603088376])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
