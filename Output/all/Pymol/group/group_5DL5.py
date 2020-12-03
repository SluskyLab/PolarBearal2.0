from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-28 & chain A, resi 35-47 & chain A, resi 55-68 & chain A, resi 91-103 & chain A, resi 106-113 & chain A, resi 131-142 & chain A, resi 145-156 & chain A, resi 175-185 & chain A, resi 188-197 & chain A, resi 201-214 & chain A, resi 218-231 & chain A, resi 258-271 & chain A, resi 274-285 & chain A, resi 317-326 & chain A, resi 336-350 & chain A, resi 354-369 & chain A, resi 379-389 & chain A, resi 401-414 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-5.770750016790995,-49.73106574175651,4.220039515837765])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
