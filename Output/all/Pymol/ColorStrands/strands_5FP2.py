from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP2.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5FP2_A_S0", "resi 163-171 & chain A & 5FP2 ")
cmd.color ("red", "5FP2_A_S0")


cmd.select("5FP2_A_S1", "resi 181-190 & chain A & 5FP2 ")
cmd.color ("yellow", "5FP2_A_S1")


cmd.select("5FP2_A_S2", "resi 196-207 & chain A & 5FP2 ")
cmd.color ("green", "5FP2_A_S2")


cmd.select("5FP2_A_S3", "resi 232-245 & chain A & 5FP2 ")
cmd.color ("cyan", "5FP2_A_S3")


cmd.select("5FP2_A_S4", "resi 248-261 & chain A & 5FP2 ")
cmd.color ("blue", "5FP2_A_S4")


cmd.select("5FP2_A_S5", "resi 289-302 & chain A & 5FP2 ")
cmd.color ("magenta", "5FP2_A_S5")


cmd.select("5FP2_A_S6", "resi 307-320 & chain A & 5FP2 ")
cmd.color ("red", "5FP2_A_S6")


cmd.select("5FP2_A_S7", "resi 343-358 & chain A & 5FP2 ")
cmd.color ("yellow", "5FP2_A_S7")


cmd.select("5FP2_A_S8", "resi 364-379 & chain A & 5FP2 ")
cmd.color ("green", "5FP2_A_S8")


cmd.select("5FP2_A_S9", "resi 404-421 & chain A & 5FP2 ")
cmd.color ("cyan", "5FP2_A_S9")


cmd.select("5FP2_A_S10", "resi 425-437 & chain A & 5FP2 ")
cmd.color ("blue", "5FP2_A_S10")


cmd.select("5FP2_A_S11", "resi 440-453 & chain A & 5FP2 ")
cmd.color ("magenta", "5FP2_A_S11")


cmd.select("5FP2_A_S12", "resi 456-468 & chain A & 5FP2 ")
cmd.color ("red", "5FP2_A_S12")


cmd.select("5FP2_A_S13", "resi 508-520 & chain A & 5FP2 ")
cmd.color ("yellow", "5FP2_A_S13")


cmd.select("5FP2_A_S14", "resi 525-536 & chain A & 5FP2 ")
cmd.color ("green", "5FP2_A_S14")


cmd.select("5FP2_A_S15", "resi 564-577 & chain A & 5FP2 ")
cmd.color ("cyan", "5FP2_A_S15")


cmd.select("5FP2_A_S16", "resi 581-593 & chain A & 5FP2 ")
cmd.color ("blue", "5FP2_A_S16")


cmd.select("5FP2_A_S17", "resi 607-618 & chain A & 5FP2 ")
cmd.color ("magenta", "5FP2_A_S17")


cmd.select("5FP2_A_S18", "resi 621-632 & chain A & 5FP2 ")
cmd.color ("red", "5FP2_A_S18")


cmd.select("5FP2_A_S19", "resi 656-667 & chain A & 5FP2 ")
cmd.color ("yellow", "5FP2_A_S19")


cmd.select("5FP2_A_S20", "resi 670-678 & chain A & 5FP2 ")
cmd.color ("green", "5FP2_A_S20")


cmd.select("5FP2_A_S21", "resi 705-713 & chain A & 5FP2 ")
cmd.color ("cyan", "5FP2_A_S21")


cmd.select("5FP2_barrel", "5FP2_A_S*")
cmd.show("cartoon", "5FP2_barrel")
cmd.zoom("5FP2_barrel")
