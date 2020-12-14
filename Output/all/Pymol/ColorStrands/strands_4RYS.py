from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RYS.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RYS_A_S0", "resi 92-98 & chain A & 4RYS ")
cmd.color ("red", "4RYS_A_S0")


cmd.select("4RYS_A_S1", "resi 106-112 & chain A & 4RYS ")
cmd.color ("yellow", "4RYS_A_S1")


cmd.select("4RYS_barrel", "4RYS_A_S*")
cmd.show("cartoon", "4RYS_barrel")
cmd.zoom("4RYS_barrel")
