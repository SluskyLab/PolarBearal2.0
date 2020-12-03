from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ERV.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2ERV_A_S0", "resi 2-9 & chain A & 2ERV ")
cmd.color ("red", "2ERV_A_S0")


cmd.select("2ERV_A_S1", "resi 16-29 & chain A & 2ERV ")
cmd.color ("yellow", "2ERV_A_S1")


cmd.select("2ERV_A_S2", "resi 36-48 & chain A & 2ERV ")
cmd.color ("green", "2ERV_A_S2")


cmd.select("2ERV_A_S3", "resi 54-69 & chain A & 2ERV ")
cmd.color ("cyan", "2ERV_A_S3")


cmd.select("2ERV_A_S4", "resi 76-89 & chain A & 2ERV ")
cmd.color ("blue", "2ERV_A_S4")


cmd.select("2ERV_A_S5", "resi 103-113 & chain A & 2ERV ")
cmd.color ("magenta", "2ERV_A_S5")


cmd.select("2ERV_A_S6", "resi 119-128 & chain A & 2ERV ")
cmd.color ("red", "2ERV_A_S6")


cmd.select("2ERV_A_S7", "resi 139-148 & chain A & 2ERV ")
cmd.color ("yellow", "2ERV_A_S7")


cmd.select("2ERV_barrel", "2ERV_A_S*")
cmd.show("cartoon", "2ERV_barrel")
cmd.zoom("2ERV_barrel")
