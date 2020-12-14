from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QOM.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2QOM_A_S0", "resi 1039-1052 & chain A & 2QOM ")
cmd.color ("red", "2QOM_A_S0")


cmd.select("2QOM_A_S1", "resi 1056-1071 & chain A & 2QOM ")
cmd.color ("yellow", "2QOM_A_S1")


cmd.select("2QOM_A_S2", "resi 1077-1092 & chain A & 2QOM ")
cmd.color ("green", "2QOM_A_S2")


cmd.select("2QOM_A_S3", "resi 1097-1112 & chain A & 2QOM ")
cmd.color ("cyan", "2QOM_A_S3")


cmd.select("2QOM_A_S4", "resi 1118-1133 & chain A & 2QOM ")
cmd.color ("blue", "2QOM_A_S4")


cmd.select("2QOM_A_S5", "resi 1142-1161 & chain A & 2QOM ")
cmd.color ("magenta", "2QOM_A_S5")


cmd.select("2QOM_A_S6", "resi 1164-1182 & chain A & 2QOM ")
cmd.color ("red", "2QOM_A_S6")


cmd.select("2QOM_A_S7", "resi 1195-1214 & chain A & 2QOM ")
cmd.color ("yellow", "2QOM_A_S7")


cmd.select("2QOM_A_S8", "resi 1220-1235 & chain A & 2QOM ")
cmd.color ("green", "2QOM_A_S8")


cmd.select("2QOM_A_S9", "resi 1255-1268 & chain A & 2QOM ")
cmd.color ("cyan", "2QOM_A_S9")


cmd.select("2QOM_A_S10", "resi 1271-1282 & chain A & 2QOM ")
cmd.color ("blue", "2QOM_A_S10")


cmd.select("2QOM_A_S11", "resi 1289-1300 & chain A & 2QOM ")
cmd.color ("magenta", "2QOM_A_S11")


cmd.select("2QOM_barrel", "2QOM_A_S*")
cmd.show("cartoon", "2QOM_barrel")
cmd.zoom("2QOM_barrel")
