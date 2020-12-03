from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MEE.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4MEE_A_S0", "resi 1005-1018 & chain A & 4MEE ")
cmd.color ("red", "4MEE_A_S0")


cmd.select("4MEE_A_S1", "resi 1023-1043 & chain A & 4MEE ")
cmd.color ("yellow", "4MEE_A_S1")


cmd.select("4MEE_A_S2", "resi 1048-1066 & chain A & 4MEE ")
cmd.color ("green", "4MEE_A_S2")


cmd.select("4MEE_A_S3", "resi 1071-1089 & chain A & 4MEE ")
cmd.color ("cyan", "4MEE_A_S3")


cmd.select("4MEE_A_S4", "resi 1099-1116 & chain A & 4MEE ")
cmd.color ("blue", "4MEE_A_S4")


cmd.select("4MEE_A_S5", "resi 1121-1143 & chain A & 4MEE ")
cmd.color ("magenta", "4MEE_A_S5")


cmd.select("4MEE_A_S6", "resi 1150-1171 & chain A & 4MEE ")
cmd.color ("red", "4MEE_A_S6")


cmd.select("4MEE_A_S7", "resi 1179-1200 & chain A & 4MEE ")
cmd.color ("yellow", "4MEE_A_S7")


cmd.select("4MEE_A_S8", "resi 1211-1230 & chain A & 4MEE ")
cmd.color ("green", "4MEE_A_S8")


cmd.select("4MEE_A_S9", "resi 1234-1254 & chain A & 4MEE ")
cmd.color ("cyan", "4MEE_A_S9")


cmd.select("4MEE_A_S10", "resi 1258-1268 & chain A & 4MEE ")
cmd.color ("blue", "4MEE_A_S10")


cmd.select("4MEE_A_S11", "resi 1275-1284 & chain A & 4MEE ")
cmd.color ("magenta", "4MEE_A_S11")


cmd.select("4MEE_barrel", "4MEE_A_S*")
cmd.show("cartoon", "4MEE_barrel")
cmd.zoom("4MEE_barrel")
