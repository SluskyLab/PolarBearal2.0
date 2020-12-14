from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-28 & chain A, resi 36-49 & chain A, resi 57-70 & chain A, resi 94-106 & chain A, resi 109-116 & chain A, resi 134-145 & chain A, resi 148-159 & chain A, resi 182-191 & chain A, resi 196-205 & chain A, resi 209-222 & chain A, resi 225-238 & chain A, resi 248-260 & chain A, resi 263-273 & chain A, resi 304-313 & chain A, resi 322-336 & chain A, resi 340-355 & chain A, resi 365-375 & chain A, resi 383-395 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.040631124013,-33.308382246229385,-10.575040021753974])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 169-171 & chain A, resi 174-179 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[15.489444414774576,-46.32833353678385,-26.826666514078777])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
