from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5HZQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 5-13 & chain A, resi 40-46 & chain A, resi 49-55 & chain A, resi 59-66 & chain A, resi 128-136 & chain A, resi 119-125 & chain A, resi 107-113 & chain A, resi 92-99 & chain A, resi 80-87 & chain A, resi 71-74 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[5.649194819973661,-13.80041555924849,-15.0175844570259])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
