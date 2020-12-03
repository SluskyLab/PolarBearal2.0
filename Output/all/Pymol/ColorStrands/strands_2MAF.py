from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2MAF.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2MAF_A_S0", "resi 8-15 & chain A & 2MAF ")
cmd.color ("red", "2MAF_A_S0")


cmd.select("2MAF_A_S1", "resi 55-61 & chain A & 2MAF ")
cmd.color ("yellow", "2MAF_A_S1")


cmd.select("2MAF_A_S2", "resi 66-71 & chain A & 2MAF ")
cmd.color ("green", "2MAF_A_S2")


cmd.select("2MAF_A_S3", "resi 114-123 & chain A & 2MAF ")
cmd.color ("cyan", "2MAF_A_S3")


cmd.select("2MAF_A_S4", "resi 132-143 & chain A & 2MAF ")
cmd.color ("blue", "2MAF_A_S4")


cmd.select("2MAF_A_S5", "resi 191-202 & chain A & 2MAF ")
cmd.color ("magenta", "2MAF_A_S5")


cmd.select("2MAF_A_S6", "resi 205-216 & chain A & 2MAF ")
cmd.color ("red", "2MAF_A_S6")


cmd.select("2MAF_A_S7", "resi 231-237 & chain A & 2MAF ")
cmd.color ("yellow", "2MAF_A_S7")


cmd.select("2MAF_barrel", "2MAF_A_S*")
cmd.show("cartoon", "2MAF_barrel")
cmd.zoom("2MAF_barrel")
