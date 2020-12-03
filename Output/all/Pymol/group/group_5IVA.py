from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IVA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 51-54 & chain A, resi 60-63 & chain A, resi 74-83 & chain A, resi 66-68 & chain A, resi 89-98 & chain A, resi 101-111 & chain A, resi 126-136 & chain A, resi 142-151 & chain A, resi 171-181 & chain A, resi 185-196 & chain A, resi 206-216 & chain A, resi 225-236 & chain A, resi 267-278 & chain A, resi 286-302 & chain A, resi 321-343 & chain A, resi 346-361 & chain A, resi 399-412 & chain A, resi 416-428 & chain A, resi 463-471 & chain A, resi 475-484 & chain A, resi 489-499 & chain A, resi 508-516 & chain A, resi 538-548 & chain A, resi 553-562 & chain A, resi 567-578 & chain A, resi 583-596 & chain A, resi 602-615 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[41.0591315407502,41.43968746850365,81.04592773788853])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 251-253 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[49.553000132242836,5.77733318010966,76.8010025024414])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 520-522 & chain A, resi 529-531 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[57.50733311971029,30.359333356221516,78.87583287556966])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
