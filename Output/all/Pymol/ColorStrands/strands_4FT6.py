from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FT6.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FT6_A_S0", "resi 8-21 & chain A & 4FT6 ")
cmd.color ("red", "4FT6_A_S0")


cmd.select("4FT6_A_S1", "resi 32-48 & chain A & 4FT6 ")
cmd.color ("yellow", "4FT6_A_S1")


cmd.select("4FT6_A_S2", "resi 53-67 & chain A & 4FT6 ")
cmd.color ("green", "4FT6_A_S2")


cmd.select("4FT6_A_S3", "resi 90-100 & chain A & 4FT6 ")
cmd.color ("cyan", "4FT6_A_S3")


cmd.select("4FT6_A_S4", "resi 103-109 & chain A & 4FT6 ")
cmd.color ("blue", "4FT6_A_S4")


cmd.select("4FT6_A_S5", "resi 131-138 & chain A & 4FT6 ")
cmd.color ("magenta", "4FT6_A_S5")


cmd.select("4FT6_A_S6", "resi 142-151 & chain A & 4FT6 ")
cmd.color ("red", "4FT6_A_S6")


cmd.select("4FT6_A_S7", "resi 176-186 & chain A & 4FT6 ")
cmd.color ("yellow", "4FT6_A_S7")


cmd.select("4FT6_A_S8", "resi 190-201 & chain A & 4FT6 ")
cmd.color ("green", "4FT6_A_S8")


cmd.select("4FT6_A_S9", "resi 203-215 & chain A & 4FT6 ")
cmd.color ("cyan", "4FT6_A_S9")


cmd.select("4FT6_A_S10", "resi 221-232 & chain A & 4FT6 ")
cmd.color ("blue", "4FT6_A_S10")


cmd.select("4FT6_A_S11", "resi 243-254 & chain A & 4FT6 ")
cmd.color ("magenta", "4FT6_A_S11")


cmd.select("4FT6_A_S12", "resi 257-271 & chain A & 4FT6 ")
cmd.color ("red", "4FT6_A_S12")


cmd.select("4FT6_A_S13", "resi 295-308 & chain A & 4FT6 ")
cmd.color ("yellow", "4FT6_A_S13")


cmd.select("4FT6_A_S14", "resi 313-329 & chain A & 4FT6 ")
cmd.color ("green", "4FT6_A_S14")


cmd.select("4FT6_A_S15", "resi 337-348 & chain A & 4FT6 ")
cmd.color ("cyan", "4FT6_A_S15")


cmd.select("4FT6_A_S16", "resi 358-369 & chain A & 4FT6 ")
cmd.color ("blue", "4FT6_A_S16")


cmd.select("4FT6_A_S17", "resi 374-387 & chain A & 4FT6 ")
cmd.color ("magenta", "4FT6_A_S17")


cmd.select("4FT6_barrel", "4FT6_A_S*")
cmd.show("cartoon", "4FT6_barrel")
cmd.zoom("4FT6_barrel")
