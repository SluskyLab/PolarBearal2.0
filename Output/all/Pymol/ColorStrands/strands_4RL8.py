from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RL8_A_S0", "resi 16-30 & chain A & 4RL8 ")
cmd.color ("red", "4RL8_A_S0")


cmd.select("4RL8_A_S1", "resi 37-58 & chain A & 4RL8 ")
cmd.color ("yellow", "4RL8_A_S1")


cmd.select("4RL8_A_S2", "resi 62-78 & chain A & 4RL8 ")
cmd.color ("green", "4RL8_A_S2")


cmd.select("4RL8_A_S3", "resi 87-101 & chain A & 4RL8 ")
cmd.color ("cyan", "4RL8_A_S3")


cmd.select("4RL8_A_S4", "resi 109-122 & chain A & 4RL8 ")
cmd.color ("blue", "4RL8_A_S4")


cmd.select("4RL8_A_S5", "resi 137-148 & chain A & 4RL8 ")
cmd.color ("magenta", "4RL8_A_S5")


cmd.select("4RL8_A_S6", "resi 152-166 & chain A & 4RL8 ")
cmd.color ("red", "4RL8_A_S6")


cmd.select("4RL8_A_S7", "resi 176-192 & chain A & 4RL8 ")
cmd.color ("yellow", "4RL8_A_S7")


cmd.select("4RL8_A_S8", "resi 196-211 & chain A & 4RL8 ")
cmd.color ("green", "4RL8_A_S8")


cmd.select("4RL8_A_S9", "resi 222-234 & chain A & 4RL8 ")
cmd.color ("cyan", "4RL8_A_S9")


cmd.select("4RL8_A_S10", "resi 238-251 & chain A & 4RL8 ")
cmd.color ("blue", "4RL8_A_S10")


cmd.select("4RL8_A_S11", "resi 259-268 & chain A & 4RL8 ")
cmd.color ("magenta", "4RL8_A_S11")


cmd.select("4RL8_barrel", "4RL8_A_S*")
cmd.show("cartoon", "4RL8_barrel")
cmd.zoom("4RL8_barrel")
