from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1EI5_A_S0", "resi 503-505 & chain A & 1EI5 ")
cmd.color ("red", "1EI5_A_S0")


cmd.select("1EI5_A_S1", "resi 513-515 & chain A & 1EI5 ")
cmd.color ("yellow", "1EI5_A_S1")


cmd.select("1EI5_barrel", "1EI5_A_S*")
cmd.show("cartoon", "1EI5_barrel")
cmd.zoom("1EI5_barrel")
