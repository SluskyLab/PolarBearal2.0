from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1P4T.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1P4T_A_S0", "resi 4-17 & chain A & 1P4T ")
cmd.color ("red", "1P4T_A_S0")


cmd.select("1P4T_A_S1", "resi 24-36 & chain A & 1P4T ")
cmd.color ("yellow", "1P4T_A_S1")


cmd.select("1P4T_A_S2", "resi 41-52 & chain A & 1P4T ")
cmd.color ("green", "1P4T_A_S2")


cmd.select("1P4T_A_S3", "resi 60-70 & chain A & 1P4T ")
cmd.color ("cyan", "1P4T_A_S3")


cmd.select("1P4T_A_S4", "resi 79-93 & chain A & 1P4T ")
cmd.color ("blue", "1P4T_A_S4")


cmd.select("1P4T_A_S5", "resi 100-118 & chain A & 1P4T ")
cmd.color ("magenta", "1P4T_A_S5")


cmd.select("1P4T_A_S6", "resi 122-132 & chain A & 1P4T ")
cmd.color ("red", "1P4T_A_S6")


cmd.select("1P4T_A_S7", "resi 144-153 & chain A & 1P4T ")
cmd.color ("yellow", "1P4T_A_S7")


cmd.select("1P4T_barrel", "1P4T_A_S*")
cmd.show("cartoon", "1P4T_barrel")
cmd.zoom("1P4T_barrel")
