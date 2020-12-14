from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1Y0G_A_S0", "resi 36-38 & chain A & 1Y0G ")
cmd.color ("red", "1Y0G_A_S0")


cmd.select("1Y0G_A_S1", "resi 50-52 & chain A & 1Y0G ")
cmd.color ("yellow", "1Y0G_A_S1")


cmd.select("1Y0G_barrel", "1Y0G_A_S*")
cmd.show("cartoon", "1Y0G_barrel")
cmd.zoom("1Y0G_barrel")
