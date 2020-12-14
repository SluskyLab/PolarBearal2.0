from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4I3B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4I3B_A_S0", "resi 7-12 & chain A & 4I3B ")
cmd.color ("red", "4I3B_A_S0")


cmd.select("4I3B_A_S1", "resi 40-46 & chain A & 4I3B ")
cmd.color ("yellow", "4I3B_A_S1")


cmd.select("4I3B_A_S2", "resi 50-56 & chain A & 4I3B ")
cmd.color ("green", "4I3B_A_S2")


cmd.select("4I3B_A_S3", "resi 63-72 & chain A & 4I3B ")
cmd.color ("cyan", "4I3B_A_S3")


cmd.select("4I3B_A_S4", "resi 87-90 & chain A & 4I3B ")
cmd.color ("blue", "4I3B_A_S4")


cmd.select("4I3B_A_S5", "resi 97-102 & chain A & 4I3B ")
cmd.color ("magenta", "4I3B_A_S5")


cmd.select("4I3B_A_S6", "resi 108-113 & chain A & 4I3B ")
cmd.color ("red", "4I3B_A_S6")


cmd.select("4I3B_A_S7", "resi 119-124 & chain A & 4I3B ")
cmd.color ("yellow", "4I3B_A_S7")


cmd.select("4I3B_A_S8", "resi 130-135 & chain A & 4I3B ")
cmd.color ("green", "4I3B_A_S8")


cmd.select("4I3B_barrel", "4I3B_A_S*")
cmd.show("cartoon", "4I3B_barrel")
cmd.zoom("4I3B_barrel")
