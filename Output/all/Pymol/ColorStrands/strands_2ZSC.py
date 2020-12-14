from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZSC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2ZSC_A_S0", "resi 10-14 & chain A & 2ZSC ")
cmd.color ("red", "2ZSC_A_S0")


cmd.select("2ZSC_A_S1", "resi 18-23 & chain A & 2ZSC ")
cmd.color ("yellow", "2ZSC_A_S1")


cmd.select("2ZSC_A_S2", "resi 28-35 & chain A & 2ZSC ")
cmd.color ("green", "2ZSC_A_S2")


cmd.select("2ZSC_A_S3", "resi 45-51 & chain A & 2ZSC ")
cmd.color ("cyan", "2ZSC_A_S3")


cmd.select("2ZSC_A_S4", "resi 61-69 & chain A & 2ZSC ")
cmd.color ("blue", "2ZSC_A_S4")


cmd.select("2ZSC_A_S5", "resi 75-85 & chain A & 2ZSC ")
cmd.color ("magenta", "2ZSC_A_S5")


cmd.select("2ZSC_A_S6", "resi 91-101 & chain A & 2ZSC ")
cmd.color ("red", "2ZSC_A_S6")


cmd.select("2ZSC_A_S7", "resi 110-119 & chain A & 2ZSC ")
cmd.color ("yellow", "2ZSC_A_S7")


cmd.select("2ZSC_barrel", "2ZSC_A_S*")
cmd.show("cartoon", "2ZSC_barrel")
cmd.zoom("2ZSC_barrel")
