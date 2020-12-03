from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EUS.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6EUS_A_S0", "resi 70-86 & chain A & 6EUS ")
cmd.color ("red", "6EUS_A_S0")


cmd.select("6EUS_A_S1", "resi 102-120 & chain A & 6EUS ")
cmd.color ("yellow", "6EUS_A_S1")


cmd.select("6EUS_A_S2", "resi 127-138 & chain A & 6EUS ")
cmd.color ("green", "6EUS_A_S2")


cmd.select("6EUS_A_S3", "resi 146-157 & chain A & 6EUS ")
cmd.color ("cyan", "6EUS_A_S3")


cmd.select("6EUS_A_S4", "resi 158-163 & chain A & 6EUS ")
cmd.color ("blue", "6EUS_A_S4")


cmd.select("6EUS_A_S5", "resi 190-199 & chain A & 6EUS ")
cmd.color ("magenta", "6EUS_A_S5")


cmd.select("6EUS_A_S6", "resi 203-210 & chain A & 6EUS ")
cmd.color ("red", "6EUS_A_S6")


cmd.select("6EUS_A_S7", "resi 222-238 & chain A & 6EUS ")
cmd.color ("yellow", "6EUS_A_S7")


cmd.select("6EUS_A_S8", "resi 243-257 & chain A & 6EUS ")
cmd.color ("green", "6EUS_A_S8")


cmd.select("6EUS_A_S9", "resi 261-276 & chain A & 6EUS ")
cmd.color ("cyan", "6EUS_A_S9")


cmd.select("6EUS_A_S10", "resi 280-290 & chain A & 6EUS ")
cmd.color ("blue", "6EUS_A_S10")


cmd.select("6EUS_A_S11", "resi 314-326 & chain A & 6EUS ")
cmd.color ("magenta", "6EUS_A_S11")


cmd.select("6EUS_A_S12", "resi 329-342 & chain A & 6EUS ")
cmd.color ("red", "6EUS_A_S12")


cmd.select("6EUS_A_S13", "resi 356-368 & chain A & 6EUS ")
cmd.color ("yellow", "6EUS_A_S13")


cmd.select("6EUS_A_S14", "resi 372-385 & chain A & 6EUS ")
cmd.color ("green", "6EUS_A_S14")


cmd.select("6EUS_A_S15", "resi 392-404 & chain A & 6EUS ")
cmd.color ("cyan", "6EUS_A_S15")


cmd.select("6EUS_barrel", "6EUS_A_S*")
cmd.show("cartoon", "6EUS_barrel")
cmd.zoom("6EUS_barrel")
