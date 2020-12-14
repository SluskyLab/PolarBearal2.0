from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4UU3.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4UU3_A_S0", "resi 26-32 & chain A & 4UU3 ")
cmd.color ("red", "4UU3_A_S0")


cmd.select("4UU3_A_S1", "resi 36-43 & chain A & 4UU3 ")
cmd.color ("yellow", "4UU3_A_S1")


cmd.select("4UU3_barrel", "4UU3_A_S*")
cmd.show("cartoon", "4UU3_barrel")
cmd.zoom("4UU3_barrel")
