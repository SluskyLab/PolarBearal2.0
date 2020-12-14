from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A0A.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2A0A_A_S0", "resi 7-9 & chain A & 2A0A ")
cmd.color ("red", "2A0A_A_S0")


cmd.select("2A0A_A_S1", "resi 50-53 & chain A & 2A0A ")
cmd.color ("yellow", "2A0A_A_S1")


cmd.select("2A0A_A_S2", "resi 67-70 & chain A & 2A0A ")
cmd.color ("green", "2A0A_A_S2")


cmd.select("2A0A_A_S3", "resi 78-85 & chain A & 2A0A ")
cmd.color ("cyan", "2A0A_A_S3")


cmd.select("2A0A_A_S4", "resi 92-96 & chain A & 2A0A ")
cmd.color ("blue", "2A0A_A_S4")


cmd.select("2A0A_A_S5", "resi 102-107 & chain A & 2A0A ")
cmd.color ("magenta", "2A0A_A_S5")


cmd.select("2A0A_A_S6", "resi 113-118 & chain A & 2A0A ")
cmd.color ("red", "2A0A_A_S6")


cmd.select("2A0A_A_S7", "resi 124-131 & chain A & 2A0A ")
cmd.color ("yellow", "2A0A_A_S7")


cmd.select("2A0A_barrel", "2A0A_A_S*")
cmd.show("cartoon", "2A0A_barrel")
cmd.zoom("2A0A_barrel")
