from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FUV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 20-26 & chain A, resi 29-39 & chain A, resi 42-56 & chain A, resi 64-81 & chain A, resi 95-114 & chain A, resi 134-154 & chain A, resi 162-172 & chain A, resi 177-183 & chain A, resi 213-224 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[8.617258083796308,71.35892726529029,43.82140322654478])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 119-122 & chain A, resi 125-129 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[26.17388852437337,93.65411122639973,30.467111375596787])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
