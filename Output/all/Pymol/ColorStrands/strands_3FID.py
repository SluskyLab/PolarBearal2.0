from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FID.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3FID_A_S0", "resi 2-9 & chain A & 3FID ")
cmd.color ("red", "3FID_A_S0")


cmd.select("3FID_A_S1", "resi 32-45 & chain A & 3FID ")
cmd.color ("yellow", "3FID_A_S1")


cmd.select("3FID_A_S2", "resi 49-61 & chain A & 3FID ")
cmd.color ("green", "3FID_A_S2")


cmd.select("3FID_A_S3", "resi 80-93 & chain A & 3FID ")
cmd.color ("cyan", "3FID_A_S3")


cmd.select("3FID_A_S4", "resi 97-109 & chain A & 3FID ")
cmd.color ("blue", "3FID_A_S4")


cmd.select("3FID_A_S5", "resi 140-155 & chain A & 3FID ")
cmd.color ("magenta", "3FID_A_S5")


cmd.select("3FID_A_S6", "resi 161-172 & chain A & 3FID ")
cmd.color ("red", "3FID_A_S6")


cmd.select("3FID_A_S7", "resi 177-189 & chain A & 3FID ")
cmd.color ("yellow", "3FID_A_S7")


cmd.select("3FID_A_S8", "resi 216-229 & chain A & 3FID ")
cmd.color ("green", "3FID_A_S8")


cmd.select("3FID_A_S9", "resi 247-262 & chain A & 3FID ")
cmd.color ("cyan", "3FID_A_S9")


cmd.select("3FID_A_S10", "resi 265-280 & chain A & 3FID ")
cmd.color ("blue", "3FID_A_S10")


cmd.select("3FID_A_S11", "resi 285-295 & chain A & 3FID ")
cmd.color ("magenta", "3FID_A_S11")


cmd.select("3FID_barrel", "3FID_A_S*")
cmd.show("cartoon", "3FID_barrel")
cmd.zoom("3FID_barrel")
