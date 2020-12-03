from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6EHB_A_S0", "resi 21-33 & chain A & 6EHB ")
cmd.color ("red", "6EHB_A_S0")


cmd.select("6EHB_A_S1", "resi 40-55 & chain A & 6EHB ")
cmd.color ("yellow", "6EHB_A_S1")


cmd.select("6EHB_A_S2", "resi 59-69 & chain A & 6EHB ")
cmd.color ("green", "6EHB_A_S2")


cmd.select("6EHB_A_S3", "resi 84-93 & chain A & 6EHB ")
cmd.color ("cyan", "6EHB_A_S3")


cmd.select("6EHB_A_S4", "resi 98-103 & chain A & 6EHB ")
cmd.color ("blue", "6EHB_A_S4")


cmd.select("6EHB_A_S5", "resi 135-143 & chain A & 6EHB ")
cmd.color ("magenta", "6EHB_A_S5")


cmd.select("6EHB_A_S6", "resi 147-162 & chain A & 6EHB ")
cmd.color ("red", "6EHB_A_S6")


cmd.select("6EHB_A_S7", "resi 175-193 & chain A & 6EHB ")
cmd.color ("yellow", "6EHB_A_S7")


cmd.select("6EHB_A_S8", "resi 197-206 & chain A & 6EHB ")
cmd.color ("green", "6EHB_A_S8")


cmd.select("6EHB_A_S9", "resi 211-220 & chain A & 6EHB ")
cmd.color ("cyan", "6EHB_A_S9")


cmd.select("6EHB_A_S10", "resi 223-235 & chain A & 6EHB ")
cmd.color ("blue", "6EHB_A_S10")


cmd.select("6EHB_A_S11", "resi 239-251 & chain A & 6EHB ")
cmd.color ("magenta", "6EHB_A_S11")


cmd.select("6EHB_A_S12", "resi 256-265 & chain A & 6EHB ")
cmd.color ("red", "6EHB_A_S12")


cmd.select("6EHB_A_S13", "resi 271-283 & chain A & 6EHB ")
cmd.color ("yellow", "6EHB_A_S13")


cmd.select("6EHB_A_S14", "resi 286-297 & chain A & 6EHB ")
cmd.color ("green", "6EHB_A_S14")


cmd.select("6EHB_A_S15", "resi 311-319 & chain A & 6EHB ")
cmd.color ("cyan", "6EHB_A_S15")


cmd.select("6EHB_barrel", "6EHB_A_S*")
cmd.show("cartoon", "6EHB_barrel")
cmd.zoom("6EHB_barrel")
