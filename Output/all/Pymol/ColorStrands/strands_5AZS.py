from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZS.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5AZS_A_S0", "resi 80-94 & chain A & 5AZS ")
cmd.color ("red", "5AZS_A_S0")


cmd.select("5AZS_A_S1", "resi 103-116 & chain A & 5AZS ")
cmd.color ("yellow", "5AZS_A_S1")


cmd.select("5AZS_A_S2", "resi 293-306 & chain A & 5AZS ")
cmd.color ("green", "5AZS_A_S2")


cmd.select("5AZS_A_S3", "resi 319-328 & chain A & 5AZS ")
cmd.color ("cyan", "5AZS_A_S3")


cmd.select("5AZS_B_S0", "resi 80-94 & chain B & 5AZS ")
cmd.color ("red", "5AZS_B_S0")


cmd.select("5AZS_B_S1", "resi 103-116 & chain B & 5AZS ")
cmd.color ("yellow", "5AZS_B_S1")


cmd.select("5AZS_B_S2", "resi 295-306 & chain B & 5AZS ")
cmd.color ("green", "5AZS_B_S2")


cmd.select("5AZS_B_S3", "resi 319-329 & chain B & 5AZS ")
cmd.color ("cyan", "5AZS_B_S3")


cmd.select("5AZS_C_S0", "resi 80-94 & chain C & 5AZS ")
cmd.color ("red", "5AZS_C_S0")


cmd.select("5AZS_C_S1", "resi 105-117 & chain C & 5AZS ")
cmd.color ("yellow", "5AZS_C_S1")


cmd.select("5AZS_C_S2", "resi 293-306 & chain C & 5AZS ")
cmd.color ("green", "5AZS_C_S2")


cmd.select("5AZS_C_S3", "resi 319-329 & chain C & 5AZS ")
cmd.color ("cyan", "5AZS_C_S3")


cmd.select("5AZS_barrel", "5AZS_A_S* or 5AZS_B_S* or 5AZS_C_S*")
cmd.show("cartoon", "5AZS_barrel")
cmd.zoom("5AZS_barrel")
