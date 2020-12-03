from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QTT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-16 & chain A, resi 22-25 & chain A, resi 29-38 & chain A, resi 41-51 & chain A, resi 70-74 & chain A, resi 78-80 & chain A, resi 85-88 & chain A, resi 98-106 & chain A, resi 91-95 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[3.777166637143603,-1.2842592690829877,-14.465111105530351])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 56-58 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[10.997666676839193,-16.630333582560223,-10.30833371480306])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 113-115 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[20.58799934387207,24.942333857218426,-12.092999776204428])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
