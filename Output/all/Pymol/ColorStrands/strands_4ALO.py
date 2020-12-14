from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4ALO_A_S0", "resi 82-86 & chain A & 4ALO ")
cmd.color ("red", "4ALO_A_S0")


cmd.select("4ALO_A_S1", "resi 92-96 & chain A & 4ALO ")
cmd.color ("yellow", "4ALO_A_S1")


cmd.select("4ALO_barrel", "4ALO_A_S*")
cmd.show("cartoon", "4ALO_barrel")
cmd.zoom("4ALO_barrel")
