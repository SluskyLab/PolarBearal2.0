from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T24.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3T24_A_S0", "resi 7-21 & chain A & 3T24 ")
cmd.color ("red", "3T24_A_S0")


cmd.select("3T24_A_S1", "resi 29-47 & chain A & 3T24 ")
cmd.color ("yellow", "3T24_A_S1")


cmd.select("3T24_A_S2", "resi 52-66 & chain A & 3T24 ")
cmd.color ("green", "3T24_A_S2")


cmd.select("3T24_A_S3", "resi 90-100 & chain A & 3T24 ")
cmd.color ("cyan", "3T24_A_S3")


cmd.select("3T24_A_S4", "resi 105-109 & chain A & 3T24 ")
cmd.color ("blue", "3T24_A_S4")


cmd.select("3T24_A_S5", "resi 131-137 & chain A & 3T24 ")
cmd.color ("magenta", "3T24_A_S5")


cmd.select("3T24_A_S6", "resi 144-151 & chain A & 3T24 ")
cmd.color ("red", "3T24_A_S6")


cmd.select("3T24_A_S7", "resi 184-194 & chain A & 3T24 ")
cmd.color ("yellow", "3T24_A_S7")


cmd.select("3T24_A_S8", "resi 197-208 & chain A & 3T24 ")
cmd.color ("green", "3T24_A_S8")


cmd.select("3T24_A_S9", "resi 211-224 & chain A & 3T24 ")
cmd.color ("cyan", "3T24_A_S9")


cmd.select("3T24_A_S10", "resi 228-240 & chain A & 3T24 ")
cmd.color ("blue", "3T24_A_S10")


cmd.select("3T24_A_S11", "resi 248-259 & chain A & 3T24 ")
cmd.color ("magenta", "3T24_A_S11")


cmd.select("3T24_A_S12", "resi 262-275 & chain A & 3T24 ")
cmd.color ("red", "3T24_A_S12")


cmd.select("3T24_A_S13", "resi 303-313 & chain A & 3T24 ")
cmd.color ("yellow", "3T24_A_S13")


cmd.select("3T24_A_S14", "resi 320-331 & chain A & 3T24 ")
cmd.color ("green", "3T24_A_S14")


cmd.select("3T24_A_S15", "resi 343-354 & chain A & 3T24 ")
cmd.color ("cyan", "3T24_A_S15")


cmd.select("3T24_A_S16", "resi 364-375 & chain A & 3T24 ")
cmd.color ("blue", "3T24_A_S16")


cmd.select("3T24_A_S17", "resi 380-393 & chain A & 3T24 ")
cmd.color ("magenta", "3T24_A_S17")


cmd.select("3T24_barrel", "3T24_A_S*")
cmd.show("cartoon", "3T24_barrel")
cmd.zoom("3T24_barrel")
