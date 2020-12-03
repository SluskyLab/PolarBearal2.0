from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A0T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 73-82 & chain P, resi 117-128 & chain P, resi 134-145 & chain P, resi 159-168 & chain P, resi 181-188 & chain P, resi 206-217 & chain P, resi 221-233 & chain P, resi 241-253 & chain P, resi 256-264 & chain P, resi 286-296 & chain P, resi 306-316 & chain P, resi 335-344 & chain P, resi 351-363 & chain P, resi 371-384 & chain P, resi 389-403 & chain P, resi 413-427 & chain P, resi 439-449 & chain P, resi 472-482 & chain P, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-51.596661912827265,-18.056223835423587,-12.673728581571153])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 193-195 & chain P, resi 200-203 & chain P, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-53.54028538295201,-20.19571440560477,-12.273857116699219])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
