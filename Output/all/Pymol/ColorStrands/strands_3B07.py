from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3B07.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3B07_A_S0", "resi 95-126 & chain A & 3B07 ")
cmd.color ("red", "3B07_A_S0")


cmd.select("3B07_A_S1", "resi 128-148 & chain A & 3B07 ")
cmd.color ("yellow", "3B07_A_S1")


cmd.select("3B07_B_S0", "resi 93-118 & chain B & 3B07 ")
cmd.color ("red", "3B07_B_S0")


cmd.select("3B07_B_S1", "resi 122-140 & chain B & 3B07 ")
cmd.color ("yellow", "3B07_B_S1")


cmd.select("3B07_C_S0", "resi 108-126 & chain C & 3B07 ")
cmd.color ("red", "3B07_C_S0")


cmd.select("3B07_C_S1", "resi 128-148 & chain C & 3B07 ")
cmd.color ("yellow", "3B07_C_S1")


cmd.select("3B07_D_S0", "resi 93-118 & chain D & 3B07 ")
cmd.color ("red", "3B07_D_S0")


cmd.select("3B07_D_S1", "resi 122-140 & chain D & 3B07 ")
cmd.color ("yellow", "3B07_D_S1")


cmd.select("3B07_E_S0", "resi 108-126 & chain E & 3B07 ")
cmd.color ("red", "3B07_E_S0")


cmd.select("3B07_E_S1", "resi 128-148 & chain E & 3B07 ")
cmd.color ("yellow", "3B07_E_S1")


cmd.select("3B07_F_S0", "resi 93-118 & chain F & 3B07 ")
cmd.color ("red", "3B07_F_S0")


cmd.select("3B07_F_S1", "resi 122-140 & chain F & 3B07 ")
cmd.color ("yellow", "3B07_F_S1")


cmd.select("3B07_G_S0", "resi 108-126 & chain G & 3B07 ")
cmd.color ("red", "3B07_G_S0")


cmd.select("3B07_G_S1", "resi 128-148 & chain G & 3B07 ")
cmd.color ("yellow", "3B07_G_S1")


cmd.select("3B07_H_S0", "resi 93-118 & chain H & 3B07 ")
cmd.color ("red", "3B07_H_S0")


cmd.select("3B07_H_S1", "resi 122-140 & chain H & 3B07 ")
cmd.color ("yellow", "3B07_H_S1")


cmd.select("3B07_barrel", "3B07_A_S* or 3B07_B_S* or 3B07_C_S* or 3B07_D_S* or 3B07_E_S* or 3B07_F_S* or 3B07_G_S* or 3B07_H_S*")
cmd.show("cartoon", "3B07_barrel")
cmd.zoom("3B07_barrel")
