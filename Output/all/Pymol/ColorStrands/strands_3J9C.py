from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3J9C.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3J9C_B_S0", "resi 276-312 & chain B & 3J9C ")
cmd.color ("red", "3J9C_B_S0")


cmd.select("3J9C_B_S1", "resi 315-353 & chain B & 3J9C ")
cmd.color ("yellow", "3J9C_B_S1")


cmd.select("3J9C_C_S0", "resi 276-312 & chain C & 3J9C ")
cmd.color ("red", "3J9C_C_S0")


cmd.select("3J9C_C_S1", "resi 315-353 & chain C & 3J9C ")
cmd.color ("yellow", "3J9C_C_S1")


cmd.select("3J9C_D_S0", "resi 276-312 & chain D & 3J9C ")
cmd.color ("red", "3J9C_D_S0")


cmd.select("3J9C_D_S1", "resi 315-353 & chain D & 3J9C ")
cmd.color ("yellow", "3J9C_D_S1")


cmd.select("3J9C_E_S0", "resi 276-312 & chain E & 3J9C ")
cmd.color ("red", "3J9C_E_S0")


cmd.select("3J9C_E_S1", "resi 315-353 & chain E & 3J9C ")
cmd.color ("yellow", "3J9C_E_S1")


cmd.select("3J9C_F_S0", "resi 276-312 & chain F & 3J9C ")
cmd.color ("red", "3J9C_F_S0")


cmd.select("3J9C_F_S1", "resi 315-353 & chain F & 3J9C ")
cmd.color ("yellow", "3J9C_F_S1")


cmd.select("3J9C_G_S0", "resi 276-312 & chain G & 3J9C ")
cmd.color ("red", "3J9C_G_S0")


cmd.select("3J9C_G_S1", "resi 315-353 & chain G & 3J9C ")
cmd.color ("yellow", "3J9C_G_S1")


cmd.select("3J9C_H_S0", "resi 276-312 & chain H & 3J9C ")
cmd.color ("red", "3J9C_H_S0")


cmd.select("3J9C_H_S1", "resi 315-353 & chain H & 3J9C ")
cmd.color ("yellow", "3J9C_H_S1")


cmd.select("3J9C_barrel", "3J9C_B_S* or 3J9C_C_S* or 3J9C_D_S* or 3J9C_E_S* or 3J9C_F_S* or 3J9C_G_S* or 3J9C_H_S*")
cmd.show("cartoon", "3J9C_barrel")
cmd.zoom("3J9C_barrel")
