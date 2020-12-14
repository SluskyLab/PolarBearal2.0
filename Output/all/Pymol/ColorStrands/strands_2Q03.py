from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Q03.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2Q03_A_S0", "resi 6-27 & chain A & 2Q03 ")
cmd.color ("red", "2Q03_A_S0")


cmd.select("2Q03_A_S1", "resi 31-42 & chain A & 2Q03 ")
cmd.color ("yellow", "2Q03_A_S1")


cmd.select("2Q03_A_S2", "resi 47-59 & chain A & 2Q03 ")
cmd.color ("green", "2Q03_A_S2")


cmd.select("2Q03_A_S3", "resi 63-75 & chain A & 2Q03 ")
cmd.color ("cyan", "2Q03_A_S3")


cmd.select("2Q03_A_S4", "resi 80-91 & chain A & 2Q03 ")
cmd.color ("blue", "2Q03_A_S4")


cmd.select("2Q03_A_S5", "resi 96-110 & chain A & 2Q03 ")
cmd.color ("magenta", "2Q03_A_S5")


cmd.select("2Q03_A_S6", "resi 115-122 & chain A & 2Q03 ")
cmd.color ("red", "2Q03_A_S6")


cmd.select("2Q03_A_S7", "resi 129-136 & chain A & 2Q03 ")
cmd.color ("yellow", "2Q03_A_S7")


cmd.select("2Q03_barrel", "2Q03_A_S*")
cmd.show("cartoon", "2Q03_barrel")
cmd.zoom("2Q03_barrel")
