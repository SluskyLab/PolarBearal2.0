from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3JTY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3JTY_A_S0", "resi 38-50 & chain A & 3JTY ")
cmd.color ("red", "3JTY_A_S0")


cmd.select("3JTY_A_S1", "resi 62-78 & chain A & 3JTY ")
cmd.color ("yellow", "3JTY_A_S1")


cmd.select("3JTY_A_S2", "resi 83-102 & chain A & 3JTY ")
cmd.color ("green", "3JTY_A_S2")


cmd.select("3JTY_A_S3", "resi 120-130 & chain A & 3JTY ")
cmd.color ("cyan", "3JTY_A_S3")


cmd.select("3JTY_A_S4", "resi 135-139 & chain A & 3JTY ")
cmd.color ("blue", "3JTY_A_S4")


cmd.select("3JTY_A_S5", "resi 161-167 & chain A & 3JTY ")
cmd.color ("magenta", "3JTY_A_S5")


cmd.select("3JTY_A_S6", "resi 174-181 & chain A & 3JTY ")
cmd.color ("red", "3JTY_A_S6")


cmd.select("3JTY_A_S7", "resi 206-216 & chain A & 3JTY ")
cmd.color ("yellow", "3JTY_A_S7")


cmd.select("3JTY_A_S8", "resi 220-231 & chain A & 3JTY ")
cmd.color ("green", "3JTY_A_S8")


cmd.select("3JTY_A_S9", "resi 233-245 & chain A & 3JTY ")
cmd.color ("cyan", "3JTY_A_S9")


cmd.select("3JTY_A_S10", "resi 251-262 & chain A & 3JTY ")
cmd.color ("blue", "3JTY_A_S10")


cmd.select("3JTY_A_S11", "resi 273-284 & chain A & 3JTY ")
cmd.color ("magenta", "3JTY_A_S11")


cmd.select("3JTY_A_S12", "resi 287-300 & chain A & 3JTY ")
cmd.color ("red", "3JTY_A_S12")


cmd.select("3JTY_A_S13", "resi 326-339 & chain A & 3JTY ")
cmd.color ("yellow", "3JTY_A_S13")


cmd.select("3JTY_A_S14", "resi 344-360 & chain A & 3JTY ")
cmd.color ("green", "3JTY_A_S14")


cmd.select("3JTY_A_S15", "resi 368-379 & chain A & 3JTY ")
cmd.color ("cyan", "3JTY_A_S15")


cmd.select("3JTY_A_S16", "resi 389-400 & chain A & 3JTY ")
cmd.color ("blue", "3JTY_A_S16")


cmd.select("3JTY_A_S17", "resi 406-419 & chain A & 3JTY ")
cmd.color ("magenta", "3JTY_A_S17")


cmd.select("3JTY_barrel", "3JTY_A_S*")
cmd.show("cartoon", "3JTY_barrel")
cmd.zoom("3JTY_barrel")
