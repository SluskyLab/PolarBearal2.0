from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UUN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1UUN_B_S0", "resi 110-120 & chain B & 1UUN ")
cmd.color ("red", "1UUN_B_S0")


cmd.select("1UUN_B_S1", "resi 173-178 & chain B & 1UUN ")
cmd.color ("yellow", "1UUN_B_S1")


cmd.select("1UUN_B_S2", "resi 110-120 & chain B & 1UUN ")
cmd.color ("green", "1UUN_B_S2")


cmd.select("1UUN_B_S3", "resi 173-178 & chain B & 1UUN ")
cmd.color ("cyan", "1UUN_B_S3")


cmd.select("1UUN_E_S0", "resi 110-120 & chain E & 1UUN ")
cmd.color ("red", "1UUN_E_S0")


cmd.select("1UUN_E_S1", "resi 173-178 & chain E & 1UUN ")
cmd.color ("yellow", "1UUN_E_S1")


cmd.select("1UUN_E_S2", "resi 110-120 & chain E & 1UUN ")
cmd.color ("green", "1UUN_E_S2")


cmd.select("1UUN_E_S3", "resi 173-178 & chain E & 1UUN ")
cmd.color ("cyan", "1UUN_E_S3")


cmd.select("1UUN_barrel", "1UUN_B_S* or 1UUN_E_S*")
cmd.show("cartoon", "1UUN_barrel")
cmd.zoom("1UUN_barrel")
