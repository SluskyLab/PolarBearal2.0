from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6FOK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 27-30 & chain A, resi 107-112 & chain A, resi 126-131 & chain A, resi 76-80 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[36.7201901390439,116.6894284202939,57.54228591918945])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 54-57 & chain A, resi 65-68 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[48.04537487030029,108.70699882507324,56.68437576293945])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 141-151 & chain A, resi 155-166 & chain A, resi 169-180 & chain A, resi 195-206 & chain A, resi 212-225 & chain A, resi 233-249 & chain A, resi 255-272 & chain A, resi 290-308 & chain A, resi 311-332 & chain A, resi 337-339 & chain A, resi 347-363 & chain A, resi 369-384 & chain A, resi 406-421 & chain A, resi 427-438 & chain A, resi 465-477 & chain A, resi 481-501 & chain A, resi 508-528 & chain A, resi 533-546 & chain A, resi 560-569 & chain A, resi 572-581 & chain A, resi 605-615 & chain A, resi 620-627 & chain A, resi 660-668 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[40.533055774936734,116.36834353042461,60.507931924825854])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
