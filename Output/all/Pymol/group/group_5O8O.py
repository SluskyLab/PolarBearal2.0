from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O8O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 67-76 & chain A, resi 79-85 & chain A, resi 95-102 & chain A, resi 105-113 & chain A, resi 117-124 & chain A, resi 131-137 & chain A, resi 143-151 & chain A, resi 155-162 & chain A, resi 170-182 & chain A, resi 187-197 & chain A, resi 204-215 & chain A, resi 220-225 & chain A, resi 231-238 & chain A, resi 243-252 & chain A, resi 266-275 & chain A, resi 280-288 & chain A, resi 291-299 & chain A, resi 305-314 & chain A, resi 319-329 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-23.654931470751762,2.2796399881158558,8.2249028618208])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
