from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-11 & chain A, resi 38-45 & chain A, resi 50-58 & chain A, resi 86-96 & chain A, resi 99-109 & chain A, resi 112-127 & chain A, resi 134-145 & chain A, resi 162-173 & chain A, resi 17-24 & chain A, resi 29-35 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[73.84947447343306,25.633141368326516,8.740727276287295])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
