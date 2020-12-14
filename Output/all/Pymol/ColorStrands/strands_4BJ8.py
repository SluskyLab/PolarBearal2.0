from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4BJ8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4BJ8_A_S0", "resi 10-14 & chain A & 4BJ8 ")
cmd.color ("red", "4BJ8_A_S0")


cmd.select("4BJ8_A_S1", "resi 18-23 & chain A & 4BJ8 ")
cmd.color ("yellow", "4BJ8_A_S1")


cmd.select("4BJ8_A_S2", "resi 27-34 & chain A & 4BJ8 ")
cmd.color ("green", "4BJ8_A_S2")


cmd.select("4BJ8_A_S3", "resi 50-56 & chain A & 4BJ8 ")
cmd.color ("cyan", "4BJ8_A_S3")


cmd.select("4BJ8_A_S4", "resi 64-68 & chain A & 4BJ8 ")
cmd.color ("blue", "4BJ8_A_S4")


cmd.select("4BJ8_A_S5", "resi 75-83 & chain A & 4BJ8 ")
cmd.color ("magenta", "4BJ8_A_S5")


cmd.select("4BJ8_A_S6", "resi 91-99 & chain A & 4BJ8 ")
cmd.color ("red", "4BJ8_A_S6")


cmd.select("4BJ8_A_S7", "resi 113-120 & chain A & 4BJ8 ")
cmd.color ("yellow", "4BJ8_A_S7")


cmd.select("4BJ8_barrel", "4BJ8_A_S*")
cmd.show("cartoon", "4BJ8_barrel")
cmd.zoom("4BJ8_barrel")
