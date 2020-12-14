from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3D5K_A_S0", "resi 85-99 & chain A & 3D5K ")
cmd.color ("red", "3D5K_A_S0")


cmd.select("3D5K_A_S1", "resi 323-332 & chain A & 3D5K ")
cmd.color ("yellow", "3D5K_A_S1")


cmd.select("3D5K_B_S0", "resi 85-99 & chain B & 3D5K ")
cmd.color ("red", "3D5K_B_S0")


cmd.select("3D5K_B_S1", "resi 323-332 & chain B & 3D5K ")
cmd.color ("yellow", "3D5K_B_S1")


cmd.select("3D5K_C_S0", "resi 88-99 & chain C & 3D5K ")
cmd.color ("red", "3D5K_C_S0")


cmd.select("3D5K_C_S1", "resi 323-332 & chain C & 3D5K ")
cmd.color ("yellow", "3D5K_C_S1")


cmd.select("3D5K_barrel", "3D5K_A_S* or 3D5K_B_S* or 3D5K_C_S*")
cmd.show("cartoon", "3D5K_barrel")
cmd.zoom("3D5K_barrel")
