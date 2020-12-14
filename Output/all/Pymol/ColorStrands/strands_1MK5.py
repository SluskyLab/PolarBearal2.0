from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MK5.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1MK5_A_S0", "resi 19-23 & chain A & 1MK5 ")
cmd.color ("red", "1MK5_A_S0")


cmd.select("1MK5_A_S1", "resi 27-32 & chain A & 1MK5 ")
cmd.color ("yellow", "1MK5_A_S1")


cmd.select("1MK5_A_S2", "resi 37-44 & chain A & 1MK5 ")
cmd.color ("green", "1MK5_A_S2")


cmd.select("1MK5_A_S3", "resi 54-60 & chain A & 1MK5 ")
cmd.color ("cyan", "1MK5_A_S3")


cmd.select("1MK5_A_S4", "resi 71-79 & chain A & 1MK5 ")
cmd.color ("blue", "1MK5_A_S4")


cmd.select("1MK5_A_S5", "resi 88-97 & chain A & 1MK5 ")
cmd.color ("magenta", "1MK5_A_S5")


cmd.select("1MK5_A_S6", "resi 103-111 & chain A & 1MK5 ")
cmd.color ("red", "1MK5_A_S6")


cmd.select("1MK5_A_S7", "resi 124-133 & chain A & 1MK5 ")
cmd.color ("yellow", "1MK5_A_S7")


cmd.select("1MK5_barrel", "1MK5_A_S*")
cmd.show("cartoon", "1MK5_barrel")
cmd.zoom("1MK5_barrel")
