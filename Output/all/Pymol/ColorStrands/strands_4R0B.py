from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4R0B_A_S0", "resi 82-84 & chain A & 4R0B ")
cmd.color ("red", "4R0B_A_S0")


cmd.select("4R0B_A_S1", "resi 90-92 & chain A & 4R0B ")
cmd.color ("yellow", "4R0B_A_S1")


cmd.select("4R0B_barrel", "4R0B_A_S*")
cmd.show("cartoon", "4R0B_barrel")
cmd.zoom("4R0B_barrel")
