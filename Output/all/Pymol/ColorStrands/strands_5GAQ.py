from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GAQ.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5GAQ_A_S0", "resi 11-27 & chain A & 5GAQ ")
cmd.color ("red", "5GAQ_A_S0")


cmd.select("5GAQ_A_S1", "resi 34-66 & chain A & 5GAQ ")
cmd.color ("yellow", "5GAQ_A_S1")


cmd.select("5GAQ_A_S2", "resi 127-137 & chain A & 5GAQ ")
cmd.color ("green", "5GAQ_A_S2")


cmd.select("5GAQ_B_S0", "resi 11-27 & chain B & 5GAQ ")
cmd.color ("red", "5GAQ_B_S0")


cmd.select("5GAQ_B_S1", "resi 34-66 & chain B & 5GAQ ")
cmd.color ("yellow", "5GAQ_B_S1")


cmd.select("5GAQ_B_S2", "resi 127-137 & chain B & 5GAQ ")
cmd.color ("green", "5GAQ_B_S2")


cmd.select("5GAQ_C_S0", "resi 11-27 & chain C & 5GAQ ")
cmd.color ("red", "5GAQ_C_S0")


cmd.select("5GAQ_C_S1", "resi 34-66 & chain C & 5GAQ ")
cmd.color ("yellow", "5GAQ_C_S1")


cmd.select("5GAQ_C_S2", "resi 127-137 & chain C & 5GAQ ")
cmd.color ("green", "5GAQ_C_S2")


cmd.select("5GAQ_D_S0", "resi 11-27 & chain D & 5GAQ ")
cmd.color ("red", "5GAQ_D_S0")


cmd.select("5GAQ_D_S1", "resi 34-66 & chain D & 5GAQ ")
cmd.color ("yellow", "5GAQ_D_S1")


cmd.select("5GAQ_D_S2", "resi 127-137 & chain D & 5GAQ ")
cmd.color ("green", "5GAQ_D_S2")


cmd.select("5GAQ_E_S0", "resi 11-27 & chain E & 5GAQ ")
cmd.color ("red", "5GAQ_E_S0")


cmd.select("5GAQ_E_S1", "resi 34-66 & chain E & 5GAQ ")
cmd.color ("yellow", "5GAQ_E_S1")


cmd.select("5GAQ_E_S2", "resi 127-137 & chain E & 5GAQ ")
cmd.color ("green", "5GAQ_E_S2")


cmd.select("5GAQ_F_S0", "resi 11-27 & chain F & 5GAQ ")
cmd.color ("red", "5GAQ_F_S0")


cmd.select("5GAQ_F_S1", "resi 34-66 & chain F & 5GAQ ")
cmd.color ("yellow", "5GAQ_F_S1")


cmd.select("5GAQ_F_S2", "resi 127-137 & chain F & 5GAQ ")
cmd.color ("green", "5GAQ_F_S2")


cmd.select("5GAQ_G_S0", "resi 11-27 & chain G & 5GAQ ")
cmd.color ("red", "5GAQ_G_S0")


cmd.select("5GAQ_G_S1", "resi 34-66 & chain G & 5GAQ ")
cmd.color ("yellow", "5GAQ_G_S1")


cmd.select("5GAQ_G_S2", "resi 127-137 & chain G & 5GAQ ")
cmd.color ("green", "5GAQ_G_S2")


cmd.select("5GAQ_H_S0", "resi 11-27 & chain H & 5GAQ ")
cmd.color ("red", "5GAQ_H_S0")


cmd.select("5GAQ_H_S1", "resi 34-66 & chain H & 5GAQ ")
cmd.color ("yellow", "5GAQ_H_S1")


cmd.select("5GAQ_H_S2", "resi 127-137 & chain H & 5GAQ ")
cmd.color ("green", "5GAQ_H_S2")


cmd.select("5GAQ_I_S0", "resi 11-27 & chain I & 5GAQ ")
cmd.color ("red", "5GAQ_I_S0")


cmd.select("5GAQ_I_S1", "resi 34-66 & chain I & 5GAQ ")
cmd.color ("yellow", "5GAQ_I_S1")


cmd.select("5GAQ_I_S2", "resi 127-137 & chain I & 5GAQ ")
cmd.color ("green", "5GAQ_I_S2")


cmd.select("5GAQ_barrel", "5GAQ_A_S* or 5GAQ_B_S* or 5GAQ_C_S* or 5GAQ_D_S* or 5GAQ_E_S* or 5GAQ_F_S* or 5GAQ_G_S* or 5GAQ_H_S* or 5GAQ_I_S*")
cmd.show("cartoon", "5GAQ_barrel")
cmd.zoom("5GAQ_barrel")
