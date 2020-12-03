from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F1V.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2F1V_A_S0", "resi 6-16 & chain A & 2F1V ")
cmd.color ("red", "2F1V_A_S0")


cmd.select("2F1V_A_S1", "resi 32-45 & chain A & 2F1V ")
cmd.color ("yellow", "2F1V_A_S1")


cmd.select("2F1V_A_S2", "resi 52-67 & chain A & 2F1V ")
cmd.color ("green", "2F1V_A_S2")


cmd.select("2F1V_A_S3", "resi 73-87 & chain A & 2F1V ")
cmd.color ("cyan", "2F1V_A_S3")


cmd.select("2F1V_A_S4", "resi 97-113 & chain A & 2F1V ")
cmd.color ("blue", "2F1V_A_S4")


cmd.select("2F1V_A_S5", "resi 124-144 & chain A & 2F1V ")
cmd.color ("magenta", "2F1V_A_S5")


cmd.select("2F1V_A_S6", "resi 147-166 & chain A & 2F1V ")
cmd.color ("red", "2F1V_A_S6")


cmd.select("2F1V_A_S7", "resi 174-191 & chain A & 2F1V ")
cmd.color ("yellow", "2F1V_A_S7")


cmd.select("2F1V_barrel", "2F1V_A_S*")
cmd.show("cartoon", "2F1V_barrel")
cmd.zoom("2F1V_barrel")
