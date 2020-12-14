from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ES7.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4ES7_A_S0", "resi 16-26 & chain A & 4ES7 ")
cmd.color ("red", "4ES7_A_S0")


cmd.select("4ES7_A_S1", "resi 40-45 & chain A & 4ES7 ")
cmd.color ("yellow", "4ES7_A_S1")


cmd.select("4ES7_A_S2", "resi 53-59 & chain A & 4ES7 ")
cmd.color ("green", "4ES7_A_S2")


cmd.select("4ES7_A_S3", "resi 66-73 & chain A & 4ES7 ")
cmd.color ("cyan", "4ES7_A_S3")


cmd.select("4ES7_A_S4", "resi 81-85 & chain A & 4ES7 ")
cmd.color ("blue", "4ES7_A_S4")


cmd.select("4ES7_A_S5", "resi 89-100 & chain A & 4ES7 ")
cmd.color ("magenta", "4ES7_A_S5")


cmd.select("4ES7_A_S6", "resi 104-112 & chain A & 4ES7 ")
cmd.color ("red", "4ES7_A_S6")


cmd.select("4ES7_A_S7", "resi 119-154 & chain A & 4ES7 ")
cmd.color ("yellow", "4ES7_A_S7")


cmd.select("4ES7_barrel", "4ES7_A_S*")
cmd.show("cartoon", "4ES7_barrel")
cmd.zoom("4ES7_barrel")
