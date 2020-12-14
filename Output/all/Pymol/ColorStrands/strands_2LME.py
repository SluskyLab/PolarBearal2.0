from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2LME_A_S0", "resi 53-63 & chain A & 2LME ")
cmd.color ("red", "2LME_A_S0")


cmd.select("2LME_A_S1", "resi 66-77 & chain A & 2LME ")
cmd.color ("yellow", "2LME_A_S1")


cmd.select("2LME_A_S2", "resi 81-90 & chain A & 2LME ")
cmd.color ("green", "2LME_A_S2")


cmd.select("2LME_A_S3", "resi 94-104 & chain A & 2LME ")
cmd.color ("cyan", "2LME_A_S3")


cmd.select("2LME_B_S0", "resi 53-63 & chain B & 2LME ")
cmd.color ("red", "2LME_B_S0")


cmd.select("2LME_B_S1", "resi 66-77 & chain B & 2LME ")
cmd.color ("yellow", "2LME_B_S1")


cmd.select("2LME_B_S2", "resi 81-90 & chain B & 2LME ")
cmd.color ("green", "2LME_B_S2")


cmd.select("2LME_B_S3", "resi 94-104 & chain B & 2LME ")
cmd.color ("cyan", "2LME_B_S3")


cmd.select("2LME_C_S0", "resi 53-63 & chain C & 2LME ")
cmd.color ("red", "2LME_C_S0")


cmd.select("2LME_C_S1", "resi 66-77 & chain C & 2LME ")
cmd.color ("yellow", "2LME_C_S1")


cmd.select("2LME_C_S2", "resi 81-90 & chain C & 2LME ")
cmd.color ("green", "2LME_C_S2")


cmd.select("2LME_C_S3", "resi 94-104 & chain C & 2LME ")
cmd.color ("cyan", "2LME_C_S3")


cmd.select("2LME_barrel", "2LME_A_S* or 2LME_B_S* or 2LME_C_S*")
cmd.show("cartoon", "2LME_barrel")
cmd.zoom("2LME_barrel")
