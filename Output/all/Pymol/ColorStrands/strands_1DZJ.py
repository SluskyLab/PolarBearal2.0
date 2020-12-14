from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1DZJ.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1DZJ_A_S0", "resi 71-73 & chain A & 1DZJ ")
cmd.color ("red", "1DZJ_A_S0")


cmd.select("1DZJ_A_S1", "resi 77-79 & chain A & 1DZJ ")
cmd.color ("yellow", "1DZJ_A_S1")


cmd.select("1DZJ_barrel", "1DZJ_A_S*")
cmd.show("cartoon", "1DZJ_barrel")
cmd.zoom("1DZJ_barrel")
