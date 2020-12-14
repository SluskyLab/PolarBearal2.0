from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PIB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3PIB_A_S0", "resi 194-205 & chain A & 3PIB ")
cmd.color ("red", "3PIB_A_S0")


cmd.select("3PIB_A_S1", "resi 209-220 & chain A & 3PIB ")
cmd.color ("yellow", "3PIB_A_S1")


cmd.select("3PIB_barrel", "3PIB_A_S*")
cmd.show("cartoon", "3PIB_barrel")
cmd.zoom("3PIB_barrel")
