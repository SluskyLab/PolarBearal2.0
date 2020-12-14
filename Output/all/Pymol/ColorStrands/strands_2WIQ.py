from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WIQ.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2WIQ_A_S0", "resi 196-206 & chain A & 2WIQ ")
cmd.color ("red", "2WIQ_A_S0")


cmd.select("2WIQ_A_S1", "resi 213-223 & chain A & 2WIQ ")
cmd.color ("yellow", "2WIQ_A_S1")


cmd.select("2WIQ_barrel", "2WIQ_A_S*")
cmd.show("cartoon", "2WIQ_barrel")
cmd.zoom("2WIQ_barrel")
