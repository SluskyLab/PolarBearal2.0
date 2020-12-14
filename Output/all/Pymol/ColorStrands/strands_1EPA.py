from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EPA.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1EPA_A_S0", "resi 13-17 & chain A & 1EPA ")
cmd.color ("red", "1EPA_A_S0")


cmd.select("1EPA_A_S1", "resi 37-42 & chain A & 1EPA ")
cmd.color ("yellow", "1EPA_A_S1")


cmd.select("1EPA_A_S2", "resi 48-54 & chain A & 1EPA ")
cmd.color ("green", "1EPA_A_S2")


cmd.select("1EPA_A_S3", "resi 61-70 & chain A & 1EPA ")
cmd.color ("cyan", "1EPA_A_S3")


cmd.select("1EPA_A_S4", "resi 75-78 & chain A & 1EPA ")
cmd.color ("blue", "1EPA_A_S4")


cmd.select("1EPA_A_S5", "resi 85-90 & chain A & 1EPA ")
cmd.color ("magenta", "1EPA_A_S5")


cmd.select("1EPA_A_S6", "resi 99-105 & chain A & 1EPA ")
cmd.color ("red", "1EPA_A_S6")


cmd.select("1EPA_barrel", "1EPA_A_S*")
cmd.show("cartoon", "1EPA_barrel")
cmd.zoom("1EPA_barrel")
