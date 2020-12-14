from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HPW.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2HPW_A_S0", "resi 201-209 & chain A & 2HPW ")
cmd.color ("red", "2HPW_A_S0")


cmd.select("2HPW_A_S1", "resi 221-229 & chain A & 2HPW ")
cmd.color ("yellow", "2HPW_A_S1")


cmd.select("2HPW_barrel", "2HPW_A_S*")
cmd.show("cartoon", "2HPW_barrel")
cmd.zoom("2HPW_barrel")
