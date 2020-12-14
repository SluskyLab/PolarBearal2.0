from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JSG.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1JSG_A_S0", "resi 26-28 & chain A & 1JSG ")
cmd.color ("red", "1JSG_A_S0")


cmd.select("1JSG_A_S1", "resi 32-34 & chain A & 1JSG ")
cmd.color ("yellow", "1JSG_A_S1")


cmd.select("1JSG_barrel", "1JSG_A_S*")
cmd.show("cartoon", "1JSG_barrel")
cmd.zoom("1JSG_barrel")
