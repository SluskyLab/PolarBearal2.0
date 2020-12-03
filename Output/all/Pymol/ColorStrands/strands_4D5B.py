from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D5B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4D5B_A_S0", "resi 22-38 & chain A & 4D5B ")
cmd.color ("red", "4D5B_A_S0")


cmd.select("4D5B_A_S1", "resi 42-60 & chain A & 4D5B ")
cmd.color ("yellow", "4D5B_A_S1")


cmd.select("4D5B_A_S2", "resi 64-79 & chain A & 4D5B ")
cmd.color ("green", "4D5B_A_S2")


cmd.select("4D5B_A_S3", "resi 85-100 & chain A & 4D5B ")
cmd.color ("cyan", "4D5B_A_S3")


cmd.select("4D5B_A_S4", "resi 105-122 & chain A & 4D5B ")
cmd.color ("blue", "4D5B_A_S4")


cmd.select("4D5B_A_S5", "resi 129-146 & chain A & 4D5B ")
cmd.color ("magenta", "4D5B_A_S5")


cmd.select("4D5B_A_S6", "resi 150-165 & chain A & 4D5B ")
cmd.color ("red", "4D5B_A_S6")


cmd.select("4D5B_A_S7", "resi 171-186 & chain A & 4D5B ")
cmd.color ("yellow", "4D5B_A_S7")


cmd.select("4D5B_A_S8", "resi 189-206 & chain A & 4D5B ")
cmd.color ("green", "4D5B_A_S8")


cmd.select("4D5B_A_S9", "resi 213-230 & chain A & 4D5B ")
cmd.color ("cyan", "4D5B_A_S9")


cmd.select("4D5B_A_S10", "resi 236-251 & chain A & 4D5B ")
cmd.color ("blue", "4D5B_A_S10")


cmd.select("4D5B_A_S11", "resi 262-278 & chain A & 4D5B ")
cmd.color ("magenta", "4D5B_A_S11")


cmd.select("4D5B_A_S12", "resi 282-298 & chain A & 4D5B ")
cmd.color ("red", "4D5B_A_S12")


cmd.select("4D5B_A_S13", "resi 309-322 & chain A & 4D5B ")
cmd.color ("yellow", "4D5B_A_S13")


cmd.select("4D5B_barrel", "4D5B_A_S*")
cmd.show("cartoon", "4D5B_barrel")
cmd.zoom("4D5B_barrel")
