from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5MDO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 20-35 & chain A, resi 47-52 & chain A, resi 338-349 & chain A, resi 307-317 & chain A, resi 292-304 & chain A, resi 268-277 & chain A, resi 251-265 & chain A, resi 233-246 & chain A, resi 214-228 & chain A, resi 197-211 & chain A, resi 184-194 & chain A, resi 164-172 & chain A, resi 148-156 & chain A, resi 106-114 & chain A, resi 96-102 & chain A, resi 70-76 & chain A, resi 55-62 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-2.1828989521303077,1.6304574409063826,33.75282454997935])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
