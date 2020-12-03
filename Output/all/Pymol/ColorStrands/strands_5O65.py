from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O65.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5O65_A_S0", "resi 108-119 & chain A & 5O65 ")
cmd.color ("red", "5O65_A_S0")


cmd.select("5O65_A_S1", "resi 143-160 & chain A & 5O65 ")
cmd.color ("yellow", "5O65_A_S1")


cmd.select("5O65_A_S2", "resi 164-180 & chain A & 5O65 ")
cmd.color ("green", "5O65_A_S2")


cmd.select("5O65_A_S3", "resi 197-215 & chain A & 5O65 ")
cmd.color ("cyan", "5O65_A_S3")


cmd.select("5O65_A_S4", "resi 223-232 & chain A & 5O65 ")
cmd.color ("blue", "5O65_A_S4")


cmd.select("5O65_A_S5", "resi 266-275 & chain A & 5O65 ")
cmd.color ("magenta", "5O65_A_S5")


cmd.select("5O65_A_S6", "resi 281-299 & chain A & 5O65 ")
cmd.color ("red", "5O65_A_S6")


cmd.select("5O65_A_S7", "resi 307-327 & chain A & 5O65 ")
cmd.color ("yellow", "5O65_A_S7")


cmd.select("5O65_A_S8", "resi 331-348 & chain A & 5O65 ")
cmd.color ("green", "5O65_A_S8")


cmd.select("5O65_A_S9", "resi 355-375 & chain A & 5O65 ")
cmd.color ("cyan", "5O65_A_S9")


cmd.select("5O65_A_S10", "resi 379-389 & chain A & 5O65 ")
cmd.color ("blue", "5O65_A_S10")


cmd.select("5O65_A_S11", "resi 397-406 & chain A & 5O65 ")
cmd.color ("magenta", "5O65_A_S11")


cmd.select("5O65_barrel", "5O65_A_S*")
cmd.show("cartoon", "5O65_barrel")
cmd.zoom("5O65_barrel")
