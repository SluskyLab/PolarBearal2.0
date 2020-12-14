from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 20-26 & chain A, resi 29-39 & chain A, resi 42-56 & chain A, resi 66-81 & chain A, resi 95-114 & chain A, resi 136-156 & chain A, resi 164-174 & chain A, resi 179-189 & chain A, resi 125-129 & chain A, resi 119-122 & chain A, resi 216-226 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[21.210522720308013,2.6633863618992493,18.898606060326777])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
