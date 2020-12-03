from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AVG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 24-28 & chain I, resi 51-56 & chain I, resi 37-43 & chain I, resi 66-71 & chain I, resi 80-86 & chain I, resi 92-101 & chain I, resi 106-115 & chain I, resi 122-128 & chain I, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-3.4364310428500175,32.98355171598237,91.90698255341628])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
