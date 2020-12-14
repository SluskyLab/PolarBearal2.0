from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K7R.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4K7R_B_S0", "resi 82-95 & chain B & 4K7R ")
cmd.color ("red", "4K7R_B_S0")


cmd.select("4K7R_B_S1", "resi 101-116 & chain B & 4K7R ")
cmd.color ("yellow", "4K7R_B_S1")


cmd.select("4K7R_B_S2", "resi 288-301 & chain B & 4K7R ")
cmd.color ("green", "4K7R_B_S2")


cmd.select("4K7R_B_S3", "resi 313-323 & chain B & 4K7R ")
cmd.color ("cyan", "4K7R_B_S3")


cmd.select("4K7R_C_S0", "resi 82-95 & chain C & 4K7R ")
cmd.color ("red", "4K7R_C_S0")


cmd.select("4K7R_C_S1", "resi 101-116 & chain C & 4K7R ")
cmd.color ("yellow", "4K7R_C_S1")


cmd.select("4K7R_C_S2", "resi 288-301 & chain C & 4K7R ")
cmd.color ("green", "4K7R_C_S2")


cmd.select("4K7R_C_S3", "resi 313-323 & chain C & 4K7R ")
cmd.color ("cyan", "4K7R_C_S3")


cmd.select("4K7R_D_S0", "resi 82-95 & chain D & 4K7R ")
cmd.color ("red", "4K7R_D_S0")


cmd.select("4K7R_D_S1", "resi 101-116 & chain D & 4K7R ")
cmd.color ("yellow", "4K7R_D_S1")


cmd.select("4K7R_D_S2", "resi 288-301 & chain D & 4K7R ")
cmd.color ("green", "4K7R_D_S2")


cmd.select("4K7R_D_S3", "resi 313-323 & chain D & 4K7R ")
cmd.color ("cyan", "4K7R_D_S3")


cmd.select("4K7R_barrel", "4K7R_B_S* or 4K7R_C_S* or 4K7R_D_S*")
cmd.show("cartoon", "4K7R_barrel")
cmd.zoom("4K7R_barrel")
