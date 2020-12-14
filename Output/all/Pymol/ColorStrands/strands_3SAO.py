from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SAO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SAO_A_S0", "resi 10-19 & chain A & 3SAO ")
cmd.color ("red", "3SAO_A_S0")


cmd.select("3SAO_A_S1", "resi 35-41 & chain A & 3SAO ")
cmd.color ("yellow", "3SAO_A_S1")


cmd.select("3SAO_A_S2", "resi 45-52 & chain A & 3SAO ")
cmd.color ("green", "3SAO_A_S2")


cmd.select("3SAO_A_S3", "resi 59-66 & chain A & 3SAO ")
cmd.color ("cyan", "3SAO_A_S3")


cmd.select("3SAO_A_S4", "resi 75-77 & chain A & 3SAO ")
cmd.color ("blue", "3SAO_A_S4")


cmd.select("3SAO_A_S5", "resi 81-90 & chain A & 3SAO ")
cmd.color ("magenta", "3SAO_A_S5")


cmd.select("3SAO_A_S6", "resi 94-102 & chain A & 3SAO ")
cmd.color ("red", "3SAO_A_S6")


cmd.select("3SAO_A_S7", "resi 108-143 & chain A & 3SAO ")
cmd.color ("yellow", "3SAO_A_S7")


cmd.select("3SAO_barrel", "3SAO_A_S*")
cmd.show("cartoon", "3SAO_barrel")
cmd.zoom("3SAO_barrel")
