from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PBY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1PBY_A_S0", "resi 354-369 & chain A & 1PBY ")
cmd.color ("red", "1PBY_A_S0")


cmd.select("1PBY_A_S1", "resi 374-387 & chain A & 1PBY ")
cmd.color ("yellow", "1PBY_A_S1")


cmd.select("1PBY_A_S2", "resi 400-436 & chain A & 1PBY ")
cmd.color ("green", "1PBY_A_S2")


cmd.select("1PBY_A_S3", "resi 455-463 & chain A & 1PBY ")
cmd.color ("cyan", "1PBY_A_S3")


cmd.select("1PBY_A_S4", "resi 470-478 & chain A & 1PBY ")
cmd.color ("blue", "1PBY_A_S4")


cmd.select("1PBY_barrel", "1PBY_A_S*")
cmd.show("cartoon", "1PBY_barrel")
cmd.zoom("1PBY_barrel")
