from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UUN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-9 & chain B, resi 15-28 & chain B, resi 38-51 & chain B, resi 139-151 & chain B, resi 173-177 & chain B, resi 159-168 & chain B, resi 59-69 & chain B, resi 126-136 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.28643024244974,21.348651065729385,42.99284886204919])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 59-69 & chain B, resi 126-136 & chain B, resi 159-168 & chain B, resi 173-177 & chain B, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[26.889945932336754,10.538594580985404,43.40062198123417])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 72-81 & chain B, resi 112-121 & chain B, resi 112-121 & chain B, resi 72-81 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[4.811225072480738,17.699974954128265,77.00482578277588])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 2-9 & chain B, resi 15-28 & chain B, resi 38-51 & chain B, resi 139-151 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[9.145000010728836,33.906714497780314,42.6932041012511])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
