from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DWO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 44-63 & chain X, resi 93-105 & chain X, resi 110-125 & chain X, resi 138-153 & chain X, resi 158-177 & chain X, resi 201-220 & chain X, resi 226-233 & chain X, resi 239-248 & chain X, resi 275-281 & chain X, resi 287-295 & chain X, resi 300-309 & chain X, resi 316-321 & chain X, resi 324-330 & chain X, resi 336-346 & chain X, resi 351-360 & chain X, resi 378-388 & chain X, resi 395-406 & chain X, resi 423-441 & chain X, resi 409-411 & chain X, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[47.826504289058214,82.70783335702461,40.61982454333389])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
