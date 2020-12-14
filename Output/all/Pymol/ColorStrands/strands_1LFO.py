from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LFO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1LFO_A_S0", "resi 5-7 & chain A & 1LFO ")
cmd.color ("red", "1LFO_A_S0")


cmd.select("1LFO_A_S1", "resi 38-42 & chain A & 1LFO ")
cmd.color ("yellow", "1LFO_A_S1")


cmd.select("1LFO_A_S2", "resi 49-53 & chain A & 1LFO ")
cmd.color ("green", "1LFO_A_S2")


cmd.select("1LFO_barrel", "1LFO_A_S*")
cmd.show("cartoon", "1LFO_barrel")
cmd.zoom("1LFO_barrel")
