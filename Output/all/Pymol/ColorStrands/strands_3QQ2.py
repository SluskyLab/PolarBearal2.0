from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QQ2.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3QQ2_A_S0", "resi 748-760 & chain A & 3QQ2 ")
cmd.color ("red", "3QQ2_A_S0")


cmd.select("3QQ2_A_S1", "resi 768-783 & chain A & 3QQ2 ")
cmd.color ("yellow", "3QQ2_A_S1")


cmd.select("3QQ2_A_S2", "resi 789-805 & chain A & 3QQ2 ")
cmd.color ("green", "3QQ2_A_S2")


cmd.select("3QQ2_A_S3", "resi 809-825 & chain A & 3QQ2 ")
cmd.color ("cyan", "3QQ2_A_S3")


cmd.select("3QQ2_A_S4", "resi 829-847 & chain A & 3QQ2 ")
cmd.color ("blue", "3QQ2_A_S4")


cmd.select("3QQ2_A_S5", "resi 855-876 & chain A & 3QQ2 ")
cmd.color ("magenta", "3QQ2_A_S5")


cmd.select("3QQ2_A_S6", "resi 880-900 & chain A & 3QQ2 ")
cmd.color ("red", "3QQ2_A_S6")


cmd.select("3QQ2_A_S7", "resi 904-926 & chain A & 3QQ2 ")
cmd.color ("yellow", "3QQ2_A_S7")


cmd.select("3QQ2_A_S8", "resi 933-948 & chain A & 3QQ2 ")
cmd.color ("green", "3QQ2_A_S8")


cmd.select("3QQ2_A_S9", "resi 967-977 & chain A & 3QQ2 ")
cmd.color ("cyan", "3QQ2_A_S9")


cmd.select("3QQ2_A_S10", "resi 983-992 & chain A & 3QQ2 ")
cmd.color ("blue", "3QQ2_A_S10")


cmd.select("3QQ2_A_S11", "resi 998-1008 & chain A & 3QQ2 ")
cmd.color ("magenta", "3QQ2_A_S11")


cmd.select("3QQ2_barrel", "3QQ2_A_S*")
cmd.show("cartoon", "3QQ2_barrel")
cmd.zoom("3QQ2_barrel")
