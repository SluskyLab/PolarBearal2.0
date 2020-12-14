from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3HPE.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3HPE_A_S0", "resi 21-35 & chain A & 3HPE ")
cmd.color ("red", "3HPE_A_S0")


cmd.select("3HPE_A_S1", "resi 39-55 & chain A & 3HPE ")
cmd.color ("yellow", "3HPE_A_S1")


cmd.select("3HPE_A_S2", "resi 59-74 & chain A & 3HPE ")
cmd.color ("green", "3HPE_A_S2")


cmd.select("3HPE_A_S3", "resi 98-104 & chain A & 3HPE ")
cmd.color ("cyan", "3HPE_A_S3")


cmd.select("3HPE_A_S4", "resi 108-115 & chain A & 3HPE ")
cmd.color ("blue", "3HPE_A_S4")


cmd.select("3HPE_A_S5", "resi 121-133 & chain A & 3HPE ")
cmd.color ("magenta", "3HPE_A_S5")


cmd.select("3HPE_A_S6", "resi 142-151 & chain A & 3HPE ")
cmd.color ("red", "3HPE_A_S6")


cmd.select("3HPE_A_S7", "resi 171-180 & chain A & 3HPE ")
cmd.color ("yellow", "3HPE_A_S7")


cmd.select("3HPE_barrel", "3HPE_A_S*")
cmd.show("cartoon", "3HPE_barrel")
cmd.zoom("3HPE_barrel")
