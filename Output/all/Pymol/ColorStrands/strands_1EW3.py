from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EW3.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1EW3_A_S0", "resi 91-93 & chain A & 1EW3 ")
cmd.color ("red", "1EW3_A_S0")


cmd.select("1EW3_A_S1", "resi 98-100 & chain A & 1EW3 ")
cmd.color ("yellow", "1EW3_A_S1")


cmd.select("1EW3_barrel", "1EW3_A_S*")
cmd.show("cartoon", "1EW3_barrel")
cmd.zoom("1EW3_barrel")
