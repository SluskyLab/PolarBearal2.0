from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H6B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4H6B_A_S0", "resi 12-30 & chain A & 4H6B ")
cmd.color ("red", "4H6B_A_S0")


cmd.select("4H6B_A_S1", "resi 50-59 & chain A & 4H6B ")
cmd.color ("yellow", "4H6B_A_S1")


cmd.select("4H6B_A_S2", "resi 66-79 & chain A & 4H6B ")
cmd.color ("green", "4H6B_A_S2")


cmd.select("4H6B_A_S3", "resi 83-94 & chain A & 4H6B ")
cmd.color ("cyan", "4H6B_A_S3")


cmd.select("4H6B_A_S4", "resi 100-109 & chain A & 4H6B ")
cmd.color ("blue", "4H6B_A_S4")


cmd.select("4H6B_A_S5", "resi 113-121 & chain A & 4H6B ")
cmd.color ("magenta", "4H6B_A_S5")


cmd.select("4H6B_A_S6", "resi 128-137 & chain A & 4H6B ")
cmd.color ("red", "4H6B_A_S6")


cmd.select("4H6B_A_S7", "resi 141-149 & chain A & 4H6B ")
cmd.color ("yellow", "4H6B_A_S7")


cmd.select("4H6B_barrel", "4H6B_A_S*")
cmd.show("cartoon", "4H6B_barrel")
cmd.zoom("4H6B_barrel")
