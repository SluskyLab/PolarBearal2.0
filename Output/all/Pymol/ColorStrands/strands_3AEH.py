from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3AEH.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3AEH_A_S0", "resi 1115-1129 & chain A & 3AEH ")
cmd.color ("red", "3AEH_A_S0")


cmd.select("3AEH_A_S1", "resi 1133-1148 & chain A & 3AEH ")
cmd.color ("yellow", "3AEH_A_S1")


cmd.select("3AEH_A_S2", "resi 1154-1169 & chain A & 3AEH ")
cmd.color ("green", "3AEH_A_S2")


cmd.select("3AEH_A_S3", "resi 1174-1189 & chain A & 3AEH ")
cmd.color ("cyan", "3AEH_A_S3")


cmd.select("3AEH_A_S4", "resi 1195-1210 & chain A & 3AEH ")
cmd.color ("blue", "3AEH_A_S4")


cmd.select("3AEH_A_S5", "resi 1219-1238 & chain A & 3AEH ")
cmd.color ("magenta", "3AEH_A_S5")


cmd.select("3AEH_A_S6", "resi 1241-1258 & chain A & 3AEH ")
cmd.color ("red", "3AEH_A_S6")


cmd.select("3AEH_A_S7", "resi 1276-1291 & chain A & 3AEH ")
cmd.color ("yellow", "3AEH_A_S7")


cmd.select("3AEH_A_S8", "resi 1297-1310 & chain A & 3AEH ")
cmd.color ("green", "3AEH_A_S8")


cmd.select("3AEH_A_S9", "resi 1332-1345 & chain A & 3AEH ")
cmd.color ("cyan", "3AEH_A_S9")


cmd.select("3AEH_A_S10", "resi 1348-1359 & chain A & 3AEH ")
cmd.color ("blue", "3AEH_A_S10")


cmd.select("3AEH_A_S11", "resi 1366-1377 & chain A & 3AEH ")
cmd.color ("magenta", "3AEH_A_S11")


cmd.select("3AEH_barrel", "3AEH_A_S*")
cmd.show("cartoon", "3AEH_barrel")
cmd.zoom("3AEH_barrel")
