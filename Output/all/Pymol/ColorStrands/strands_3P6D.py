from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3P6D.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3P6D_A_S0", "resi 11-14 & chain A & 3P6D ")
cmd.color ("red", "3P6D_A_S0")


cmd.select("3P6D_A_S1", "resi 39-42 & chain A & 3P6D ")
cmd.color ("yellow", "3P6D_A_S1")


cmd.select("3P6D_A_S2", "resi 50-54 & chain A & 3P6D ")
cmd.color ("green", "3P6D_A_S2")


cmd.select("3P6D_A_S3", "resi 60-67 & chain A & 3P6D ")
cmd.color ("cyan", "3P6D_A_S3")


cmd.select("3P6D_A_S4", "resi 81-84 & chain A & 3P6D ")
cmd.color ("blue", "3P6D_A_S4")


cmd.select("3P6D_A_S5", "resi 91-96 & chain A & 3P6D ")
cmd.color ("magenta", "3P6D_A_S5")


cmd.select("3P6D_A_S6", "resi 102-107 & chain A & 3P6D ")
cmd.color ("red", "3P6D_A_S6")


cmd.select("3P6D_A_S7", "resi 113-118 & chain A & 3P6D ")
cmd.color ("yellow", "3P6D_A_S7")


cmd.select("3P6D_A_S8", "resi 124-131 & chain A & 3P6D ")
cmd.color ("green", "3P6D_A_S8")


cmd.select("3P6D_barrel", "3P6D_A_S*")
cmd.show("cartoon", "3P6D_barrel")
cmd.zoom("3P6D_barrel")
