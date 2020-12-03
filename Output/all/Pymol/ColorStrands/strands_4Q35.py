from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Q35.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4Q35_A_S0", "resi 232-236 & chain A & 4Q35 ")
cmd.color ("red", "4Q35_A_S0")


cmd.select("4Q35_A_S1", "resi 240-249 & chain A & 4Q35 ")
cmd.color ("yellow", "4Q35_A_S1")


cmd.select("4Q35_A_S2", "resi 254-264 & chain A & 4Q35 ")
cmd.color ("green", "4Q35_A_S2")


cmd.select("4Q35_A_S3", "resi 268-279 & chain A & 4Q35 ")
cmd.color ("cyan", "4Q35_A_S3")


cmd.select("4Q35_A_S4", "resi 284-298 & chain A & 4Q35 ")
cmd.color ("blue", "4Q35_A_S4")


cmd.select("4Q35_A_S5", "resi 302-321 & chain A & 4Q35 ")
cmd.color ("magenta", "4Q35_A_S5")


cmd.select("4Q35_A_S6", "resi 324-335 & chain A & 4Q35 ")
cmd.color ("red", "4Q35_A_S6")


cmd.select("4Q35_A_S7", "resi 355-364 & chain A & 4Q35 ")
cmd.color ("yellow", "4Q35_A_S7")


cmd.select("4Q35_A_S8", "resi 367-378 & chain A & 4Q35 ")
cmd.color ("green", "4Q35_A_S8")


cmd.select("4Q35_A_S9", "resi 387-400 & chain A & 4Q35 ")
cmd.color ("cyan", "4Q35_A_S9")


cmd.select("4Q35_A_S10", "resi 407-420 & chain A & 4Q35 ")
cmd.color ("blue", "4Q35_A_S10")


cmd.select("4Q35_A_S11", "resi 426-440 & chain A & 4Q35 ")
cmd.color ("magenta", "4Q35_A_S11")


cmd.select("4Q35_A_S12", "resi 444-461 & chain A & 4Q35 ")
cmd.color ("red", "4Q35_A_S12")


cmd.select("4Q35_A_S13", "resi 476-495 & chain A & 4Q35 ")
cmd.color ("yellow", "4Q35_A_S13")


cmd.select("4Q35_A_S14", "resi 504-517 & chain A & 4Q35 ")
cmd.color ("green", "4Q35_A_S14")


cmd.select("4Q35_A_S15", "resi 554-567 & chain A & 4Q35 ")
cmd.color ("cyan", "4Q35_A_S15")


cmd.select("4Q35_A_S16", "resi 574-589 & chain A & 4Q35 ")
cmd.color ("blue", "4Q35_A_S16")


cmd.select("4Q35_A_S17", "resi 606-616 & chain A & 4Q35 ")
cmd.color ("magenta", "4Q35_A_S17")


cmd.select("4Q35_A_S18", "resi 619-629 & chain A & 4Q35 ")
cmd.color ("red", "4Q35_A_S18")


cmd.select("4Q35_A_S19", "resi 634-646 & chain A & 4Q35 ")
cmd.color ("yellow", "4Q35_A_S19")


cmd.select("4Q35_A_S20", "resi 650-659 & chain A & 4Q35 ")
cmd.color ("green", "4Q35_A_S20")


cmd.select("4Q35_A_S21", "resi 682-693 & chain A & 4Q35 ")
cmd.color ("cyan", "4Q35_A_S21")


cmd.select("4Q35_A_S22", "resi 696-706 & chain A & 4Q35 ")
cmd.color ("blue", "4Q35_A_S22")


cmd.select("4Q35_A_S23", "resi 711-722 & chain A & 4Q35 ")
cmd.color ("magenta", "4Q35_A_S23")


cmd.select("4Q35_A_S24", "resi 725-740 & chain A & 4Q35 ")
cmd.color ("red", "4Q35_A_S24")


cmd.select("4Q35_A_S25", "resi 744-759 & chain A & 4Q35 ")
cmd.color ("yellow", "4Q35_A_S25")


cmd.select("4Q35_barrel", "4Q35_A_S*")
cmd.show("cartoon", "4Q35_barrel")
cmd.zoom("4Q35_barrel")
