from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3W9T.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3W9T_A_S0", "resi 337-370 & chain A & 3W9T ")
cmd.color ("red", "3W9T_A_S0")


cmd.select("3W9T_A_S1", "resi 397-407 & chain A & 3W9T ")
cmd.color ("yellow", "3W9T_A_S1")


cmd.select("3W9T_B_S0", "resi 302-334 & chain B & 3W9T ")
cmd.color ("red", "3W9T_B_S0")


cmd.select("3W9T_B_S1", "resi 337-370 & chain B & 3W9T ")
cmd.color ("yellow", "3W9T_B_S1")


cmd.select("3W9T_B_S2", "resi 397-407 & chain B & 3W9T ")
cmd.color ("green", "3W9T_B_S2")


cmd.select("3W9T_C_S0", "resi 302-334 & chain C & 3W9T ")
cmd.color ("red", "3W9T_C_S0")


cmd.select("3W9T_C_S1", "resi 337-370 & chain C & 3W9T ")
cmd.color ("yellow", "3W9T_C_S1")


cmd.select("3W9T_C_S2", "resi 397-407 & chain C & 3W9T ")
cmd.color ("green", "3W9T_C_S2")


cmd.select("3W9T_D_S0", "resi 302-334 & chain D & 3W9T ")
cmd.color ("red", "3W9T_D_S0")


cmd.select("3W9T_D_S1", "resi 337-370 & chain D & 3W9T ")
cmd.color ("yellow", "3W9T_D_S1")


cmd.select("3W9T_D_S2", "resi 397-407 & chain D & 3W9T ")
cmd.color ("green", "3W9T_D_S2")


cmd.select("3W9T_E_S0", "resi 302-334 & chain E & 3W9T ")
cmd.color ("red", "3W9T_E_S0")


cmd.select("3W9T_E_S1", "resi 337-370 & chain E & 3W9T ")
cmd.color ("yellow", "3W9T_E_S1")


cmd.select("3W9T_E_S2", "resi 397-407 & chain E & 3W9T ")
cmd.color ("green", "3W9T_E_S2")


cmd.select("3W9T_F_S0", "resi 302-334 & chain F & 3W9T ")
cmd.color ("red", "3W9T_F_S0")


cmd.select("3W9T_F_S1", "resi 337-370 & chain F & 3W9T ")
cmd.color ("yellow", "3W9T_F_S1")


cmd.select("3W9T_F_S2", "resi 397-407 & chain F & 3W9T ")
cmd.color ("green", "3W9T_F_S2")


cmd.select("3W9T_G_S0", "resi 302-332 & chain G & 3W9T ")
cmd.color ("red", "3W9T_G_S0")


cmd.select("3W9T_G_S1", "resi 337-370 & chain G & 3W9T ")
cmd.color ("yellow", "3W9T_G_S1")


cmd.select("3W9T_G_S2", "resi 397-407 & chain G & 3W9T ")
cmd.color ("green", "3W9T_G_S2")


cmd.select("3W9T_barrel", "3W9T_A_S* or 3W9T_B_S* or 3W9T_C_S* or 3W9T_D_S* or 3W9T_E_S* or 3W9T_F_S* or 3W9T_G_S*")
cmd.show("cartoon", "3W9T_barrel")
cmd.zoom("3W9T_barrel")
