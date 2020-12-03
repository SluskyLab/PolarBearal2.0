from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5DL8_B_S0", "resi 10-23 & chain B & 5DL8 ")
cmd.color ("red", "5DL8_B_S0")


cmd.select("5DL8_B_S1", "resi 32-48 & chain B & 5DL8 ")
cmd.color ("yellow", "5DL8_B_S1")


cmd.select("5DL8_B_S2", "resi 60-74 & chain B & 5DL8 ")
cmd.color ("green", "5DL8_B_S2")


cmd.select("5DL8_B_S3", "resi 97-107 & chain B & 5DL8 ")
cmd.color ("cyan", "5DL8_B_S3")


cmd.select("5DL8_B_S4", "resi 112-116 & chain B & 5DL8 ")
cmd.color ("blue", "5DL8_B_S4")


cmd.select("5DL8_B_S5", "resi 138-146 & chain B & 5DL8 ")
cmd.color ("magenta", "5DL8_B_S5")


cmd.select("5DL8_B_S6", "resi 150-158 & chain B & 5DL8 ")
cmd.color ("red", "5DL8_B_S6")


cmd.select("5DL8_B_S7", "resi 184-194 & chain B & 5DL8 ")
cmd.color ("yellow", "5DL8_B_S7")


cmd.select("5DL8_B_S8", "resi 197-208 & chain B & 5DL8 ")
cmd.color ("green", "5DL8_B_S8")


cmd.select("5DL8_B_S9", "resi 211-222 & chain B & 5DL8 ")
cmd.color ("cyan", "5DL8_B_S9")


cmd.select("5DL8_B_S10", "resi 228-239 & chain B & 5DL8 ")
cmd.color ("blue", "5DL8_B_S10")


cmd.select("5DL8_B_S11", "resi 248-259 & chain B & 5DL8 ")
cmd.color ("magenta", "5DL8_B_S11")


cmd.select("5DL8_B_S12", "resi 264-276 & chain B & 5DL8 ")
cmd.color ("red", "5DL8_B_S12")


cmd.select("5DL8_B_S13", "resi 303-314 & chain B & 5DL8 ")
cmd.color ("yellow", "5DL8_B_S13")


cmd.select("5DL8_B_S14", "resi 318-333 & chain B & 5DL8 ")
cmd.color ("green", "5DL8_B_S14")


cmd.select("5DL8_B_S15", "resi 341-352 & chain B & 5DL8 ")
cmd.color ("cyan", "5DL8_B_S15")


cmd.select("5DL8_B_S16", "resi 361-374 & chain B & 5DL8 ")
cmd.color ("blue", "5DL8_B_S16")


cmd.select("5DL8_B_S17", "resi 379-392 & chain B & 5DL8 ")
cmd.color ("magenta", "5DL8_B_S17")


cmd.select("5DL8_barrel", "5DL8_B_S*")
cmd.show("cartoon", "5DL8_barrel")
cmd.zoom("5DL8_barrel")
