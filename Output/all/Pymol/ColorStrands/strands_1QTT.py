from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QTT.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QTT_A_S0", "resi 23-25 & chain A & 1QTT ")
cmd.color ("red", "1QTT_A_S0")


cmd.select("1QTT_A_S1", "resi 29-31 & chain A & 1QTT ")
cmd.color ("yellow", "1QTT_A_S1")


cmd.select("1QTT_barrel", "1QTT_A_S*")
cmd.show("cartoon", "1QTT_barrel")
cmd.zoom("1QTT_barrel")
