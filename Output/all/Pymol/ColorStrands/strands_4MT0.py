from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MT0.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4MT0_B_S0", "resi 99-113 & chain B & 4MT0 ")
cmd.color ("red", "4MT0_B_S0")


cmd.select("4MT0_B_S1", "resi 117-130 & chain B & 4MT0 ")
cmd.color ("yellow", "4MT0_B_S1")


cmd.select("4MT0_B_S2", "resi 306-319 & chain B & 4MT0 ")
cmd.color ("green", "4MT0_B_S2")


cmd.select("4MT0_B_S3", "resi 332-341 & chain B & 4MT0 ")
cmd.color ("cyan", "4MT0_B_S3")


cmd.select("4MT0_C_S0", "resi 99-113 & chain C & 4MT0 ")
cmd.color ("red", "4MT0_C_S0")


cmd.select("4MT0_C_S1", "resi 117-130 & chain C & 4MT0 ")
cmd.color ("yellow", "4MT0_C_S1")


cmd.select("4MT0_C_S2", "resi 306-319 & chain C & 4MT0 ")
cmd.color ("green", "4MT0_C_S2")


cmd.select("4MT0_C_S3", "resi 332-341 & chain C & 4MT0 ")
cmd.color ("cyan", "4MT0_C_S3")


cmd.select("4MT0_D_S0", "resi 99-113 & chain D & 4MT0 ")
cmd.color ("red", "4MT0_D_S0")


cmd.select("4MT0_D_S1", "resi 117-130 & chain D & 4MT0 ")
cmd.color ("yellow", "4MT0_D_S1")


cmd.select("4MT0_D_S2", "resi 306-319 & chain D & 4MT0 ")
cmd.color ("green", "4MT0_D_S2")


cmd.select("4MT0_D_S3", "resi 332-341 & chain D & 4MT0 ")
cmd.color ("cyan", "4MT0_D_S3")


cmd.select("4MT0_barrel", "4MT0_B_S* or 4MT0_C_S* or 4MT0_D_S*")
cmd.show("cartoon", "4MT0_barrel")
cmd.zoom("4MT0_barrel")
