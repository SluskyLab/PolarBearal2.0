from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6R2Q.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 52-63 & chain B, resi 85-88 & chain B, resi 99-102 & chain B, resi 110-113 & chain B, resi 121-135 & chain B, resi 173-191 & chain B, resi 138-140 & chain B, resi 196-216 & chain B, resi 221-242 & chain B, resi 246-259 & chain B, resi 288-299 & chain B, resi 304-317 & chain B, resi 337-350 & chain B, resi 356-369 & chain B, resi 396-407 & chain B, resi 413-425 & chain B, resi 433-445 & chain B, resi 452-464 & chain B, resi 489-500 & chain B, resi 506-518 & chain B, resi 525-540 & chain B, resi 546-563 & chain B, resi 572-590 & chain B, resi 598-621 & chain B, resi 625-638 & chain B, resi 644-659 & chain B, resi 680-694 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[21.499013530737344,65.46374038490089,3.8595189381189443])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 263-267 & chain B, resi 279-283 & chain B, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[5.3098999738693236,36.14169979095459,-3.06309996843338])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 375-378 & chain B, resi 387-390 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[6.785499960184097,31.26075053215027,16.60574996471405])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
