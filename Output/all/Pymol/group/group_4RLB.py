from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RLB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-26 & chain A, resi 29-39 & chain A, resi 42-61 & chain A, resi 64-81 & chain A, resi 95-114 & chain A, resi 134-154 & chain A, resi 162-172 & chain A, resi 177-182 & chain A, resi 214-225 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-19.571092948664067,-55.40021710063136,0.7070232471234577])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 119-122 & chain A, resi 125-128 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-3.4002500846982002,-68.75675058364868,-19.693875074386597])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
