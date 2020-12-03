from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY7.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SY7_A_S0", "resi 18-31 & chain A & 3SY7 ")
cmd.color ("red", "3SY7_A_S0")


cmd.select("3SY7_A_S1", "resi 40-55 & chain A & 3SY7 ")
cmd.color ("yellow", "3SY7_A_S1")


cmd.select("3SY7_A_S2", "resi 60-76 & chain A & 3SY7 ")
cmd.color ("green", "3SY7_A_S2")


cmd.select("3SY7_A_S3", "resi 97-107 & chain A & 3SY7 ")
cmd.color ("cyan", "3SY7_A_S3")


cmd.select("3SY7_A_S4", "resi 112-117 & chain A & 3SY7 ")
cmd.color ("blue", "3SY7_A_S4")


cmd.select("3SY7_A_S5", "resi 138-144 & chain A & 3SY7 ")
cmd.color ("magenta", "3SY7_A_S5")


cmd.select("3SY7_A_S6", "resi 151-158 & chain A & 3SY7 ")
cmd.color ("red", "3SY7_A_S6")


cmd.select("3SY7_A_S7", "resi 183-193 & chain A & 3SY7 ")
cmd.color ("yellow", "3SY7_A_S7")


cmd.select("3SY7_A_S8", "resi 196-207 & chain A & 3SY7 ")
cmd.color ("green", "3SY7_A_S8")


cmd.select("3SY7_A_S9", "resi 209-223 & chain A & 3SY7 ")
cmd.color ("cyan", "3SY7_A_S9")


cmd.select("3SY7_A_S10", "resi 227-240 & chain A & 3SY7 ")
cmd.color ("blue", "3SY7_A_S10")


cmd.select("3SY7_A_S11", "resi 249-261 & chain A & 3SY7 ")
cmd.color ("magenta", "3SY7_A_S11")


cmd.select("3SY7_A_S12", "resi 264-275 & chain A & 3SY7 ")
cmd.color ("red", "3SY7_A_S12")


cmd.select("3SY7_A_S13", "resi 311-324 & chain A & 3SY7 ")
cmd.color ("yellow", "3SY7_A_S13")


cmd.select("3SY7_A_S14", "resi 329-345 & chain A & 3SY7 ")
cmd.color ("green", "3SY7_A_S14")


cmd.select("3SY7_A_S15", "resi 366-377 & chain A & 3SY7 ")
cmd.color ("cyan", "3SY7_A_S15")


cmd.select("3SY7_A_S16", "resi 387-398 & chain A & 3SY7 ")
cmd.color ("blue", "3SY7_A_S16")


cmd.select("3SY7_A_S17", "resi 406-420 & chain A & 3SY7 ")
cmd.color ("magenta", "3SY7_A_S17")


cmd.select("3SY7_barrel", "3SY7_A_S*")
cmd.show("cartoon", "3SY7_barrel")
cmd.zoom("3SY7_barrel")
