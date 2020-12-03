from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1T.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4E1T_A_S0", "resi 151-158 & chain A & 4E1T ")
cmd.color ("red", "4E1T_A_S0")


cmd.select("4E1T_A_S1", "resi 165-176 & chain A & 4E1T ")
cmd.color ("yellow", "4E1T_A_S1")


cmd.select("4E1T_A_S2", "resi 180-191 & chain A & 4E1T ")
cmd.color ("green", "4E1T_A_S2")


cmd.select("4E1T_A_S3", "resi 196-207 & chain A & 4E1T ")
cmd.color ("cyan", "4E1T_A_S3")


cmd.select("4E1T_A_S4", "resi 212-223 & chain A & 4E1T ")
cmd.color ("blue", "4E1T_A_S4")


cmd.select("4E1T_A_S5", "resi 227-237 & chain A & 4E1T ")
cmd.color ("magenta", "4E1T_A_S5")


cmd.select("4E1T_A_S6", "resi 240-255 & chain A & 4E1T ")
cmd.color ("red", "4E1T_A_S6")


cmd.select("4E1T_A_S7", "resi 265-278 & chain A & 4E1T ")
cmd.color ("yellow", "4E1T_A_S7")


cmd.select("4E1T_A_S8", "resi 284-299 & chain A & 4E1T ")
cmd.color ("green", "4E1T_A_S8")


cmd.select("4E1T_A_S9", "resi 308-321 & chain A & 4E1T ")
cmd.color ("cyan", "4E1T_A_S9")


cmd.select("4E1T_A_S10", "resi 325-335 & chain A & 4E1T ")
cmd.color ("blue", "4E1T_A_S10")


cmd.select("4E1T_A_S11", "resi 339-350 & chain A & 4E1T ")
cmd.color ("magenta", "4E1T_A_S11")


cmd.select("4E1T_barrel", "4E1T_A_S*")
cmd.show("cartoon", "4E1T_barrel")
cmd.zoom("4E1T_barrel")
