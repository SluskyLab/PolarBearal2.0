from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2L5P_A_S0", "resi 51-55 & chain A & 2L5P ")
cmd.color ("red", "2L5P_A_S0")


cmd.select("2L5P_A_S1", "resi 74-79 & chain A & 2L5P ")
cmd.color ("yellow", "2L5P_A_S1")


cmd.select("2L5P_A_S2", "resi 86-92 & chain A & 2L5P ")
cmd.color ("green", "2L5P_A_S2")


cmd.select("2L5P_A_S3", "resi 99-108 & chain A & 2L5P ")
cmd.color ("cyan", "2L5P_A_S3")


cmd.select("2L5P_A_S4", "resi 113-116 & chain A & 2L5P ")
cmd.color ("blue", "2L5P_A_S4")


cmd.select("2L5P_A_S5", "resi 128-136 & chain A & 2L5P ")
cmd.color ("magenta", "2L5P_A_S5")


cmd.select("2L5P_A_S6", "resi 140-146 & chain A & 2L5P ")
cmd.color ("red", "2L5P_A_S6")


cmd.select("2L5P_barrel", "2L5P_A_S*")
cmd.show("cartoon", "2L5P_barrel")
cmd.zoom("2L5P_barrel")
