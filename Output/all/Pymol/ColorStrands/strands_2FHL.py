from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FHL.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2FHL_A_S0", "resi 8-13 & chain A & 2FHL ")
cmd.color ("red", "2FHL_A_S0")


cmd.select("2FHL_A_S1", "resi 16-21 & chain A & 2FHL ")
cmd.color ("yellow", "2FHL_A_S1")


cmd.select("2FHL_A_S2", "resi 27-34 & chain A & 2FHL ")
cmd.color ("green", "2FHL_A_S2")


cmd.select("2FHL_A_S3", "resi 47-53 & chain A & 2FHL ")
cmd.color ("cyan", "2FHL_A_S3")


cmd.select("2FHL_A_S4", "resi 62-66 & chain A & 2FHL ")
cmd.color ("blue", "2FHL_A_S4")


cmd.select("2FHL_A_S5", "resi 74-82 & chain A & 2FHL ")
cmd.color ("magenta", "2FHL_A_S5")


cmd.select("2FHL_A_S6", "resi 90-98 & chain A & 2FHL ")
cmd.color ("red", "2FHL_A_S6")


cmd.select("2FHL_A_S7", "resi 112-119 & chain A & 2FHL ")
cmd.color ("yellow", "2FHL_A_S7")


cmd.select("2FHL_barrel", "2FHL_A_S*")
cmd.show("cartoon", "2FHL_barrel")
cmd.zoom("2FHL_barrel")
