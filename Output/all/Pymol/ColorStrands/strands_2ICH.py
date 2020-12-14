from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICH.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2ICH_A_S0", "resi 227-233 & chain A & 2ICH ")
cmd.color ("red", "2ICH_A_S0")


cmd.select("2ICH_A_S1", "resi 240-247 & chain A & 2ICH ")
cmd.color ("yellow", "2ICH_A_S1")


cmd.select("2ICH_A_S2", "resi 254-261 & chain A & 2ICH ")
cmd.color ("green", "2ICH_A_S2")


cmd.select("2ICH_A_S3", "resi 268-283 & chain A & 2ICH ")
cmd.color ("cyan", "2ICH_A_S3")


cmd.select("2ICH_A_S4", "resi 292-299 & chain A & 2ICH ")
cmd.color ("blue", "2ICH_A_S4")


cmd.select("2ICH_A_S5", "resi 304-318 & chain A & 2ICH ")
cmd.color ("magenta", "2ICH_A_S5")


cmd.select("2ICH_A_S6", "resi 324-336 & chain A & 2ICH ")
cmd.color ("red", "2ICH_A_S6")


cmd.select("2ICH_A_S7", "resi 340-347 & chain A & 2ICH ")
cmd.color ("yellow", "2ICH_A_S7")


cmd.select("2ICH_barrel", "2ICH_A_S*")
cmd.show("cartoon", "2ICH_barrel")
cmd.zoom("2ICH_barrel")
