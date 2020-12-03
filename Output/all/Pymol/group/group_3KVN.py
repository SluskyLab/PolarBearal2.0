from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-11 & chain A, resi 139-142 & chain A, resi 182-185 & chain A, resi 227-230 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-3.6777500426396728,31.97031259536743,69.14662456512451])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 108-112 & chain A, resi 115-120 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-15.575000069358133,30.592454216697,89.70918135209517])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 347-360 & chain A, resi 369-383 & chain A, resi 388-403 & chain A, resi 408-425 & chain A, resi 428-450 & chain A, resi 453-474 & chain A, resi 484-499 & chain A, resi 517-533 & chain A, resi 538-549 & chain A, resi 579-592 & chain A, resi 595-606 & chain A, resi 609-621 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-2.795828143362693,43.41139061252276,28.351677084962528])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 512-514 & chain A, resi 556-561 & chain A, resi 564-572 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[4.399666713343726,30.381166564093697,57.05299970838759])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
