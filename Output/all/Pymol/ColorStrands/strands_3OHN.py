from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3OHN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3OHN_A_S0", "resi 141-151 & chain A & 3OHN ")
cmd.color ("red", "3OHN_A_S0")


cmd.select("3OHN_A_S1", "resi 159-170 & chain A & 3OHN ")
cmd.color ("yellow", "3OHN_A_S1")


cmd.select("3OHN_A_S2", "resi 176-187 & chain A & 3OHN ")
cmd.color ("green", "3OHN_A_S2")


cmd.select("3OHN_A_S3", "resi 197-209 & chain A & 3OHN ")
cmd.color ("cyan", "3OHN_A_S3")


cmd.select("3OHN_A_S4", "resi 214-220 & chain A & 3OHN ")
cmd.color ("blue", "3OHN_A_S4")


cmd.select("3OHN_A_S5", "resi 234-240 & chain A & 3OHN ")
cmd.color ("magenta", "3OHN_A_S5")


cmd.select("3OHN_A_S6", "resi 330-337 & chain A & 3OHN ")
cmd.color ("red", "3OHN_A_S6")


cmd.select("3OHN_A_S7", "resi 348-359 & chain A & 3OHN ")
cmd.color ("yellow", "3OHN_A_S7")


cmd.select("3OHN_A_S8", "resi 362-371 & chain A & 3OHN ")
cmd.color ("green", "3OHN_A_S8")


cmd.select("3OHN_A_S9", "resi 374-385 & chain A & 3OHN ")
cmd.color ("cyan", "3OHN_A_S9")


cmd.select("3OHN_A_S10", "resi 391-402 & chain A & 3OHN ")
cmd.color ("blue", "3OHN_A_S10")


cmd.select("3OHN_A_S11", "resi 409-420 & chain A & 3OHN ")
cmd.color ("magenta", "3OHN_A_S11")


cmd.select("3OHN_A_S12", "resi 429-438 & chain A & 3OHN ")
cmd.color ("red", "3OHN_A_S12")


cmd.select("3OHN_A_S13", "resi 481-490 & chain A & 3OHN ")
cmd.color ("yellow", "3OHN_A_S13")


cmd.select("3OHN_A_S14", "resi 495-506 & chain A & 3OHN ")
cmd.color ("green", "3OHN_A_S14")


cmd.select("3OHN_A_S15", "resi 514-524 & chain A & 3OHN ")
cmd.color ("cyan", "3OHN_A_S15")


cmd.select("3OHN_A_S16", "resi 529-538 & chain A & 3OHN ")
cmd.color ("blue", "3OHN_A_S16")


cmd.select("3OHN_A_S17", "resi 546-555 & chain A & 3OHN ")
cmd.color ("magenta", "3OHN_A_S17")


cmd.select("3OHN_A_S18", "resi 575-582 & chain A & 3OHN ")
cmd.color ("red", "3OHN_A_S18")


cmd.select("3OHN_A_S19", "resi 588-597 & chain A & 3OHN ")
cmd.color ("yellow", "3OHN_A_S19")


cmd.select("3OHN_A_S20", "resi 601-611 & chain A & 3OHN ")
cmd.color ("green", "3OHN_A_S20")


cmd.select("3OHN_A_S21", "resi 619-629 & chain A & 3OHN ")
cmd.color ("cyan", "3OHN_A_S21")


cmd.select("3OHN_A_S22", "resi 632-641 & chain A & 3OHN ")
cmd.color ("blue", "3OHN_A_S22")


cmd.select("3OHN_A_S23", "resi 647-656 & chain A & 3OHN ")
cmd.color ("magenta", "3OHN_A_S23")


cmd.select("3OHN_barrel", "3OHN_A_S*")
cmd.show("cartoon", "3OHN_barrel")
cmd.zoom("3OHN_barrel")
