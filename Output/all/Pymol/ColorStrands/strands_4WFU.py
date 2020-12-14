from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4WFU.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4WFU_A_S0", "resi 71-73 & chain A & 4WFU ")
cmd.color ("red", "4WFU_A_S0")


cmd.select("4WFU_A_S1", "resi 77-79 & chain A & 4WFU ")
cmd.color ("yellow", "4WFU_A_S1")


cmd.select("4WFU_barrel", "4WFU_A_S*")
cmd.show("cartoon", "4WFU_barrel")
cmd.zoom("4WFU_barrel")
