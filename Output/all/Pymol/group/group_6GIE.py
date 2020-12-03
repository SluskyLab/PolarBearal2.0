from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6GIE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 0-13 & chain A, resi 21-35 & chain A, resi 52-61 & chain A, resi 72-83 & chain A, resi 90-124 & chain A, resi 127-135 & chain A, resi 168-178 & chain A, resi 185-194 & chain A, resi 198-209 & chain A, resi 212-220 & chain A, resi 230-241 & chain A, resi 244-254 & chain A, resi 263-273 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[2.2200250096735545,168.61678705215454,50.36412501335144])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
