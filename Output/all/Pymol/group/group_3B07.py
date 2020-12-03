from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3B07.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 18-28 & chain A, resi 33-43 & chain A, resi 49-61 & chain A, resi 225-233 & chain A, resi 95-101 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[58.00786261465035,9.895450947915807,-57.200333314783435])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 74-88 & chain A, resi 162-169 & chain A, resi 130-154 & chain A, resi 108-125 & chain A, resi 102-118 & chain B, resi 122-150 & chain B, resi 153-165 & chain B, resi 70-84 & chain B, resi 59-62 & chain B, resi 168-171 & chain B, resi 222-241 & chain B, resi 244-266 & chain B, resi 271-278 & chain B, resi 108-125 & chain C, resi 130-154 & chain C, resi 162-169 & chain C, resi 74-88 & chain C, resi 239-257 & chain C, resi 262-282 & chain C, resi 287-299 & chain C, resi 102-118 & chain D, resi 122-150 & chain D, resi 153-165 & chain D, resi 70-84 & chain D, resi 59-62 & chain D, resi 168-171 & chain D, resi 222-241 & chain D, resi 244-266 & chain D, resi 271-278 & chain D, resi 108-125 & chain E, resi 130-154 & chain E, resi 162-169 & chain E, resi 74-88 & chain E, resi 239-257 & chain E, resi 262-282 & chain E, resi 287-299 & chain E, resi 102-118 & chain F, resi 122-150 & chain F, resi 153-165 & chain F, resi 70-84 & chain F, resi 59-62 & chain F, resi 168-171 & chain F, resi 222-241 & chain F, resi 244-266 & chain F, resi 271-278 & chain F, resi 108-125 & chain G, resi 130-154 & chain G, resi 162-169 & chain G, resi 74-88 & chain G, resi 239-257 & chain G, resi 262-282 & chain G, resi 287-299 & chain G, resi 102-118 & chain H, resi 122-150 & chain H, resi 153-165 & chain H, resi 70-84 & chain H, resi 59-62 & chain H, resi 168-171 & chain H, resi 222-241 & chain H, resi 244-266 & chain H, resi 271-278 & chain H, resi 239-257 & chain A, resi 262-282 & chain A, resi 287-299 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[51.63979370452996,41.25637795028853,-31.20903572723979])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 13-22 & chain B, resi 27-36 & chain B, resi 44-55 & chain B, resi 208-215 & chain B, resi 89-95 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[33.26227654802038,14.662957500904165,-56.30117010562978])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 18-28 & chain C, resi 33-43 & chain C, resi 49-61 & chain C, resi 225-233 & chain C, resi 95-101 & chain C, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[20.104921630784578,34.948372560388904,-57.134647444182754])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 12-22 & chain D, resi 27-37 & chain D, resi 44-55 & chain D, resi 208-215 & chain D, resi 89-95 & chain D, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[25.10922451408542,59.29255076817104,-56.75936765086894])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 18-28 & chain E, resi 33-43 & chain E, resi 49-61 & chain E, resi 225-233 & chain E, resi 95-101 & chain E, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[45.23643153321509,72.73964721081303,-57.04013704786114])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 12-22 & chain F, resi 27-37 & chain F, resi 44-55 & chain F, resi 208-215 & chain F, resi 89-95 & chain F, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[69.63608216266243,67.82232627090143,-56.72883683807996])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 18-28 & chain G, resi 33-43 & chain G, resi 49-61 & chain G, resi 225-233 & chain G, resi 95-101 & chain G, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[83.13323510861865,47.72825502881817,-57.1045098398246])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 12-22 & chain H, resi 27-37 & chain H, resi 44-55 & chain H, resi 208-215 & chain H, resi 89-95 & chain H, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[78.12044836550342,23.32695907475997,-56.85724499760842])
cmd.color ("purple", "Centroid8")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
