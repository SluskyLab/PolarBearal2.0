from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T24.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-23 & chain A, resi 26-43 & chain A, resi 58-66 & chain A, resi 89-101 & chain A, resi 104-111 & chain A, resi 129-137 & chain A, resi 150-161 & chain A, resi 185-195 & chain A, resi 198-207 & chain A, resi 211-225 & chain A, resi 228-260 & chain A, resi 263-273 & chain A, resi 303-312 & chain A, resi 321-334 & chain A, resi 341-354 & chain A, resi 364-374 & chain A, resi 379-392 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-1.5354235707151838,1.493222689939313,-34.605633210927635])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
