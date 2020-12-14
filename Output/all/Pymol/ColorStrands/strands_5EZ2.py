from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5EZ2.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5EZ2_A_S0", "resi 90-94 & chain A & 5EZ2 ")
cmd.color ("red", "5EZ2_A_S0")


cmd.select("5EZ2_A_S1", "resi 105-109 & chain A & 5EZ2 ")
cmd.color ("yellow", "5EZ2_A_S1")


cmd.select("5EZ2_barrel", "5EZ2_A_S*")
cmd.show("cartoon", "5EZ2_barrel")
cmd.zoom("5EZ2_barrel")
