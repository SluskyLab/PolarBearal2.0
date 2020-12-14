from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H56.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4H56_A_S0", "resi 114-132 & chain A & 4H56 ")
cmd.color ("red", "4H56_A_S0")


cmd.select("4H56_B_S0", "resi 114-132 & chain B & 4H56 ")
cmd.color ("red", "4H56_B_S0")


cmd.select("4H56_B_S1", "resi 135-155 & chain B & 4H56 ")
cmd.color ("yellow", "4H56_B_S1")


cmd.select("4H56_C_S0", "resi 114-132 & chain C & 4H56 ")
cmd.color ("red", "4H56_C_S0")


cmd.select("4H56_C_S1", "resi 135-155 & chain C & 4H56 ")
cmd.color ("yellow", "4H56_C_S1")


cmd.select("4H56_D_S0", "resi 114-132 & chain D & 4H56 ")
cmd.color ("red", "4H56_D_S0")


cmd.select("4H56_D_S1", "resi 135-155 & chain D & 4H56 ")
cmd.color ("yellow", "4H56_D_S1")


cmd.select("4H56_E_S0", "resi 114-132 & chain E & 4H56 ")
cmd.color ("red", "4H56_E_S0")


cmd.select("4H56_E_S1", "resi 135-155 & chain E & 4H56 ")
cmd.color ("yellow", "4H56_E_S1")


cmd.select("4H56_F_S0", "resi 114-132 & chain F & 4H56 ")
cmd.color ("red", "4H56_F_S0")


cmd.select("4H56_F_S1", "resi 135-155 & chain F & 4H56 ")
cmd.color ("yellow", "4H56_F_S1")


cmd.select("4H56_G_S0", "resi 135-155 & chain G & 4H56 ")
cmd.color ("red", "4H56_G_S0")


cmd.select("4H56_H_S0", "resi 114-132 & chain H & 4H56 ")
cmd.color ("red", "4H56_H_S0")


cmd.select("4H56_I_S0", "resi 114-132 & chain I & 4H56 ")
cmd.color ("red", "4H56_I_S0")


cmd.select("4H56_I_S1", "resi 135-155 & chain I & 4H56 ")
cmd.color ("yellow", "4H56_I_S1")


cmd.select("4H56_J_S0", "resi 114-132 & chain J & 4H56 ")
cmd.color ("red", "4H56_J_S0")


cmd.select("4H56_J_S1", "resi 135-155 & chain J & 4H56 ")
cmd.color ("yellow", "4H56_J_S1")


cmd.select("4H56_K_S0", "resi 114-132 & chain K & 4H56 ")
cmd.color ("red", "4H56_K_S0")


cmd.select("4H56_K_S1", "resi 135-155 & chain K & 4H56 ")
cmd.color ("yellow", "4H56_K_S1")


cmd.select("4H56_L_S0", "resi 114-132 & chain L & 4H56 ")
cmd.color ("red", "4H56_L_S0")


cmd.select("4H56_L_S1", "resi 135-155 & chain L & 4H56 ")
cmd.color ("yellow", "4H56_L_S1")


cmd.select("4H56_M_S0", "resi 114-132 & chain M & 4H56 ")
cmd.color ("red", "4H56_M_S0")


cmd.select("4H56_M_S1", "resi 135-155 & chain M & 4H56 ")
cmd.color ("yellow", "4H56_M_S1")


cmd.select("4H56_N_S0", "resi 135-155 & chain N & 4H56 ")
cmd.color ("red", "4H56_N_S0")


cmd.select("4H56_barrel", "4H56_A_S* or 4H56_B_S* or 4H56_C_S* or 4H56_D_S* or 4H56_E_S* or 4H56_F_S* or 4H56_G_S* or 4H56_H_S* or 4H56_I_S* or 4H56_J_S* or 4H56_K_S* or 4H56_L_S* or 4H56_M_S* or 4H56_N_S*")
cmd.show("cartoon", "4H56_barrel")
cmd.zoom("4H56_barrel")
