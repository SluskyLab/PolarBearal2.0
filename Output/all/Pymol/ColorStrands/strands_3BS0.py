from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BS0.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3BS0_A_S0", "resi 44-60 & chain A & 3BS0 ")
cmd.color ("red", "3BS0_A_S0")


cmd.select("3BS0_A_S1", "resi 67-88 & chain A & 3BS0 ")
cmd.color ("yellow", "3BS0_A_S1")


cmd.select("3BS0_A_S2", "resi 94-109 & chain A & 3BS0 ")
cmd.color ("green", "3BS0_A_S2")


cmd.select("3BS0_A_S3", "resi 128-143 & chain A & 3BS0 ")
cmd.color ("cyan", "3BS0_A_S3")


cmd.select("3BS0_A_S4", "resi 151-170 & chain A & 3BS0 ")
cmd.color ("blue", "3BS0_A_S4")


cmd.select("3BS0_A_S5", "resi 198-227 & chain A & 3BS0 ")
cmd.color ("magenta", "3BS0_A_S5")


cmd.select("3BS0_A_S6", "resi 232-257 & chain A & 3BS0 ")
cmd.color ("red", "3BS0_A_S6")


cmd.select("3BS0_A_S7", "resi 264-288 & chain A & 3BS0 ")
cmd.color ("yellow", "3BS0_A_S7")


cmd.select("3BS0_A_S8", "resi 293-316 & chain A & 3BS0 ")
cmd.color ("green", "3BS0_A_S8")


cmd.select("3BS0_A_S9", "resi 322-344 & chain A & 3BS0 ")
cmd.color ("cyan", "3BS0_A_S9")


cmd.select("3BS0_A_S10", "resi 347-357 & chain A & 3BS0 ")
cmd.color ("blue", "3BS0_A_S10")


cmd.select("3BS0_A_S11", "resi 375-386 & chain A & 3BS0 ")
cmd.color ("magenta", "3BS0_A_S11")


cmd.select("3BS0_A_S12", "resi 389-406 & chain A & 3BS0 ")
cmd.color ("red", "3BS0_A_S12")


cmd.select("3BS0_A_S13", "resi 416-433 & chain A & 3BS0 ")
cmd.color ("yellow", "3BS0_A_S13")


cmd.select("3BS0_barrel", "3BS0_A_S*")
cmd.show("cartoon", "3BS0_barrel")
cmd.zoom("3BS0_barrel")
