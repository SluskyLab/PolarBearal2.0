from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 147-158 & chain A, resi 165-176 & chain A, resi 181-188 & chain A, resi 191-194 & chain A, resi 201-204 & chain A, resi 207-217 & chain A, resi 222-230 & chain A, resi 240-248 & chain A, resi 336-344 & chain A, resi 356-365 & chain A, resi 370-379 & chain A, resi 382-392 & chain A, resi 398-409 & chain A, resi 415-425 & chain A, resi 437-444 & chain A, resi 467-478 & chain A, resi 485-495 & chain A, resi 501-510 & chain A, resi 521-527 & chain A, resi 538-545 & chain A, resi 552-557 & chain A, resi 563-572 & chain A, resi 579-605 & chain A, resi 609-618 & chain A, resi 623-634 & chain A, resi 202-216 & chain B, resi 181-193 & chain B, resi 222-231 & chain B, resi 239-248 & chain B, resi 336-344 & chain B, resi 356-365 & chain B, resi 370-379 & chain B, resi 382-391 & chain B, resi 399-409 & chain B, resi 415-422 & chain B, resi 439-444 & chain B, resi 467-473 & chain B, resi 489-495 & chain B, resi 501-528 & chain B, resi 537-542 & chain B, resi 555-557 & chain B, resi 564-566 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.434817498568446,32.75253251992166,50.02314252018928])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 266-268 & chain A, resi 291-293 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[23.390999794006348,37.95383326212565,65.5303332010905])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 273-278 & chain A, resi 281-287 & chain A, resi 305-311 & chain A, resi 320-323 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[28.957958618799847,26.551249901453655,61.59933360417684])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 148-154 & chain B, resi 626-633 & chain B, resi 609-616 & chain B, resi 599-603 & chain B, resi 580-583 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[26.99781247973442,17.411562532186508,18.306468695402145])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 273-278 & chain B, resi 305-311 & chain B, resi 319-323 & chain B, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[25.17427772945828,34.42433346642388,27.66505569881863])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
