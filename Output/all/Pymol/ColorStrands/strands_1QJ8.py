from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QJ8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QJ8_A_S0", "resi 2-14 & chain A & 1QJ8 ")
cmd.color ("red", "1QJ8_A_S0")


cmd.select("1QJ8_A_S1", "resi 18-31 & chain A & 1QJ8 ")
cmd.color ("yellow", "1QJ8_A_S1")


cmd.select("1QJ8_A_S2", "resi 38-50 & chain A & 1QJ8 ")
cmd.color ("green", "1QJ8_A_S2")


cmd.select("1QJ8_A_S3", "resi 57-73 & chain A & 1QJ8 ")
cmd.color ("cyan", "1QJ8_A_S3")


cmd.select("1QJ8_A_S4", "resi 76-93 & chain A & 1QJ8 ")
cmd.color ("blue", "1QJ8_A_S4")


cmd.select("1QJ8_A_S5", "resi 100-116 & chain A & 1QJ8 ")
cmd.color ("magenta", "1QJ8_A_S5")


cmd.select("1QJ8_A_S6", "resi 120-131 & chain A & 1QJ8 ")
cmd.color ("red", "1QJ8_A_S6")


cmd.select("1QJ8_A_S7", "resi 137-148 & chain A & 1QJ8 ")
cmd.color ("yellow", "1QJ8_A_S7")


cmd.select("1QJ8_barrel", "1QJ8_A_S*")
cmd.show("cartoon", "1QJ8_barrel")
cmd.zoom("1QJ8_barrel")
