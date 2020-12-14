from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3IA8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3IA8_A_S0", "resi 18-29 & chain A & 3IA8 ")
cmd.color ("red", "3IA8_A_S0")


cmd.select("3IA8_A_S1", "resi 36-45 & chain A & 3IA8 ")
cmd.color ("yellow", "3IA8_A_S1")


cmd.select("3IA8_A_S2", "resi 52-59 & chain A & 3IA8 ")
cmd.color ("green", "3IA8_A_S2")


cmd.select("3IA8_A_S3", "resi 67-75 & chain A & 3IA8 ")
cmd.color ("cyan", "3IA8_A_S3")


cmd.select("3IA8_A_S4", "resi 81-90 & chain A & 3IA8 ")
cmd.color ("blue", "3IA8_A_S4")


cmd.select("3IA8_A_S5", "resi 93-101 & chain A & 3IA8 ")
cmd.color ("magenta", "3IA8_A_S5")


cmd.select("3IA8_A_S6", "resi 106-114 & chain A & 3IA8 ")
cmd.color ("red", "3IA8_A_S6")


cmd.select("3IA8_A_S7", "resi 125-132 & chain A & 3IA8 ")
cmd.color ("yellow", "3IA8_A_S7")


cmd.select("3IA8_A_S8", "resi 139-146 & chain A & 3IA8 ")
cmd.color ("green", "3IA8_A_S8")


cmd.select("3IA8_A_S9", "resi 155-164 & chain A & 3IA8 ")
cmd.color ("cyan", "3IA8_A_S9")


cmd.select("3IA8_barrel", "3IA8_A_S*")
cmd.show("cartoon", "3IA8_barrel")
cmd.zoom("3IA8_barrel")
