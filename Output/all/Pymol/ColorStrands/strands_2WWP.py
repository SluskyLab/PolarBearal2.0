from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2WWP_A_S0", "resi 41-49 & chain A & 2WWP ")
cmd.color ("red", "2WWP_A_S0")


cmd.select("2WWP_A_S1", "resi 65-70 & chain A & 2WWP ")
cmd.color ("yellow", "2WWP_A_S1")


cmd.select("2WWP_A_S2", "resi 76-83 & chain A & 2WWP ")
cmd.color ("green", "2WWP_A_S2")


cmd.select("2WWP_A_S3", "resi 90-99 & chain A & 2WWP ")
cmd.color ("cyan", "2WWP_A_S3")


cmd.select("2WWP_A_S4", "resi 104-109 & chain A & 2WWP ")
cmd.color ("blue", "2WWP_A_S4")


cmd.select("2WWP_A_S5", "resi 113-124 & chain A & 2WWP ")
cmd.color ("magenta", "2WWP_A_S5")


cmd.select("2WWP_A_S6", "resi 128-137 & chain A & 2WWP ")
cmd.color ("red", "2WWP_A_S6")


cmd.select("2WWP_A_S7", "resi 145-150 & chain A & 2WWP ")
cmd.color ("yellow", "2WWP_A_S7")


cmd.select("2WWP_barrel", "2WWP_A_S*")
cmd.show("cartoon", "2WWP_barrel")
cmd.zoom("2WWP_barrel")
