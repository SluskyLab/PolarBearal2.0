from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3FIP_A_S0", "resi 147-159 & chain A & 3FIP ")
cmd.color ("red", "3FIP_A_S0")


cmd.select("3FIP_A_S1", "resi 163-176 & chain A & 3FIP ")
cmd.color ("yellow", "3FIP_A_S1")


cmd.select("3FIP_A_S2", "resi 182-195 & chain A & 3FIP ")
cmd.color ("green", "3FIP_A_S2")


cmd.select("3FIP_A_S3", "resi 201-217 & chain A & 3FIP ")
cmd.color ("cyan", "3FIP_A_S3")


cmd.select("3FIP_A_S4", "resi 221-228 & chain A & 3FIP ")
cmd.color ("blue", "3FIP_A_S4")


cmd.select("3FIP_A_S5", "resi 241-249 & chain A & 3FIP ")
cmd.color ("magenta", "3FIP_A_S5")


cmd.select("3FIP_A_S6", "resi 337-343 & chain A & 3FIP ")
cmd.color ("red", "3FIP_A_S6")


cmd.select("3FIP_A_S7", "resi 357-364 & chain A & 3FIP ")
cmd.color ("yellow", "3FIP_A_S7")


cmd.select("3FIP_A_S8", "resi 371-378 & chain A & 3FIP ")
cmd.color ("green", "3FIP_A_S8")


cmd.select("3FIP_A_S9", "resi 383-391 & chain A & 3FIP ")
cmd.color ("cyan", "3FIP_A_S9")


cmd.select("3FIP_A_S10", "resi 398-408 & chain A & 3FIP ")
cmd.color ("blue", "3FIP_A_S10")


cmd.select("3FIP_A_S11", "resi 416-426 & chain A & 3FIP ")
cmd.color ("magenta", "3FIP_A_S11")


cmd.select("3FIP_A_S12", "resi 436-445 & chain A & 3FIP ")
cmd.color ("red", "3FIP_A_S12")


cmd.select("3FIP_A_S13", "resi 468-477 & chain A & 3FIP ")
cmd.color ("yellow", "3FIP_A_S13")


cmd.select("3FIP_A_S14", "resi 485-494 & chain A & 3FIP ")
cmd.color ("green", "3FIP_A_S14")


cmd.select("3FIP_A_S15", "resi 501-510 & chain A & 3FIP ")
cmd.color ("cyan", "3FIP_A_S15")


cmd.select("3FIP_A_S16", "resi 521-528 & chain A & 3FIP ")
cmd.color ("blue", "3FIP_A_S16")


cmd.select("3FIP_A_S17", "resi 538-545 & chain A & 3FIP ")
cmd.color ("magenta", "3FIP_A_S17")


cmd.select("3FIP_A_S18", "resi 551-558 & chain A & 3FIP ")
cmd.color ("red", "3FIP_A_S18")


cmd.select("3FIP_A_S19", "resi 564-571 & chain A & 3FIP ")
cmd.color ("yellow", "3FIP_A_S19")


cmd.select("3FIP_A_S20", "resi 579-586 & chain A & 3FIP ")
cmd.color ("green", "3FIP_A_S20")


cmd.select("3FIP_A_S21", "resi 597-604 & chain A & 3FIP ")
cmd.color ("cyan", "3FIP_A_S21")


cmd.select("3FIP_A_S22", "resi 610-617 & chain A & 3FIP ")
cmd.color ("blue", "3FIP_A_S22")


cmd.select("3FIP_A_S23", "resi 624-633 & chain A & 3FIP ")
cmd.color ("magenta", "3FIP_A_S23")


cmd.select("3FIP_barrel", "3FIP_A_S*")
cmd.show("cartoon", "3FIP_barrel")
cmd.zoom("3FIP_barrel")
