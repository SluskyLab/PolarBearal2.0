from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4TW1.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4TW1_A_S0", "resi 135-151 & chain A & 4TW1 ")
cmd.color ("red", "4TW1_A_S0")


cmd.select("4TW1_B_S0", "resi 136-147 & chain B & 4TW1 ")
cmd.color ("red", "4TW1_B_S0")


cmd.select("4TW1_B_S1", "resi 159-174 & chain B & 4TW1 ")
cmd.color ("yellow", "4TW1_B_S1")


cmd.select("4TW1_C_S0", "resi 107-124 & chain C & 4TW1 ")
cmd.color ("red", "4TW1_C_S0")


cmd.select("4TW1_C_S1", "resi 135-150 & chain C & 4TW1 ")
cmd.color ("yellow", "4TW1_C_S1")


cmd.select("4TW1_D_S0", "resi 136-152 & chain D & 4TW1 ")
cmd.color ("red", "4TW1_D_S0")


cmd.select("4TW1_D_S1", "resi 158-174 & chain D & 4TW1 ")
cmd.color ("yellow", "4TW1_D_S1")


cmd.select("4TW1_E_S0", "resi 111-128 & chain E & 4TW1 ")
cmd.color ("red", "4TW1_E_S0")


cmd.select("4TW1_E_S1", "resi 132-150 & chain E & 4TW1 ")
cmd.color ("yellow", "4TW1_E_S1")


cmd.select("4TW1_F_S0", "resi 136-151 & chain F & 4TW1 ")
cmd.color ("red", "4TW1_F_S0")


cmd.select("4TW1_F_S1", "resi 158-174 & chain F & 4TW1 ")
cmd.color ("yellow", "4TW1_F_S1")


cmd.select("4TW1_G_S0", "resi 107-129 & chain G & 4TW1 ")
cmd.color ("red", "4TW1_G_S0")


cmd.select("4TW1_G_S1", "resi 133-151 & chain G & 4TW1 ")
cmd.color ("yellow", "4TW1_G_S1")


cmd.select("4TW1_H_S0", "resi 136-152 & chain H & 4TW1 ")
cmd.color ("red", "4TW1_H_S0")


cmd.select("4TW1_I_S0", "resi 133-151 & chain I & 4TW1 ")
cmd.color ("red", "4TW1_I_S0")


cmd.select("4TW1_J_S0", "resi 131-147 & chain J & 4TW1 ")
cmd.color ("red", "4TW1_J_S0")


cmd.select("4TW1_J_S1", "resi 152-169 & chain J & 4TW1 ")
cmd.color ("yellow", "4TW1_J_S1")


cmd.select("4TW1_K_S0", "resi 107-125 & chain K & 4TW1 ")
cmd.color ("red", "4TW1_K_S0")


cmd.select("4TW1_K_S1", "resi 132-151 & chain K & 4TW1 ")
cmd.color ("yellow", "4TW1_K_S1")


cmd.select("4TW1_L_S0", "resi 136-152 & chain L & 4TW1 ")
cmd.color ("red", "4TW1_L_S0")


cmd.select("4TW1_L_S1", "resi 157-174 & chain L & 4TW1 ")
cmd.color ("yellow", "4TW1_L_S1")


cmd.select("4TW1_M_S0", "resi 107-128 & chain M & 4TW1 ")
cmd.color ("red", "4TW1_M_S0")


cmd.select("4TW1_M_S1", "resi 133-151 & chain M & 4TW1 ")
cmd.color ("yellow", "4TW1_M_S1")


cmd.select("4TW1_N_S0", "resi 136-152 & chain N & 4TW1 ")
cmd.color ("red", "4TW1_N_S0")


cmd.select("4TW1_N_S1", "resi 157-174 & chain N & 4TW1 ")
cmd.color ("yellow", "4TW1_N_S1")


cmd.select("4TW1_O_S0", "resi 109-150 & chain O & 4TW1 ")
cmd.color ("red", "4TW1_O_S0")


cmd.select("4TW1_P_S0", "resi 136-150 & chain P & 4TW1 ")
cmd.color ("red", "4TW1_P_S0")


cmd.select("4TW1_barrel", "4TW1_A_S* or 4TW1_B_S* or 4TW1_C_S* or 4TW1_D_S* or 4TW1_E_S* or 4TW1_F_S* or 4TW1_G_S* or 4TW1_H_S* or 4TW1_I_S* or 4TW1_J_S* or 4TW1_K_S* or 4TW1_L_S* or 4TW1_M_S* or 4TW1_N_S* or 4TW1_O_S* or 4TW1_P_S*")
cmd.show("cartoon", "4TW1_barrel")
cmd.zoom("4TW1_barrel")
