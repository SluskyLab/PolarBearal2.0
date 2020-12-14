from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXG.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5IXG_B_S0", "resi 7-17 & chain B & 5IXG ")
cmd.color ("red", "5IXG_B_S0")


cmd.select("5IXG_B_S1", "resi 34-45 & chain B & 5IXG ")
cmd.color ("yellow", "5IXG_B_S1")


cmd.select("5IXG_B_S2", "resi 49-63 & chain B & 5IXG ")
cmd.color ("green", "5IXG_B_S2")


cmd.select("5IXG_B_S3", "resi 87-94 & chain B & 5IXG ")
cmd.color ("cyan", "5IXG_B_S3")


cmd.select("5IXG_B_S4", "resi 101-108 & chain B & 5IXG ")
cmd.color ("blue", "5IXG_B_S4")


cmd.select("5IXG_B_S5", "resi 114-126 & chain B & 5IXG ")
cmd.color ("magenta", "5IXG_B_S5")


cmd.select("5IXG_B_S6", "resi 135-144 & chain B & 5IXG ")
cmd.color ("red", "5IXG_B_S6")


cmd.select("5IXG_B_S7", "resi 163-174 & chain B & 5IXG ")
cmd.color ("yellow", "5IXG_B_S7")


cmd.select("5IXG_barrel", "5IXG_B_S*")
cmd.show("cartoon", "5IXG_barrel")
cmd.zoom("5IXG_barrel")
