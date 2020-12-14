from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3O44.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3O44_A_S0", "resi 277-299 & chain A & 3O44 ")
cmd.color ("red", "3O44_A_S0")


cmd.select("3O44_B_S0", "resi 277-299 & chain B & 3O44 ")
cmd.color ("red", "3O44_B_S0")


cmd.select("3O44_B_S1", "resi 303-324 & chain B & 3O44 ")
cmd.color ("yellow", "3O44_B_S1")


cmd.select("3O44_C_S0", "resi 277-299 & chain C & 3O44 ")
cmd.color ("red", "3O44_C_S0")


cmd.select("3O44_C_S1", "resi 303-324 & chain C & 3O44 ")
cmd.color ("yellow", "3O44_C_S1")


cmd.select("3O44_D_S0", "resi 277-299 & chain D & 3O44 ")
cmd.color ("red", "3O44_D_S0")


cmd.select("3O44_D_S1", "resi 303-324 & chain D & 3O44 ")
cmd.color ("yellow", "3O44_D_S1")


cmd.select("3O44_E_S0", "resi 277-299 & chain E & 3O44 ")
cmd.color ("red", "3O44_E_S0")


cmd.select("3O44_E_S1", "resi 303-324 & chain E & 3O44 ")
cmd.color ("yellow", "3O44_E_S1")


cmd.select("3O44_F_S0", "resi 277-299 & chain F & 3O44 ")
cmd.color ("red", "3O44_F_S0")


cmd.select("3O44_F_S1", "resi 303-324 & chain F & 3O44 ")
cmd.color ("yellow", "3O44_F_S1")


cmd.select("3O44_G_S0", "resi 303-324 & chain G & 3O44 ")
cmd.color ("red", "3O44_G_S0")


cmd.select("3O44_H_S0", "resi 277-299 & chain H & 3O44 ")
cmd.color ("red", "3O44_H_S0")


cmd.select("3O44_I_S0", "resi 277-299 & chain I & 3O44 ")
cmd.color ("red", "3O44_I_S0")


cmd.select("3O44_I_S1", "resi 303-324 & chain I & 3O44 ")
cmd.color ("yellow", "3O44_I_S1")


cmd.select("3O44_J_S0", "resi 277-299 & chain J & 3O44 ")
cmd.color ("red", "3O44_J_S0")


cmd.select("3O44_J_S1", "resi 303-324 & chain J & 3O44 ")
cmd.color ("yellow", "3O44_J_S1")


cmd.select("3O44_K_S0", "resi 277-299 & chain K & 3O44 ")
cmd.color ("red", "3O44_K_S0")


cmd.select("3O44_K_S1", "resi 303-324 & chain K & 3O44 ")
cmd.color ("yellow", "3O44_K_S1")


cmd.select("3O44_L_S0", "resi 277-299 & chain L & 3O44 ")
cmd.color ("red", "3O44_L_S0")


cmd.select("3O44_L_S1", "resi 303-324 & chain L & 3O44 ")
cmd.color ("yellow", "3O44_L_S1")


cmd.select("3O44_M_S0", "resi 277-299 & chain M & 3O44 ")
cmd.color ("red", "3O44_M_S0")


cmd.select("3O44_M_S1", "resi 303-324 & chain M & 3O44 ")
cmd.color ("yellow", "3O44_M_S1")


cmd.select("3O44_N_S0", "resi 303-324 & chain N & 3O44 ")
cmd.color ("red", "3O44_N_S0")


cmd.select("3O44_barrel", "3O44_A_S* or 3O44_B_S* or 3O44_C_S* or 3O44_D_S* or 3O44_E_S* or 3O44_F_S* or 3O44_G_S* or 3O44_H_S* or 3O44_I_S* or 3O44_J_S* or 3O44_K_S* or 3O44_L_S* or 3O44_M_S* or 3O44_N_S*")
cmd.show("cartoon", "3O44_barrel")
cmd.zoom("3O44_barrel")
