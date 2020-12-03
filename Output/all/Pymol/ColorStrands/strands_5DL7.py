from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL7.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5DL7_A_S0", "resi 7-20 & chain A & 5DL7 ")
cmd.color ("red", "5DL7_A_S0")


cmd.select("5DL7_A_S1", "resi 31-47 & chain A & 5DL7 ")
cmd.color ("yellow", "5DL7_A_S1")


cmd.select("5DL7_A_S2", "resi 52-63 & chain A & 5DL7 ")
cmd.color ("green", "5DL7_A_S2")


cmd.select("5DL7_A_S3", "resi 91-101 & chain A & 5DL7 ")
cmd.color ("cyan", "5DL7_A_S3")


cmd.select("5DL7_A_S4", "resi 106-110 & chain A & 5DL7 ")
cmd.color ("blue", "5DL7_A_S4")


cmd.select("5DL7_A_S5", "resi 132-138 & chain A & 5DL7 ")
cmd.color ("magenta", "5DL7_A_S5")


cmd.select("5DL7_A_S6", "resi 143-152 & chain A & 5DL7 ")
cmd.color ("red", "5DL7_A_S6")


cmd.select("5DL7_A_S7", "resi 182-191 & chain A & 5DL7 ")
cmd.color ("yellow", "5DL7_A_S7")


cmd.select("5DL7_A_S8", "resi 194-205 & chain A & 5DL7 ")
cmd.color ("green", "5DL7_A_S8")


cmd.select("5DL7_A_S9", "resi 207-221 & chain A & 5DL7 ")
cmd.color ("cyan", "5DL7_A_S9")


cmd.select("5DL7_A_S10", "resi 225-238 & chain A & 5DL7 ")
cmd.color ("blue", "5DL7_A_S10")


cmd.select("5DL7_A_S11", "resi 247-259 & chain A & 5DL7 ")
cmd.color ("magenta", "5DL7_A_S11")


cmd.select("5DL7_A_S12", "resi 262-276 & chain A & 5DL7 ")
cmd.color ("red", "5DL7_A_S12")


cmd.select("5DL7_A_S13", "resi 300-316 & chain A & 5DL7 ")
cmd.color ("yellow", "5DL7_A_S13")


cmd.select("5DL7_A_S14", "resi 323-339 & chain A & 5DL7 ")
cmd.color ("green", "5DL7_A_S14")


cmd.select("5DL7_A_S15", "resi 348-360 & chain A & 5DL7 ")
cmd.color ("cyan", "5DL7_A_S15")


cmd.select("5DL7_A_S16", "resi 370-381 & chain A & 5DL7 ")
cmd.color ("blue", "5DL7_A_S16")


cmd.select("5DL7_A_S17", "resi 391-404 & chain A & 5DL7 ")
cmd.color ("magenta", "5DL7_A_S17")


cmd.select("5DL7_barrel", "5DL7_A_S*")
cmd.show("cartoon", "5DL7_barrel")
cmd.zoom("5DL7_barrel")
