from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AIP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4AIP_A_S0", "resi 184-194 & chain A & 4AIP ")
cmd.color ("red", "4AIP_A_S0")


cmd.select("4AIP_A_S1", "resi 198-208 & chain A & 4AIP ")
cmd.color ("yellow", "4AIP_A_S1")


cmd.select("4AIP_A_S2", "resi 211-223 & chain A & 4AIP ")
cmd.color ("green", "4AIP_A_S2")


cmd.select("4AIP_A_S3", "resi 246-259 & chain A & 4AIP ")
cmd.color ("cyan", "4AIP_A_S3")


cmd.select("4AIP_A_S4", "resi 263-279 & chain A & 4AIP ")
cmd.color ("blue", "4AIP_A_S4")


cmd.select("4AIP_A_S5", "resi 302-318 & chain A & 4AIP ")
cmd.color ("magenta", "4AIP_A_S5")


cmd.select("4AIP_A_S6", "resi 324-339 & chain A & 4AIP ")
cmd.color ("red", "4AIP_A_S6")


cmd.select("4AIP_A_S7", "resi 355-372 & chain A & 4AIP ")
cmd.color ("yellow", "4AIP_A_S7")


cmd.select("4AIP_A_S8", "resi 375-390 & chain A & 4AIP ")
cmd.color ("green", "4AIP_A_S8")


cmd.select("4AIP_A_S9", "resi 435-451 & chain A & 4AIP ")
cmd.color ("cyan", "4AIP_A_S9")


cmd.select("4AIP_A_S10", "resi 454-471 & chain A & 4AIP ")
cmd.color ("blue", "4AIP_A_S10")


cmd.select("4AIP_A_S11", "resi 476-490 & chain A & 4AIP ")
cmd.color ("magenta", "4AIP_A_S11")


cmd.select("4AIP_A_S12", "resi 494-506 & chain A & 4AIP ")
cmd.color ("red", "4AIP_A_S12")


cmd.select("4AIP_A_S13", "resi 522-544 & chain A & 4AIP ")
cmd.color ("yellow", "4AIP_A_S13")


cmd.select("4AIP_A_S14", "resi 547-560 & chain A & 4AIP ")
cmd.color ("green", "4AIP_A_S14")


cmd.select("4AIP_A_S15", "resi 583-596 & chain A & 4AIP ")
cmd.color ("cyan", "4AIP_A_S15")


cmd.select("4AIP_A_S16", "resi 599-614 & chain A & 4AIP ")
cmd.color ("blue", "4AIP_A_S16")


cmd.select("4AIP_A_S17", "resi 635-644 & chain A & 4AIP ")
cmd.color ("magenta", "4AIP_A_S17")


cmd.select("4AIP_A_S18", "resi 648-661 & chain A & 4AIP ")
cmd.color ("red", "4AIP_A_S18")


cmd.select("4AIP_A_S19", "resi 682-695 & chain A & 4AIP ")
cmd.color ("yellow", "4AIP_A_S19")


cmd.select("4AIP_A_S20", "resi 701-716 & chain A & 4AIP ")
cmd.color ("green", "4AIP_A_S20")


cmd.select("4AIP_A_S21", "resi 729-741 & chain A & 4AIP ")
cmd.color ("cyan", "4AIP_A_S21")


cmd.select("4AIP_barrel", "4AIP_A_S*")
cmd.show("cartoon", "4AIP_barrel")
cmd.zoom("4AIP_barrel")
