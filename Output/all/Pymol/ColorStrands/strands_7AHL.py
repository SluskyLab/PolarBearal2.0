from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/7AHL.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("7AHL_A_S0", "resi 106-127 & chain A & 7AHL ")
cmd.color ("red", "7AHL_A_S0")


cmd.select("7AHL_A_S1", "resi 132-150 & chain A & 7AHL ")
cmd.color ("yellow", "7AHL_A_S1")


cmd.select("7AHL_B_S0", "resi 101-127 & chain B & 7AHL ")
cmd.color ("red", "7AHL_B_S0")


cmd.select("7AHL_B_S1", "resi 132-150 & chain B & 7AHL ")
cmd.color ("yellow", "7AHL_B_S1")


cmd.select("7AHL_C_S0", "resi 104-127 & chain C & 7AHL ")
cmd.color ("red", "7AHL_C_S0")


cmd.select("7AHL_C_S1", "resi 132-150 & chain C & 7AHL ")
cmd.color ("yellow", "7AHL_C_S1")


cmd.select("7AHL_D_S0", "resi 106-127 & chain D & 7AHL ")
cmd.color ("red", "7AHL_D_S0")


cmd.select("7AHL_D_S1", "resi 132-150 & chain D & 7AHL ")
cmd.color ("yellow", "7AHL_D_S1")


cmd.select("7AHL_E_S0", "resi 109-127 & chain E & 7AHL ")
cmd.color ("red", "7AHL_E_S0")


cmd.select("7AHL_E_S1", "resi 132-150 & chain E & 7AHL ")
cmd.color ("yellow", "7AHL_E_S1")


cmd.select("7AHL_F_S0", "resi 101-127 & chain F & 7AHL ")
cmd.color ("red", "7AHL_F_S0")


cmd.select("7AHL_F_S1", "resi 132-150 & chain F & 7AHL ")
cmd.color ("yellow", "7AHL_F_S1")


cmd.select("7AHL_G_S0", "resi 101-127 & chain G & 7AHL ")
cmd.color ("red", "7AHL_G_S0")


cmd.select("7AHL_G_S1", "resi 132-150 & chain G & 7AHL ")
cmd.color ("yellow", "7AHL_G_S1")


cmd.select("7AHL_barrel", "7AHL_A_S* or 7AHL_B_S* or 7AHL_C_S* or 7AHL_D_S* or 7AHL_E_S* or 7AHL_F_S* or 7AHL_G_S*")
cmd.show("cartoon", "7AHL_barrel")
cmd.zoom("7AHL_barrel")
