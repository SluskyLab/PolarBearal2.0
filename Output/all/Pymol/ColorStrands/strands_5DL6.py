from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL6.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5DL6_A_S0", "resi 8-21 & chain A & 5DL6 ")
cmd.color ("red", "5DL6_A_S0")


cmd.select("5DL6_A_S1", "resi 31-47 & chain A & 5DL6 ")
cmd.color ("yellow", "5DL6_A_S1")


cmd.select("5DL6_A_S2", "resi 52-71 & chain A & 5DL6 ")
cmd.color ("green", "5DL6_A_S2")


cmd.select("5DL6_A_S3", "resi 90-100 & chain A & 5DL6 ")
cmd.color ("cyan", "5DL6_A_S3")


cmd.select("5DL6_A_S4", "resi 105-109 & chain A & 5DL6 ")
cmd.color ("blue", "5DL6_A_S4")


cmd.select("5DL6_A_S5", "resi 131-137 & chain A & 5DL6 ")
cmd.color ("magenta", "5DL6_A_S5")


cmd.select("5DL6_A_S6", "resi 144-151 & chain A & 5DL6 ")
cmd.color ("red", "5DL6_A_S6")


cmd.select("5DL6_A_S7", "resi 180-190 & chain A & 5DL6 ")
cmd.color ("yellow", "5DL6_A_S7")


cmd.select("5DL6_A_S8", "resi 193-204 & chain A & 5DL6 ")
cmd.color ("green", "5DL6_A_S8")


cmd.select("5DL6_A_S9", "resi 207-220 & chain A & 5DL6 ")
cmd.color ("cyan", "5DL6_A_S9")


cmd.select("5DL6_A_S10", "resi 224-236 & chain A & 5DL6 ")
cmd.color ("blue", "5DL6_A_S10")


cmd.select("5DL6_A_S11", "resi 247-258 & chain A & 5DL6 ")
cmd.color ("magenta", "5DL6_A_S11")


cmd.select("5DL6_A_S12", "resi 263-275 & chain A & 5DL6 ")
cmd.color ("red", "5DL6_A_S12")


cmd.select("5DL6_A_S13", "resi 299-312 & chain A & 5DL6 ")
cmd.color ("yellow", "5DL6_A_S13")


cmd.select("5DL6_A_S14", "resi 316-332 & chain A & 5DL6 ")
cmd.color ("green", "5DL6_A_S14")


cmd.select("5DL6_A_S15", "resi 343-354 & chain A & 5DL6 ")
cmd.color ("cyan", "5DL6_A_S15")


cmd.select("5DL6_A_S16", "resi 362-372 & chain A & 5DL6 ")
cmd.color ("blue", "5DL6_A_S16")


cmd.select("5DL6_A_S17", "resi 384-398 & chain A & 5DL6 ")
cmd.color ("magenta", "5DL6_A_S17")


cmd.select("5DL6_barrel", "5DL6_A_S*")
cmd.show("cartoon", "5DL6_barrel")
cmd.zoom("5DL6_barrel")
