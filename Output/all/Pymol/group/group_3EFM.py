from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EFM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 54-57 & chain A, resi 127-134 & chain A, resi 148-154 & chain A, resi 101-104 & chain A, resi 107-110 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[32.81251836706091,28.9320740169949,-0.9920741021633148])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 81-83 & chain A, resi 91-94 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[21.7922853742327,29.031857081821986,8.909714358193535])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 162-170 & chain A, resi 174-184 & chain A, resi 191-202 & chain A, resi 211-225 & chain A, resi 228-241 & chain A, resi 261-275 & chain A, resi 281-297 & chain A, resi 302-323 & chain A, resi 326-347 & chain A, resi 368-387 & chain A, resi 390-407 & chain A, resi 410-429 & chain A, resi 434-445 & chain A, resi 460-473 & chain A, resi 478-495 & chain A, resi 510-513 & chain A, resi 517-530 & chain A, resi 533-545 & chain A, resi 559-568 & chain A, resi 576-586 & chain A, resi 597-609 & chain A, resi 612-619 & chain A, resi 643-651 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[31.466255484108242,28.676813106206346,-1.4617850784200745])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
