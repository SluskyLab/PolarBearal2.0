from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1R0U.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1R0U_A_S0", "resi 2-16 & chain A & 1R0U ")
cmd.color ("red", "1R0U_A_S0")


cmd.select("1R0U_A_S1", "resi 22-34 & chain A & 1R0U ")
cmd.color ("yellow", "1R0U_A_S1")


cmd.select("1R0U_A_S2", "resi 39-45 & chain A & 1R0U ")
cmd.color ("green", "1R0U_A_S2")


cmd.select("1R0U_A_S3", "resi 52-58 & chain A & 1R0U ")
cmd.color ("cyan", "1R0U_A_S3")


cmd.select("1R0U_A_S4", "resi 63-68 & chain A & 1R0U ")
cmd.color ("blue", "1R0U_A_S4")


cmd.select("1R0U_A_S5", "resi 72-77 & chain A & 1R0U ")
cmd.color ("magenta", "1R0U_A_S5")


cmd.select("1R0U_A_S6", "resi 81-88 & chain A & 1R0U ")
cmd.color ("red", "1R0U_A_S6")


cmd.select("1R0U_A_S7", "resi 94-106 & chain A & 1R0U ")
cmd.color ("yellow", "1R0U_A_S7")


cmd.select("1R0U_A_S8", "resi 112-121 & chain A & 1R0U ")
cmd.color ("green", "1R0U_A_S8")


cmd.select("1R0U_A_S9", "resi 128-137 & chain A & 1R0U ")
cmd.color ("cyan", "1R0U_A_S9")


cmd.select("1R0U_barrel", "1R0U_A_S*")
cmd.show("cartoon", "1R0U_barrel")
cmd.zoom("1R0U_barrel")
