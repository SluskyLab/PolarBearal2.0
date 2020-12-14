from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QWD.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1QWD_A_S0", "resi 128-132 & chain A & 1QWD ")
cmd.color ("red", "1QWD_A_S0")


cmd.select("1QWD_A_S1", "resi 137-141 & chain A & 1QWD ")
cmd.color ("yellow", "1QWD_A_S1")


cmd.select("1QWD_barrel", "1QWD_A_S*")
cmd.show("cartoon", "1QWD_barrel")
cmd.zoom("1QWD_barrel")
