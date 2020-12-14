from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QFT.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QFT_A_S0", "resi 29-35 & chain A & 1QFT ")
cmd.color ("red", "1QFT_A_S0")


cmd.select("1QFT_A_S1", "resi 47-57 & chain A & 1QFT ")
cmd.color ("yellow", "1QFT_A_S1")


cmd.select("1QFT_A_S2", "resi 61-70 & chain A & 1QFT ")
cmd.color ("green", "1QFT_A_S2")


cmd.select("1QFT_A_S3", "resi 78-87 & chain A & 1QFT ")
cmd.color ("cyan", "1QFT_A_S3")


cmd.select("1QFT_A_S4", "resi 96-101 & chain A & 1QFT ")
cmd.color ("blue", "1QFT_A_S4")


cmd.select("1QFT_A_S5", "resi 108-114 & chain A & 1QFT ")
cmd.color ("magenta", "1QFT_A_S5")


cmd.select("1QFT_A_S6", "resi 120-124 & chain A & 1QFT ")
cmd.color ("red", "1QFT_A_S6")


cmd.select("1QFT_A_S7", "resi 133-138 & chain A & 1QFT ")
cmd.color ("yellow", "1QFT_A_S7")


cmd.select("1QFT_barrel", "1QFT_A_S*")
cmd.show("cartoon", "1QFT_barrel")
cmd.zoom("1QFT_barrel")
