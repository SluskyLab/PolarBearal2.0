from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GR7.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2GR7_A_S0", "resi 1045-1055 & chain A & 2GR7 ")
cmd.color ("red", "2GR7_A_S0")


cmd.select("2GR7_A_S1", "resi 1058-1068 & chain A & 2GR7 ")
cmd.color ("yellow", "2GR7_A_S1")


cmd.select("2GR7_A_S2", "resi 1074-1083 & chain A & 2GR7 ")
cmd.color ("green", "2GR7_A_S2")


cmd.select("2GR7_A_S3", "resi 1087-1097 & chain A & 2GR7 ")
cmd.color ("cyan", "2GR7_A_S3")


cmd.select("2GR7_B_S0", "resi 1045-1055 & chain B & 2GR7 ")
cmd.color ("red", "2GR7_B_S0")


cmd.select("2GR7_B_S1", "resi 1058-1068 & chain B & 2GR7 ")
cmd.color ("yellow", "2GR7_B_S1")


cmd.select("2GR7_B_S2", "resi 1074-1083 & chain B & 2GR7 ")
cmd.color ("green", "2GR7_B_S2")


cmd.select("2GR7_B_S3", "resi 1087-1097 & chain B & 2GR7 ")
cmd.color ("cyan", "2GR7_B_S3")


cmd.select("2GR7_C_S0", "resi 1045-1055 & chain C & 2GR7 ")
cmd.color ("red", "2GR7_C_S0")


cmd.select("2GR7_C_S1", "resi 1058-1068 & chain C & 2GR7 ")
cmd.color ("yellow", "2GR7_C_S1")


cmd.select("2GR7_C_S2", "resi 1074-1083 & chain C & 2GR7 ")
cmd.color ("green", "2GR7_C_S2")


cmd.select("2GR7_C_S3", "resi 1087-1097 & chain C & 2GR7 ")
cmd.color ("cyan", "2GR7_C_S3")


cmd.select("2GR7_D_S0", "resi 1045-1055 & chain D & 2GR7 ")
cmd.color ("red", "2GR7_D_S0")


cmd.select("2GR7_D_S1", "resi 1058-1068 & chain D & 2GR7 ")
cmd.color ("yellow", "2GR7_D_S1")


cmd.select("2GR7_D_S2", "resi 1074-1083 & chain D & 2GR7 ")
cmd.color ("green", "2GR7_D_S2")


cmd.select("2GR7_D_S3", "resi 1087-1097 & chain D & 2GR7 ")
cmd.color ("cyan", "2GR7_D_S3")


cmd.select("2GR7_E_S0", "resi 1045-1055 & chain E & 2GR7 ")
cmd.color ("red", "2GR7_E_S0")


cmd.select("2GR7_E_S1", "resi 1058-1068 & chain E & 2GR7 ")
cmd.color ("yellow", "2GR7_E_S1")


cmd.select("2GR7_E_S2", "resi 1074-1083 & chain E & 2GR7 ")
cmd.color ("green", "2GR7_E_S2")


cmd.select("2GR7_E_S3", "resi 1087-1097 & chain E & 2GR7 ")
cmd.color ("cyan", "2GR7_E_S3")


cmd.select("2GR7_F_S0", "resi 1045-1055 & chain F & 2GR7 ")
cmd.color ("red", "2GR7_F_S0")


cmd.select("2GR7_F_S1", "resi 1058-1068 & chain F & 2GR7 ")
cmd.color ("yellow", "2GR7_F_S1")


cmd.select("2GR7_F_S2", "resi 1074-1083 & chain F & 2GR7 ")
cmd.color ("green", "2GR7_F_S2")


cmd.select("2GR7_F_S3", "resi 1087-1097 & chain F & 2GR7 ")
cmd.color ("cyan", "2GR7_F_S3")


cmd.select("2GR7_barrel", "2GR7_A_S* or 2GR7_B_S* or 2GR7_C_S* or 2GR7_D_S* or 2GR7_E_S* or 2GR7_F_S*")
cmd.show("cartoon", "2GR7_barrel")
cmd.zoom("2GR7_barrel")
