from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2XST.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2XST_A_S0", "resi 35-45 & chain A & 2XST ")
cmd.color ("red", "2XST_A_S0")


cmd.select("2XST_A_S1", "resi 59-64 & chain A & 2XST ")
cmd.color ("yellow", "2XST_A_S1")


cmd.select("2XST_A_S2", "resi 70-76 & chain A & 2XST ")
cmd.color ("green", "2XST_A_S2")


cmd.select("2XST_A_S3", "resi 86-93 & chain A & 2XST ")
cmd.color ("cyan", "2XST_A_S3")


cmd.select("2XST_A_S4", "resi 98-101 & chain A & 2XST ")
cmd.color ("blue", "2XST_A_S4")


cmd.select("2XST_A_S5", "resi 105-115 & chain A & 2XST ")
cmd.color ("magenta", "2XST_A_S5")


cmd.select("2XST_A_S6", "resi 119-127 & chain A & 2XST ")
cmd.color ("red", "2XST_A_S6")


cmd.select("2XST_A_S7", "resi 133-168 & chain A & 2XST ")
cmd.color ("yellow", "2XST_A_S7")


cmd.select("2XST_barrel", "2XST_A_S*")
cmd.show("cartoon", "2XST_barrel")
cmd.zoom("2XST_barrel")
