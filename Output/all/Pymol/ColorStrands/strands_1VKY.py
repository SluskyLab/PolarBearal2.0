from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VKY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1VKY_A_S0", "resi 27-29 & chain A & 1VKY ")
cmd.color ("red", "1VKY_A_S0")


cmd.select("1VKY_A_S1", "resi 331-333 & chain A & 1VKY ")
cmd.color ("yellow", "1VKY_A_S1")


cmd.select("1VKY_barrel", "1VKY_A_S*")
cmd.show("cartoon", "1VKY_barrel")
cmd.zoom("1VKY_barrel")
