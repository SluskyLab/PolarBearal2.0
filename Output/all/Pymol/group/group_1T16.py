from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1T16.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 44-60 & chain A, resi 77-87 & chain A, resi 92-99 & chain A, resi 120-134 & chain A, resi 104-107 & chain A, resi 140-158 & chain A, resi 196-218 & chain A, resi 221-228 & chain A, resi 231-240 & chain A, resi 263-271 & chain A, resi 274-284 & chain A, resi 287-296 & chain A, resi 303-307 & chain A, resi 313-318 & chain A, resi 324-333 & chain A, resi 339-348 & chain A, resi 366-376 & chain A, resi 381-392 & chain A, resi 402-420 & chain A, resi 395-399 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[33.380502277425585,46.775753466003145,59.12712109142355])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
