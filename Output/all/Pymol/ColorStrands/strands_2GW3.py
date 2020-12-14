from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GW3.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2GW3_A_S0", "resi 191-202 & chain A & 2GW3 ")
cmd.color ("red", "2GW3_A_S0")


cmd.select("2GW3_A_S1", "resi 207-217 & chain A & 2GW3 ")
cmd.color ("yellow", "2GW3_A_S1")


cmd.select("2GW3_barrel", "2GW3_A_S*")
cmd.show("cartoon", "2GW3_barrel")
cmd.zoom("2GW3_barrel")
