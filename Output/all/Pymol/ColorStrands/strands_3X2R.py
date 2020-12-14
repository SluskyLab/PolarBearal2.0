from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3X2R.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3X2R_A_S0", "resi 150-158 & chain A & 3X2R ")
cmd.color ("red", "3X2R_A_S0")


cmd.select("3X2R_A_S1", "resi 161-169 & chain A & 3X2R ")
cmd.color ("yellow", "3X2R_A_S1")


cmd.select("3X2R_A_S2", "resi 197-208 & chain A & 3X2R ")
cmd.color ("green", "3X2R_A_S2")


cmd.select("3X2R_A_S3", "resi 214-224 & chain A & 3X2R ")
cmd.color ("cyan", "3X2R_A_S3")


cmd.select("3X2R_B_S0", "resi 150-158 & chain B & 3X2R ")
cmd.color ("red", "3X2R_B_S0")


cmd.select("3X2R_B_S1", "resi 161-169 & chain B & 3X2R ")
cmd.color ("yellow", "3X2R_B_S1")


cmd.select("3X2R_B_S2", "resi 197-208 & chain B & 3X2R ")
cmd.color ("green", "3X2R_B_S2")


cmd.select("3X2R_B_S3", "resi 214-224 & chain B & 3X2R ")
cmd.color ("cyan", "3X2R_B_S3")


cmd.select("3X2R_C_S0", "resi 136-147 & chain C & 3X2R ")
cmd.color ("red", "3X2R_C_S0")


cmd.select("3X2R_C_S1", "resi 150-158 & chain C & 3X2R ")
cmd.color ("yellow", "3X2R_C_S1")


cmd.select("3X2R_C_S2", "resi 170-179 & chain C & 3X2R ")
cmd.color ("green", "3X2R_C_S2")


cmd.select("3X2R_C_S3", "resi 188-208 & chain C & 3X2R ")
cmd.color ("cyan", "3X2R_C_S3")


cmd.select("3X2R_C_S4", "resi 214-224 & chain C & 3X2R ")
cmd.color ("blue", "3X2R_C_S4")


cmd.select("3X2R_D_S0", "resi 150-158 & chain D & 3X2R ")
cmd.color ("red", "3X2R_D_S0")


cmd.select("3X2R_D_S1", "resi 161-169 & chain D & 3X2R ")
cmd.color ("yellow", "3X2R_D_S1")


cmd.select("3X2R_D_S2", "resi 197-208 & chain D & 3X2R ")
cmd.color ("green", "3X2R_D_S2")


cmd.select("3X2R_D_S3", "resi 214-224 & chain D & 3X2R ")
cmd.color ("cyan", "3X2R_D_S3")


cmd.select("3X2R_E_S0", "resi 150-158 & chain E & 3X2R ")
cmd.color ("red", "3X2R_E_S0")


cmd.select("3X2R_E_S1", "resi 161-169 & chain E & 3X2R ")
cmd.color ("yellow", "3X2R_E_S1")


cmd.select("3X2R_E_S2", "resi 197-208 & chain E & 3X2R ")
cmd.color ("green", "3X2R_E_S2")


cmd.select("3X2R_E_S3", "resi 214-224 & chain E & 3X2R ")
cmd.color ("cyan", "3X2R_E_S3")


cmd.select("3X2R_F_S0", "resi 150-158 & chain F & 3X2R ")
cmd.color ("red", "3X2R_F_S0")


cmd.select("3X2R_F_S1", "resi 161-169 & chain F & 3X2R ")
cmd.color ("yellow", "3X2R_F_S1")


cmd.select("3X2R_F_S2", "resi 197-208 & chain F & 3X2R ")
cmd.color ("green", "3X2R_F_S2")


cmd.select("3X2R_F_S3", "resi 214-224 & chain F & 3X2R ")
cmd.color ("cyan", "3X2R_F_S3")


cmd.select("3X2R_G_S0", "resi 150-158 & chain G & 3X2R ")
cmd.color ("red", "3X2R_G_S0")


cmd.select("3X2R_G_S1", "resi 161-169 & chain G & 3X2R ")
cmd.color ("yellow", "3X2R_G_S1")


cmd.select("3X2R_G_S2", "resi 197-208 & chain G & 3X2R ")
cmd.color ("green", "3X2R_G_S2")


cmd.select("3X2R_G_S3", "resi 214-224 & chain G & 3X2R ")
cmd.color ("cyan", "3X2R_G_S3")


cmd.select("3X2R_H_S0", "resi 150-158 & chain H & 3X2R ")
cmd.color ("red", "3X2R_H_S0")


cmd.select("3X2R_H_S1", "resi 161-169 & chain H & 3X2R ")
cmd.color ("yellow", "3X2R_H_S1")


cmd.select("3X2R_H_S2", "resi 197-208 & chain H & 3X2R ")
cmd.color ("green", "3X2R_H_S2")


cmd.select("3X2R_H_S3", "resi 214-224 & chain H & 3X2R ")
cmd.color ("cyan", "3X2R_H_S3")


cmd.select("3X2R_I_S0", "resi 150-158 & chain I & 3X2R ")
cmd.color ("red", "3X2R_I_S0")


cmd.select("3X2R_I_S1", "resi 161-169 & chain I & 3X2R ")
cmd.color ("yellow", "3X2R_I_S1")


cmd.select("3X2R_I_S2", "resi 197-208 & chain I & 3X2R ")
cmd.color ("green", "3X2R_I_S2")


cmd.select("3X2R_I_S3", "resi 214-224 & chain I & 3X2R ")
cmd.color ("cyan", "3X2R_I_S3")


cmd.select("3X2R_barrel", "3X2R_A_S* or 3X2R_B_S* or 3X2R_C_S* or 3X2R_D_S* or 3X2R_E_S* or 3X2R_F_S* or 3X2R_G_S* or 3X2R_H_S* or 3X2R_I_S*")
cmd.show("cartoon", "3X2R_barrel")
cmd.zoom("3X2R_barrel")
