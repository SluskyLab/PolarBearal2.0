from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1T16.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1T16_A_S0", "resi 43-60 & chain A & 1T16 ")
cmd.color ("red", "1T16_A_S0")


cmd.select("1T16_A_S1", "resi 68-88 & chain A & 1T16 ")
cmd.color ("yellow", "1T16_A_S1")


cmd.select("1T16_A_S2", "resi 92-108 & chain A & 1T16 ")
cmd.color ("green", "1T16_A_S2")


cmd.select("1T16_A_S3", "resi 115-134 & chain A & 1T16 ")
cmd.color ("cyan", "1T16_A_S3")


cmd.select("1T16_A_S4", "resi 141-158 & chain A & 1T16 ")
cmd.color ("blue", "1T16_A_S4")


cmd.select("1T16_A_S5", "resi 197-217 & chain A & 1T16 ")
cmd.color ("magenta", "1T16_A_S5")


cmd.select("1T16_A_S6", "resi 221-241 & chain A & 1T16 ")
cmd.color ("red", "1T16_A_S6")


cmd.select("1T16_A_S7", "resi 260-283 & chain A & 1T16 ")
cmd.color ("yellow", "1T16_A_S7")


cmd.select("1T16_A_S8", "resi 287-307 & chain A & 1T16 ")
cmd.color ("green", "1T16_A_S8")


cmd.select("1T16_A_S9", "resi 315-335 & chain A & 1T16 ")
cmd.color ("cyan", "1T16_A_S9")


cmd.select("1T16_A_S10", "resi 339-351 & chain A & 1T16 ")
cmd.color ("blue", "1T16_A_S10")


cmd.select("1T16_A_S11", "resi 366-377 & chain A & 1T16 ")
cmd.color ("magenta", "1T16_A_S11")


cmd.select("1T16_A_S12", "resi 380-397 & chain A & 1T16 ")
cmd.color ("red", "1T16_A_S12")


cmd.select("1T16_A_S13", "resi 404-421 & chain A & 1T16 ")
cmd.color ("yellow", "1T16_A_S13")


cmd.select("1T16_barrel", "1T16_A_S*")
cmd.show("cartoon", "1T16_barrel")
cmd.zoom("1T16_barrel")
