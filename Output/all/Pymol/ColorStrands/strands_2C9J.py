from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2C9J.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2C9J_A_S0", "resi 87-93 & chain A & 2C9J ")
cmd.color ("red", "2C9J_A_S0")


cmd.select("2C9J_A_S1", "resi 101-107 & chain A & 2C9J ")
cmd.color ("yellow", "2C9J_A_S1")


cmd.select("2C9J_barrel", "2C9J_A_S*")
cmd.show("cartoon", "2C9J_barrel")
cmd.zoom("2C9J_barrel")
