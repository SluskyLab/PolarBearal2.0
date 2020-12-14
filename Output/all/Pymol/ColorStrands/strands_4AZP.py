from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AZP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4AZP_A_S0", "resi 14-17 & chain A & 4AZP ")
cmd.color ("red", "4AZP_A_S0")


cmd.select("4AZP_A_S1", "resi 42-45 & chain A & 4AZP ")
cmd.color ("yellow", "4AZP_A_S1")


cmd.select("4AZP_A_S2", "resi 52-57 & chain A & 4AZP ")
cmd.color ("green", "4AZP_A_S2")


cmd.select("4AZP_A_S3", "resi 63-73 & chain A & 4AZP ")
cmd.color ("cyan", "4AZP_A_S3")


cmd.select("4AZP_A_S4", "resi 84-88 & chain A & 4AZP ")
cmd.color ("blue", "4AZP_A_S4")


cmd.select("4AZP_A_S5", "resi 94-99 & chain A & 4AZP ")
cmd.color ("magenta", "4AZP_A_S5")


cmd.select("4AZP_A_S6", "resi 105-110 & chain A & 4AZP ")
cmd.color ("red", "4AZP_A_S6")


cmd.select("4AZP_A_S7", "resi 116-121 & chain A & 4AZP ")
cmd.color ("yellow", "4AZP_A_S7")


cmd.select("4AZP_A_S8", "resi 127-134 & chain A & 4AZP ")
cmd.color ("green", "4AZP_A_S8")


cmd.select("4AZP_barrel", "4AZP_A_S*")
cmd.show("cartoon", "4AZP_barrel")
cmd.zoom("4AZP_barrel")
