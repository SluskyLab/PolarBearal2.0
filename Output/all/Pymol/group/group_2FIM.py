from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FIM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 252-259 & chain A, resi 270-275 & chain A, resi 281-288 & chain A, resi 296-300 & chain A, resi 313-319 & chain A, resi 325-329 & chain A, resi 349-355 & chain A, resi 368-373 & chain A, resi 405-410 & chain A, resi 438-441 & chain A, resi 451-457 & chain A, resi 460-465 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[88.04964050292969,-2.0786400394886733,26.0096799214681])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 414-416 & chain A, resi 421-423 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[97.39983367919922,18.12750005722046,14.427000045776367])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
