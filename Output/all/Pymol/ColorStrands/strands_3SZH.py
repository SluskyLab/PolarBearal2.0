from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZH.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SZH_A_S0", "resi 11-14 & chain A & 3SZH ")
cmd.color ("red", "3SZH_A_S0")


cmd.select("3SZH_A_S1", "resi 20-25 & chain A & 3SZH ")
cmd.color ("yellow", "3SZH_A_S1")


cmd.select("3SZH_A_S2", "resi 30-37 & chain A & 3SZH ")
cmd.color ("green", "3SZH_A_S2")


cmd.select("3SZH_A_S3", "resi 50-56 & chain A & 3SZH ")
cmd.color ("cyan", "3SZH_A_S3")


cmd.select("3SZH_A_S4", "resi 61-67 & chain A & 3SZH ")
cmd.color ("blue", "3SZH_A_S4")


cmd.select("3SZH_A_S5", "resi 76-85 & chain A & 3SZH ")
cmd.color ("magenta", "3SZH_A_S5")


cmd.select("3SZH_A_S6", "resi 92-100 & chain A & 3SZH ")
cmd.color ("red", "3SZH_A_S6")


cmd.select("3SZH_A_S7", "resi 111-121 & chain A & 3SZH ")
cmd.color ("yellow", "3SZH_A_S7")


cmd.select("3SZH_barrel", "3SZH_A_S*")
cmd.show("cartoon", "3SZH_barrel")
cmd.zoom("3SZH_barrel")
