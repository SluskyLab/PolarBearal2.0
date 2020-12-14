from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2JOZ.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2JOZ_A_S0", "resi 20-28 & chain A & 2JOZ ")
cmd.color ("red", "2JOZ_A_S0")


cmd.select("2JOZ_A_S1", "resi 32-39 & chain A & 2JOZ ")
cmd.color ("yellow", "2JOZ_A_S1")


cmd.select("2JOZ_A_S2", "resi 43-50 & chain A & 2JOZ ")
cmd.color ("green", "2JOZ_A_S2")


cmd.select("2JOZ_A_S3", "resi 62-68 & chain A & 2JOZ ")
cmd.color ("cyan", "2JOZ_A_S3")


cmd.select("2JOZ_A_S4", "resi 75-80 & chain A & 2JOZ ")
cmd.color ("blue", "2JOZ_A_S4")


cmd.select("2JOZ_A_S5", "resi 88-91 & chain A & 2JOZ ")
cmd.color ("magenta", "2JOZ_A_S5")


cmd.select("2JOZ_A_S6", "resi 97-101 & chain A & 2JOZ ")
cmd.color ("red", "2JOZ_A_S6")


cmd.select("2JOZ_A_S7", "resi 107-112 & chain A & 2JOZ ")
cmd.color ("yellow", "2JOZ_A_S7")


cmd.select("2JOZ_barrel", "2JOZ_A_S*")
cmd.show("cartoon", "2JOZ_barrel")
cmd.zoom("2JOZ_barrel")
