from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5AZP_A_S0", "resi 79-93 & chain A & 5AZP ")
cmd.color ("red", "5AZP_A_S0")


cmd.select("5AZP_A_S1", "resi 102-117 & chain A & 5AZP ")
cmd.color ("yellow", "5AZP_A_S1")


cmd.select("5AZP_A_S2", "resi 290-303 & chain A & 5AZP ")
cmd.color ("green", "5AZP_A_S2")


cmd.select("5AZP_A_S3", "resi 316-325 & chain A & 5AZP ")
cmd.color ("cyan", "5AZP_A_S3")


cmd.select("5AZP_B_S0", "resi 79-93 & chain B & 5AZP ")
cmd.color ("red", "5AZP_B_S0")


cmd.select("5AZP_B_S1", "resi 102-117 & chain B & 5AZP ")
cmd.color ("yellow", "5AZP_B_S1")


cmd.select("5AZP_B_S2", "resi 290-303 & chain B & 5AZP ")
cmd.color ("green", "5AZP_B_S2")


cmd.select("5AZP_B_S3", "resi 316-325 & chain B & 5AZP ")
cmd.color ("cyan", "5AZP_B_S3")


cmd.select("5AZP_C_S0", "resi 79-93 & chain C & 5AZP ")
cmd.color ("red", "5AZP_C_S0")


cmd.select("5AZP_C_S1", "resi 103-117 & chain C & 5AZP ")
cmd.color ("yellow", "5AZP_C_S1")


cmd.select("5AZP_C_S2", "resi 290-303 & chain C & 5AZP ")
cmd.color ("green", "5AZP_C_S2")


cmd.select("5AZP_C_S3", "resi 316-325 & chain C & 5AZP ")
cmd.color ("cyan", "5AZP_C_S3")


cmd.select("5AZP_barrel", "5AZP_A_S* or 5AZP_B_S* or 5AZP_C_S*")
cmd.show("cartoon", "5AZP_barrel")
cmd.zoom("5AZP_barrel")
