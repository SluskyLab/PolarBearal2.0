from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1NYC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1NYC_A_S0", "resi 54-59 & chain A & 1NYC ")
cmd.color ("red", "1NYC_A_S0")


cmd.select("1NYC_A_S1", "resi 64-68 & chain A & 1NYC ")
cmd.color ("yellow", "1NYC_A_S1")


cmd.select("1NYC_barrel", "1NYC_A_S*")
cmd.show("cartoon", "1NYC_barrel")
cmd.zoom("1NYC_barrel")
