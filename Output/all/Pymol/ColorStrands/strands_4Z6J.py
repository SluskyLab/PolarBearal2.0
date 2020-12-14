from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Z6J.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4Z6J_A_S0", "resi 18-21 & chain A & 4Z6J ")
cmd.color ("red", "4Z6J_A_S0")


cmd.select("4Z6J_A_S1", "resi 27-33 & chain A & 4Z6J ")
cmd.color ("yellow", "4Z6J_A_S1")


cmd.select("4Z6J_A_S2", "resi 41-49 & chain A & 4Z6J ")
cmd.color ("green", "4Z6J_A_S2")


cmd.select("4Z6J_A_S3", "resi 62-69 & chain A & 4Z6J ")
cmd.color ("cyan", "4Z6J_A_S3")


cmd.select("4Z6J_A_S4", "resi 73-81 & chain A & 4Z6J ")
cmd.color ("blue", "4Z6J_A_S4")


cmd.select("4Z6J_A_S5", "resi 90-99 & chain A & 4Z6J ")
cmd.color ("magenta", "4Z6J_A_S5")


cmd.select("4Z6J_A_S6", "resi 106-115 & chain A & 4Z6J ")
cmd.color ("red", "4Z6J_A_S6")


cmd.select("4Z6J_A_S7", "resi 122-131 & chain A & 4Z6J ")
cmd.color ("yellow", "4Z6J_A_S7")


cmd.select("4Z6J_barrel", "4Z6J_A_S*")
cmd.show("cartoon", "4Z6J_barrel")
cmd.zoom("4Z6J_barrel")
