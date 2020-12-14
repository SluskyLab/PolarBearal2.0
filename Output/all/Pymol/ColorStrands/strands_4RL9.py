from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL9.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RL9_A_S0", "resi 19-27 & chain A & 4RL9 ")
cmd.color ("red", "4RL9_A_S0")


cmd.select("4RL9_A_S1", "resi 30-38 & chain A & 4RL9 ")
cmd.color ("yellow", "4RL9_A_S1")


cmd.select("4RL9_A_S2", "resi 42-55 & chain A & 4RL9 ")
cmd.color ("green", "4RL9_A_S2")


cmd.select("4RL9_A_S3", "resi 65-81 & chain A & 4RL9 ")
cmd.color ("cyan", "4RL9_A_S3")


cmd.select("4RL9_A_S4", "resi 94-114 & chain A & 4RL9 ")
cmd.color ("blue", "4RL9_A_S4")


cmd.select("4RL9_A_S5", "resi 136-160 & chain A & 4RL9 ")
cmd.color ("magenta", "4RL9_A_S5")


cmd.select("4RL9_A_S6", "resi 163-188 & chain A & 4RL9 ")
cmd.color ("red", "4RL9_A_S6")


cmd.select("4RL9_A_S7", "resi 217-227 & chain A & 4RL9 ")
cmd.color ("yellow", "4RL9_A_S7")


cmd.select("4RL9_barrel", "4RL9_A_S*")
cmd.show("cartoon", "4RL9_barrel")
cmd.zoom("4RL9_barrel")
