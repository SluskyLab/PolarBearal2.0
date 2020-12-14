from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3S26.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3S26_A_S0", "resi 31-39 & chain A & 3S26 ")
cmd.color ("red", "3S26_A_S0")


cmd.select("3S26_A_S1", "resi 52-57 & chain A & 3S26 ")
cmd.color ("yellow", "3S26_A_S1")


cmd.select("3S26_A_S2", "resi 64-70 & chain A & 3S26 ")
cmd.color ("green", "3S26_A_S2")


cmd.select("3S26_A_S3", "resi 81-88 & chain A & 3S26 ")
cmd.color ("cyan", "3S26_A_S3")


cmd.select("3S26_A_S4", "resi 93-97 & chain A & 3S26 ")
cmd.color ("blue", "3S26_A_S4")


cmd.select("3S26_A_S5", "resi 106-116 & chain A & 3S26 ")
cmd.color ("magenta", "3S26_A_S5")


cmd.select("3S26_A_S6", "resi 120-128 & chain A & 3S26 ")
cmd.color ("red", "3S26_A_S6")


cmd.select("3S26_A_S7", "resi 134-169 & chain A & 3S26 ")
cmd.color ("yellow", "3S26_A_S7")


cmd.select("3S26_barrel", "3S26_A_S*")
cmd.show("cartoon", "3S26_barrel")
cmd.zoom("3S26_barrel")
