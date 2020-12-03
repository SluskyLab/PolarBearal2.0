from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QJP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QJP_A_S0", "resi 6-16 & chain A & 1QJP ")
cmd.color ("red", "1QJP_A_S0")


cmd.select("1QJP_A_S1", "resi 33-45 & chain A & 1QJP ")
cmd.color ("yellow", "1QJP_A_S1")


cmd.select("1QJP_A_S2", "resi 48-60 & chain A & 1QJP ")
cmd.color ("green", "1QJP_A_S2")


cmd.select("1QJP_A_S3", "resi 71-85 & chain A & 1QJP ")
cmd.color ("cyan", "1QJP_A_S3")


cmd.select("1QJP_A_S4", "resi 91-108 & chain A & 1QJP ")
cmd.color ("blue", "1QJP_A_S4")


cmd.select("1QJP_A_S5", "resi 112-131 & chain A & 1QJP ")
cmd.color ("magenta", "1QJP_A_S5")


cmd.select("1QJP_A_S6", "resi 134-143 & chain A & 1QJP ")
cmd.color ("red", "1QJP_A_S6")


cmd.select("1QJP_A_S7", "resi 161-170 & chain A & 1QJP ")
cmd.color ("yellow", "1QJP_A_S7")


cmd.select("1QJP_barrel", "1QJP_A_S*")
cmd.show("cartoon", "1QJP_barrel")
cmd.zoom("1QJP_barrel")
