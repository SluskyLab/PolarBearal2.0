from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6SLJ_B_S0", "resi 970-979 & chain B & 6SLJ ")
cmd.color ("red", "6SLJ_B_S0")


cmd.select("6SLJ_B_S1", "resi 1008-1016 & chain B & 6SLJ ")
cmd.color ("yellow", "6SLJ_B_S1")


cmd.select("6SLJ_barrel", "6SLJ_B_S*")
cmd.show("cartoon", "6SLJ_barrel")
cmd.zoom("6SLJ_barrel")
