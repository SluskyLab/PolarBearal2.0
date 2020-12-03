from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DZM.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3DZM_A_S0", "resi 3-12 & chain A & 3DZM ")
cmd.color ("red", "3DZM_A_S0")


cmd.select("3DZM_A_S1", "resi 17-25 & chain A & 3DZM ")
cmd.color ("yellow", "3DZM_A_S1")


cmd.select("3DZM_A_S2", "resi 32-44 & chain A & 3DZM ")
cmd.color ("green", "3DZM_A_S2")


cmd.select("3DZM_A_S3", "resi 69-84 & chain A & 3DZM ")
cmd.color ("cyan", "3DZM_A_S3")


cmd.select("3DZM_A_S4", "resi 93-111 & chain A & 3DZM ")
cmd.color ("blue", "3DZM_A_S4")


cmd.select("3DZM_A_S5", "resi 119-138 & chain A & 3DZM ")
cmd.color ("magenta", "3DZM_A_S5")


cmd.select("3DZM_A_S6", "resi 145-165 & chain A & 3DZM ")
cmd.color ("red", "3DZM_A_S6")


cmd.select("3DZM_A_S7", "resi 196-205 & chain A & 3DZM ")
cmd.color ("yellow", "3DZM_A_S7")


cmd.select("3DZM_barrel", "3DZM_A_S*")
cmd.show("cartoon", "3DZM_barrel")
cmd.zoom("3DZM_barrel")
