from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AQB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1AQB_A_S0", "resi 24-30 & chain A & 1AQB ")
cmd.color ("red", "1AQB_A_S0")


cmd.select("1AQB_A_S1", "resi 39-46 & chain A & 1AQB ")
cmd.color ("yellow", "1AQB_A_S1")


cmd.select("1AQB_A_S2", "resi 53-61 & chain A & 1AQB ")
cmd.color ("green", "1AQB_A_S2")


cmd.select("1AQB_A_S3", "resi 69-77 & chain A & 1AQB ")
cmd.color ("cyan", "1AQB_A_S3")


cmd.select("1AQB_A_S4", "resi 86-91 & chain A & 1AQB ")
cmd.color ("blue", "1AQB_A_S4")


cmd.select("1AQB_A_S5", "resi 100-110 & chain A & 1AQB ")
cmd.color ("magenta", "1AQB_A_S5")


cmd.select("1AQB_A_S6", "resi 114-122 & chain A & 1AQB ")
cmd.color ("red", "1AQB_A_S6")


cmd.select("1AQB_A_S7", "resi 131-168 & chain A & 1AQB ")
cmd.color ("yellow", "1AQB_A_S7")


cmd.select("1AQB_barrel", "1AQB_A_S*")
cmd.show("cartoon", "1AQB_barrel")
cmd.zoom("1AQB_barrel")
