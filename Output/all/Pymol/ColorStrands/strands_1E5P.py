from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1E5P_A_S0", "resi 32-39 & chain A & 1E5P ")
cmd.color ("red", "1E5P_A_S0")


cmd.select("1E5P_A_S1", "resi 43-51 & chain A & 1E5P ")
cmd.color ("yellow", "1E5P_A_S1")


cmd.select("1E5P_A_S2", "resi 58-67 & chain A & 1E5P ")
cmd.color ("green", "1E5P_A_S2")


cmd.select("1E5P_A_S3", "resi 71-74 & chain A & 1E5P ")
cmd.color ("cyan", "1E5P_A_S3")


cmd.select("1E5P_A_S4", "resi 79-86 & chain A & 1E5P ")
cmd.color ("blue", "1E5P_A_S4")


cmd.select("1E5P_A_S5", "resi 93-99 & chain A & 1E5P ")
cmd.color ("magenta", "1E5P_A_S5")


cmd.select("1E5P_barrel", "1E5P_A_S*")
cmd.show("cartoon", "1E5P_barrel")
cmd.zoom("1E5P_barrel")
