from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FQE.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FQE_A_S0", "resi 1-9 & chain A & 4FQE ")
cmd.color ("red", "4FQE_A_S0")


cmd.select("4FQE_A_S1", "resi 17-25 & chain A & 4FQE ")
cmd.color ("yellow", "4FQE_A_S1")


cmd.select("4FQE_A_S2", "resi 32-41 & chain A & 4FQE ")
cmd.color ("green", "4FQE_A_S2")


cmd.select("4FQE_A_S3", "resi 58-70 & chain A & 4FQE ")
cmd.color ("cyan", "4FQE_A_S3")


cmd.select("4FQE_A_S4", "resi 74-86 & chain A & 4FQE ")
cmd.color ("blue", "4FQE_A_S4")


cmd.select("4FQE_A_S5", "resi 89-101 & chain A & 4FQE ")
cmd.color ("magenta", "4FQE_A_S5")


cmd.select("4FQE_A_S6", "resi 104-117 & chain A & 4FQE ")
cmd.color ("red", "4FQE_A_S6")


cmd.select("4FQE_A_S7", "resi 130-142 & chain A & 4FQE ")
cmd.color ("yellow", "4FQE_A_S7")


cmd.select("4FQE_A_S8", "resi 146-158 & chain A & 4FQE ")
cmd.color ("green", "4FQE_A_S8")


cmd.select("4FQE_A_S9", "resi 171-182 & chain A & 4FQE ")
cmd.color ("cyan", "4FQE_A_S9")


cmd.select("4FQE_A_S10", "resi 185-196 & chain A & 4FQE ")
cmd.color ("blue", "4FQE_A_S10")


cmd.select("4FQE_A_S11", "resi 207-215 & chain A & 4FQE ")
cmd.color ("magenta", "4FQE_A_S11")


cmd.select("4FQE_barrel", "4FQE_A_S*")
cmd.show("cartoon", "4FQE_barrel")
cmd.zoom("4FQE_barrel")
