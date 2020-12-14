from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2QO4_A_S0", "resi 9-12 & chain A & 2QO4 ")
cmd.color ("red", "2QO4_A_S0")


cmd.select("2QO4_A_S1", "resi 37-40 & chain A & 2QO4 ")
cmd.color ("yellow", "2QO4_A_S1")


cmd.select("2QO4_A_S2", "resi 47-52 & chain A & 2QO4 ")
cmd.color ("green", "2QO4_A_S2")


cmd.select("2QO4_A_S3", "resi 58-68 & chain A & 2QO4 ")
cmd.color ("cyan", "2QO4_A_S3")


cmd.select("2QO4_A_S4", "resi 80-83 & chain A & 2QO4 ")
cmd.color ("blue", "2QO4_A_S4")


cmd.select("2QO4_A_S5", "resi 89-91 & chain A & 2QO4 ")
cmd.color ("magenta", "2QO4_A_S5")


cmd.select("2QO4_A_S6", "resi 97-101 & chain A & 2QO4 ")
cmd.color ("red", "2QO4_A_S6")


cmd.select("2QO4_A_S7", "resi 107-112 & chain A & 2QO4 ")
cmd.color ("yellow", "2QO4_A_S7")


cmd.select("2QO4_A_S8", "resi 118-125 & chain A & 2QO4 ")
cmd.color ("green", "2QO4_A_S8")


cmd.select("2QO4_barrel", "2QO4_A_S*")
cmd.show("cartoon", "2QO4_barrel")
cmd.zoom("2QO4_barrel")
