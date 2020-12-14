from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RLB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RLB_A_S0", "resi 17-27 & chain A & 4RLB ")
cmd.color ("red", "4RLB_A_S0")


cmd.select("4RLB_A_S1", "resi 30-38 & chain A & 4RLB ")
cmd.color ("yellow", "4RLB_A_S1")


cmd.select("4RLB_A_S2", "resi 42-59 & chain A & 4RLB ")
cmd.color ("green", "4RLB_A_S2")


cmd.select("4RLB_A_S3", "resi 65-81 & chain A & 4RLB ")
cmd.color ("cyan", "4RLB_A_S3")


cmd.select("4RLB_A_S4", "resi 94-114 & chain A & 4RLB ")
cmd.color ("blue", "4RLB_A_S4")


cmd.select("4RLB_A_S5", "resi 134-155 & chain A & 4RLB ")
cmd.color ("magenta", "4RLB_A_S5")


cmd.select("4RLB_A_S6", "resi 161-183 & chain A & 4RLB ")
cmd.color ("red", "4RLB_A_S6")


cmd.select("4RLB_A_S7", "resi 215-225 & chain A & 4RLB ")
cmd.color ("yellow", "4RLB_A_S7")


cmd.select("4RLB_barrel", "4RLB_A_S*")
cmd.show("cartoon", "4RLB_barrel")
cmd.zoom("4RLB_barrel")
