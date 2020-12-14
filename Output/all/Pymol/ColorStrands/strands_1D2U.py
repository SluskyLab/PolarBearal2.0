from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1D2U.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1D2U_A_S0", "resi 20-25 & chain A & 1D2U ")
cmd.color ("red", "1D2U_A_S0")


cmd.select("1D2U_A_S1", "resi 41-47 & chain A & 1D2U ")
cmd.color ("yellow", "1D2U_A_S1")


cmd.select("1D2U_A_S2", "resi 54-60 & chain A & 1D2U ")
cmd.color ("green", "1D2U_A_S2")


cmd.select("1D2U_A_S3", "resi 68-77 & chain A & 1D2U ")
cmd.color ("cyan", "1D2U_A_S3")


cmd.select("1D2U_A_S4", "resi 81-89 & chain A & 1D2U ")
cmd.color ("blue", "1D2U_A_S4")


cmd.select("1D2U_A_S5", "resi 104-111 & chain A & 1D2U ")
cmd.color ("magenta", "1D2U_A_S5")


cmd.select("1D2U_A_S6", "resi 117-124 & chain A & 1D2U ")
cmd.color ("red", "1D2U_A_S6")


cmd.select("1D2U_A_S7", "resi 133-137 & chain A & 1D2U ")
cmd.color ("yellow", "1D2U_A_S7")


cmd.select("1D2U_barrel", "1D2U_A_S*")
cmd.show("cartoon", "1D2U_barrel")
cmd.zoom("1D2U_barrel")
