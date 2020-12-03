from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FUV.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FUV_A_S0", "resi 19-27 & chain A & 4FUV ")
cmd.color ("red", "4FUV_A_S0")


cmd.select("4FUV_A_S1", "resi 30-38 & chain A & 4FUV ")
cmd.color ("yellow", "4FUV_A_S1")


cmd.select("4FUV_A_S2", "resi 41-55 & chain A & 4FUV ")
cmd.color ("green", "4FUV_A_S2")


cmd.select("4FUV_A_S3", "resi 65-82 & chain A & 4FUV ")
cmd.color ("cyan", "4FUV_A_S3")


cmd.select("4FUV_A_S4", "resi 94-114 & chain A & 4FUV ")
cmd.color ("blue", "4FUV_A_S4")


cmd.select("4FUV_A_S5", "resi 130-158 & chain A & 4FUV ")
cmd.color ("magenta", "4FUV_A_S5")


cmd.select("4FUV_A_S6", "resi 161-185 & chain A & 4FUV ")
cmd.color ("red", "4FUV_A_S6")


cmd.select("4FUV_A_S7", "resi 214-224 & chain A & 4FUV ")
cmd.color ("yellow", "4FUV_A_S7")


cmd.select("4FUV_barrel", "4FUV_A_S*")
cmd.show("cartoon", "4FUV_barrel")
cmd.zoom("4FUV_barrel")
