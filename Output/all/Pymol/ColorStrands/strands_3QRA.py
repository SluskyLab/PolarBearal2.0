from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QRA.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3QRA_A_S0", "resi 30-41 & chain A & 3QRA ")
cmd.color ("red", "3QRA_A_S0")


cmd.select("3QRA_A_S1", "resi 49-63 & chain A & 3QRA ")
cmd.color ("yellow", "3QRA_A_S1")


cmd.select("3QRA_A_S2", "resi 67-78 & chain A & 3QRA ")
cmd.color ("green", "3QRA_A_S2")


cmd.select("3QRA_A_S3", "resi 91-107 & chain A & 3QRA ")
cmd.color ("cyan", "3QRA_A_S3")


cmd.select("3QRA_A_S4", "resi 110-127 & chain A & 3QRA ")
cmd.color ("blue", "3QRA_A_S4")


cmd.select("3QRA_A_S5", "resi 134-150 & chain A & 3QRA ")
cmd.color ("magenta", "3QRA_A_S5")


cmd.select("3QRA_A_S6", "resi 154-164 & chain A & 3QRA ")
cmd.color ("red", "3QRA_A_S6")


cmd.select("3QRA_A_S7", "resi 171-182 & chain A & 3QRA ")
cmd.color ("yellow", "3QRA_A_S7")


cmd.select("3QRA_barrel", "3QRA_A_S*")
cmd.show("cartoon", "3QRA_barrel")
cmd.zoom("3QRA_barrel")
