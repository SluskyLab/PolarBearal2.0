from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FRT.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FRT_A_S0", "resi 7-21 & chain A & 4FRT ")
cmd.color ("red", "4FRT_A_S0")


cmd.select("4FRT_A_S1", "resi 28-47 & chain A & 4FRT ")
cmd.color ("yellow", "4FRT_A_S1")


cmd.select("4FRT_A_S2", "resi 52-71 & chain A & 4FRT ")
cmd.color ("green", "4FRT_A_S2")


cmd.select("4FRT_A_S3", "resi 82-100 & chain A & 4FRT ")
cmd.color ("cyan", "4FRT_A_S3")


cmd.select("4FRT_A_S4", "resi 103-109 & chain A & 4FRT ")
cmd.color ("blue", "4FRT_A_S4")


cmd.select("4FRT_A_S5", "resi 131-138 & chain A & 4FRT ")
cmd.color ("magenta", "4FRT_A_S5")


cmd.select("4FRT_A_S6", "resi 144-151 & chain A & 4FRT ")
cmd.color ("red", "4FRT_A_S6")


cmd.select("4FRT_A_S7", "resi 184-194 & chain A & 4FRT ")
cmd.color ("yellow", "4FRT_A_S7")


cmd.select("4FRT_A_S8", "resi 198-208 & chain A & 4FRT ")
cmd.color ("green", "4FRT_A_S8")


cmd.select("4FRT_A_S9", "resi 211-224 & chain A & 4FRT ")
cmd.color ("cyan", "4FRT_A_S9")


cmd.select("4FRT_A_S10", "resi 228-240 & chain A & 4FRT ")
cmd.color ("blue", "4FRT_A_S10")


cmd.select("4FRT_A_S11", "resi 248-259 & chain A & 4FRT ")
cmd.color ("magenta", "4FRT_A_S11")


cmd.select("4FRT_A_S12", "resi 264-275 & chain A & 4FRT ")
cmd.color ("red", "4FRT_A_S12")


cmd.select("4FRT_A_S13", "resi 303-313 & chain A & 4FRT ")
cmd.color ("yellow", "4FRT_A_S13")


cmd.select("4FRT_A_S14", "resi 318-333 & chain A & 4FRT ")
cmd.color ("green", "4FRT_A_S14")


cmd.select("4FRT_A_S15", "resi 342-354 & chain A & 4FRT ")
cmd.color ("cyan", "4FRT_A_S15")


cmd.select("4FRT_A_S16", "resi 364-375 & chain A & 4FRT ")
cmd.color ("blue", "4FRT_A_S16")


cmd.select("4FRT_A_S17", "resi 380-391 & chain A & 4FRT ")
cmd.color ("magenta", "4FRT_A_S17")


cmd.select("4FRT_barrel", "4FRT_A_S*")
cmd.show("cartoon", "4FRT_barrel")
cmd.zoom("4FRT_barrel")
