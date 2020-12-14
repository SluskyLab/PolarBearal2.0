from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4DKN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4DKN_A_S0", "resi 192-200 & chain A & 4DKN ")
cmd.color ("red", "4DKN_A_S0")


cmd.select("4DKN_A_S1", "resi 207-215 & chain A & 4DKN ")
cmd.color ("yellow", "4DKN_A_S1")


cmd.select("4DKN_barrel", "4DKN_A_S*")
cmd.show("cartoon", "4DKN_barrel")
cmd.zoom("4DKN_barrel")
