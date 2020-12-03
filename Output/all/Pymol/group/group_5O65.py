from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O65.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 108-119 & chain A, resi 144-160 & chain A, resi 164-203 & chain A, resi 207-215 & chain A, resi 223-231 & chain A, resi 266-277 & chain A, resi 280-291 & chain A, resi 316-326 & chain A, resi 331-342 & chain A, resi 362-374 & chain A, resi 380-388 & chain A, resi 396-405 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[42.593777756285824,100.71866014268663,10.562679717566793])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 294-296 & chain A, resi 309-312 & chain A, resi 345-349 & chain A, resi 355-357 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[29.55119997660319,111.0923329671224,32.789333724975585])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
