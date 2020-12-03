from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QD5.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QD5_A_S0", "resi 35-46 & chain A & 1QD5 ")
cmd.color ("red", "1QD5_A_S0")


cmd.select("1QD5_A_S1", "resi 66-80 & chain A & 1QD5 ")
cmd.color ("yellow", "1QD5_A_S1")


cmd.select("1QD5_A_S2", "resi 86-97 & chain A & 1QD5 ")
cmd.color ("green", "1QD5_A_S2")


cmd.select("1QD5_A_S3", "resi 110-124 & chain A & 1QD5 ")
cmd.color ("cyan", "1QD5_A_S3")


cmd.select("1QD5_A_S4", "resi 132-145 & chain A & 1QD5 ")
cmd.color ("blue", "1QD5_A_S4")


cmd.select("1QD5_A_S5", "resi 153-165 & chain A & 1QD5 ")
cmd.color ("magenta", "1QD5_A_S5")


cmd.select("1QD5_A_S6", "resi 168-179 & chain A & 1QD5 ")
cmd.color ("red", "1QD5_A_S6")


cmd.select("1QD5_A_S7", "resi 194-202 & chain A & 1QD5 ")
cmd.color ("yellow", "1QD5_A_S7")


cmd.select("1QD5_A_S8", "resi 207-213 & chain A & 1QD5 ")
cmd.color ("green", "1QD5_A_S8")


cmd.select("1QD5_A_S9", "resi 221-229 & chain A & 1QD5 ")
cmd.color ("cyan", "1QD5_A_S9")


cmd.select("1QD5_A_S10", "resi 235-245 & chain A & 1QD5 ")
cmd.color ("blue", "1QD5_A_S10")


cmd.select("1QD5_A_S11", "resi 256-265 & chain A & 1QD5 ")
cmd.color ("magenta", "1QD5_A_S11")


cmd.select("1QD5_barrel", "1QD5_A_S*")
cmd.show("cartoon", "1QD5_barrel")
cmd.zoom("1QD5_barrel")
