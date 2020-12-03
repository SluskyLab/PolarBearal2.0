from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AF6.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1AF6_A_S0", "resi 2-15 & chain A & 1AF6 ")
cmd.color ("red", "1AF6_A_S0")


cmd.select("1AF6_A_S1", "resi 41-50 & chain A & 1AF6 ")
cmd.color ("yellow", "1AF6_A_S1")


cmd.select("1AF6_A_S2", "resi 57-68 & chain A & 1AF6 ")
cmd.color ("green", "1AF6_A_S2")


cmd.select("1AF6_A_S3", "resi 80-89 & chain A & 1AF6 ")
cmd.color ("cyan", "1AF6_A_S3")


cmd.select("1AF6_A_S4", "resi 99-104 & chain A & 1AF6 ")
cmd.color ("blue", "1AF6_A_S4")


cmd.select("1AF6_A_S5", "resi 119-132 & chain A & 1AF6 ")
cmd.color ("magenta", "1AF6_A_S5")


cmd.select("1AF6_A_S6", "resi 138-152 & chain A & 1AF6 ")
cmd.color ("red", "1AF6_A_S6")


cmd.select("1AF6_A_S7", "resi 165-179 & chain A & 1AF6 ")
cmd.color ("yellow", "1AF6_A_S7")


cmd.select("1AF6_A_S8", "resi 185-197 & chain A & 1AF6 ")
cmd.color ("green", "1AF6_A_S8")


cmd.select("1AF6_A_S9", "resi 211-221 & chain A & 1AF6 ")
cmd.color ("cyan", "1AF6_A_S9")


cmd.select("1AF6_A_S10", "resi 224-238 & chain A & 1AF6 ")
cmd.color ("blue", "1AF6_A_S10")


cmd.select("1AF6_A_S11", "resi 268-279 & chain A & 1AF6 ")
cmd.color ("magenta", "1AF6_A_S11")


cmd.select("1AF6_A_S12", "resi 284-296 & chain A & 1AF6 ")
cmd.color ("red", "1AF6_A_S12")


cmd.select("1AF6_A_S13", "resi 303-316 & chain A & 1AF6 ")
cmd.color ("yellow", "1AF6_A_S13")


cmd.select("1AF6_A_S14", "resi 319-332 & chain A & 1AF6 ")
cmd.color ("green", "1AF6_A_S14")


cmd.select("1AF6_A_S15", "resi 339-352 & chain A & 1AF6 ")
cmd.color ("cyan", "1AF6_A_S15")


cmd.select("1AF6_A_S16", "resi 362-375 & chain A & 1AF6 ")
cmd.color ("blue", "1AF6_A_S16")


cmd.select("1AF6_A_S17", "resi 406-421 & chain A & 1AF6 ")
cmd.color ("magenta", "1AF6_A_S17")


cmd.select("1AF6_barrel", "1AF6_A_S*")
cmd.show("cartoon", "1AF6_barrel")
cmd.zoom("1AF6_barrel")
