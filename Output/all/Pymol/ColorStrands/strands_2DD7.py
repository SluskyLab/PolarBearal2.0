from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2DD7.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2DD7_A_S0", "resi 189-197 & chain A & 2DD7 ")
cmd.color ("red", "2DD7_A_S0")


cmd.select("2DD7_A_S1", "resi 204-212 & chain A & 2DD7 ")
cmd.color ("yellow", "2DD7_A_S1")


cmd.select("2DD7_barrel", "2DD7_A_S*")
cmd.show("cartoon", "2DD7_barrel")
cmd.zoom("2DD7_barrel")
