from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VPR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1VPR_A_S0", "resi 1195-1196 & chain A & 1VPR ")
cmd.color ("red", "1VPR_A_S0")


cmd.select("1VPR_A_S1", "resi 1204-1206 & chain A & 1VPR ")
cmd.color ("yellow", "1VPR_A_S1")


cmd.select("1VPR_barrel", "1VPR_A_S*")
cmd.show("cartoon", "1VPR_barrel")
cmd.zoom("1VPR_barrel")
