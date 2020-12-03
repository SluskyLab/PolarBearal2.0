from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X27.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2X27_X_S0", "resi 10-29 & chain X & 2X27 ")
cmd.color ("red", "2X27_X_S0")


cmd.select("2X27_X_S1", "resi 39-56 & chain X & 2X27 ")
cmd.color ("yellow", "2X27_X_S1")


cmd.select("2X27_X_S2", "resi 59-77 & chain X & 2X27 ")
cmd.color ("green", "2X27_X_S2")


cmd.select("2X27_X_S3", "resi 85-102 & chain X & 2X27 ")
cmd.color ("cyan", "2X27_X_S3")


cmd.select("2X27_X_S4", "resi 112-128 & chain X & 2X27 ")
cmd.color ("blue", "2X27_X_S4")


cmd.select("2X27_X_S5", "resi 139-157 & chain X & 2X27 ")
cmd.color ("magenta", "2X27_X_S5")


cmd.select("2X27_X_S6", "resi 162-181 & chain X & 2X27 ")
cmd.color ("red", "2X27_X_S6")


cmd.select("2X27_X_S7", "resi 191-210 & chain X & 2X27 ")
cmd.color ("yellow", "2X27_X_S7")


cmd.select("2X27_barrel", "2X27_X_S*")
cmd.show("cartoon", "2X27_barrel")
cmd.zoom("2X27_barrel")
