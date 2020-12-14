from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZD.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SZD_B_S0", "resi 14-27 & chain B & 3SZD ")
cmd.color ("red", "3SZD_B_S0")


cmd.select("3SZD_B_S1", "resi 37-53 & chain B & 3SZD ")
cmd.color ("yellow", "3SZD_B_S1")


cmd.select("3SZD_B_S2", "resi 58-73 & chain B & 3SZD ")
cmd.color ("green", "3SZD_B_S2")


cmd.select("3SZD_B_S3", "resi 95-105 & chain B & 3SZD ")
cmd.color ("cyan", "3SZD_B_S3")


cmd.select("3SZD_B_S4", "resi 110-115 & chain B & 3SZD ")
cmd.color ("blue", "3SZD_B_S4")


cmd.select("3SZD_B_S5", "resi 136-142 & chain B & 3SZD ")
cmd.color ("magenta", "3SZD_B_S5")


cmd.select("3SZD_B_S6", "resi 147-156 & chain B & 3SZD ")
cmd.color ("red", "3SZD_B_S6")


cmd.select("3SZD_B_S7", "resi 181-191 & chain B & 3SZD ")
cmd.color ("yellow", "3SZD_B_S7")


cmd.select("3SZD_B_S8", "resi 195-206 & chain B & 3SZD ")
cmd.color ("green", "3SZD_B_S8")


cmd.select("3SZD_B_S9", "resi 208-220 & chain B & 3SZD ")
cmd.color ("cyan", "3SZD_B_S9")


cmd.select("3SZD_B_S10", "resi 226-237 & chain B & 3SZD ")
cmd.color ("blue", "3SZD_B_S10")


cmd.select("3SZD_B_S11", "resi 248-259 & chain B & 3SZD ")
cmd.color ("magenta", "3SZD_B_S11")


cmd.select("3SZD_B_S12", "resi 262-276 & chain B & 3SZD ")
cmd.color ("red", "3SZD_B_S12")


cmd.select("3SZD_B_S13", "resi 301-314 & chain B & 3SZD ")
cmd.color ("yellow", "3SZD_B_S13")


cmd.select("3SZD_B_S14", "resi 319-336 & chain B & 3SZD ")
cmd.color ("green", "3SZD_B_S14")


cmd.select("3SZD_B_S15", "resi 340-355 & chain B & 3SZD ")
cmd.color ("cyan", "3SZD_B_S15")


cmd.select("3SZD_B_S16", "resi 365-376 & chain B & 3SZD ")
cmd.color ("blue", "3SZD_B_S16")


cmd.select("3SZD_B_S17", "resi 383-396 & chain B & 3SZD ")
cmd.color ("magenta", "3SZD_B_S17")


cmd.select("3SZD_barrel", "3SZD_B_S*")
cmd.show("cartoon", "3SZD_barrel")
cmd.zoom("3SZD_barrel")
