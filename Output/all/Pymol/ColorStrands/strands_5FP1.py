from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP1.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5FP1_A_S0", "resi 146-154 & chain A & 5FP1 ")
cmd.color ("red", "5FP1_A_S0")


cmd.select("5FP1_A_S1", "resi 158-169 & chain A & 5FP1 ")
cmd.color ("yellow", "5FP1_A_S1")


cmd.select("5FP1_A_S2", "resi 173-184 & chain A & 5FP1 ")
cmd.color ("green", "5FP1_A_S2")


cmd.select("5FP1_A_S3", "resi 194-206 & chain A & 5FP1 ")
cmd.color ("cyan", "5FP1_A_S3")


cmd.select("5FP1_A_S4", "resi 213-226 & chain A & 5FP1 ")
cmd.color ("blue", "5FP1_A_S4")


cmd.select("5FP1_A_S5", "resi 261-277 & chain A & 5FP1 ")
cmd.color ("magenta", "5FP1_A_S5")


cmd.select("5FP1_A_S6", "resi 280-297 & chain A & 5FP1 ")
cmd.color ("red", "5FP1_A_S6")


cmd.select("5FP1_A_S7", "resi 318-337 & chain A & 5FP1 ")
cmd.color ("yellow", "5FP1_A_S7")


cmd.select("5FP1_A_S8", "resi 344-365 & chain A & 5FP1 ")
cmd.color ("green", "5FP1_A_S8")


cmd.select("5FP1_A_S9", "resi 402-426 & chain A & 5FP1 ")
cmd.color ("cyan", "5FP1_A_S9")


cmd.select("5FP1_A_S10", "resi 429-447 & chain A & 5FP1 ")
cmd.color ("blue", "5FP1_A_S10")


cmd.select("5FP1_A_S11", "resi 456-474 & chain A & 5FP1 ")
cmd.color ("magenta", "5FP1_A_S11")


cmd.select("5FP1_A_S12", "resi 480-490 & chain A & 5FP1 ")
cmd.color ("red", "5FP1_A_S12")


cmd.select("5FP1_A_S13", "resi 515-528 & chain A & 5FP1 ")
cmd.color ("yellow", "5FP1_A_S13")


cmd.select("5FP1_A_S14", "resi 532-551 & chain A & 5FP1 ")
cmd.color ("green", "5FP1_A_S14")


cmd.select("5FP1_A_S15", "resi 555-574 & chain A & 5FP1 ")
cmd.color ("cyan", "5FP1_A_S15")


cmd.select("5FP1_A_S16", "resi 579-594 & chain A & 5FP1 ")
cmd.color ("blue", "5FP1_A_S16")


cmd.select("5FP1_A_S17", "resi 620-631 & chain A & 5FP1 ")
cmd.color ("magenta", "5FP1_A_S17")


cmd.select("5FP1_A_S18", "resi 635-649 & chain A & 5FP1 ")
cmd.color ("red", "5FP1_A_S18")


cmd.select("5FP1_A_S19", "resi 655-671 & chain A & 5FP1 ")
cmd.color ("yellow", "5FP1_A_S19")


cmd.select("5FP1_A_S20", "resi 674-694 & chain A & 5FP1 ")
cmd.color ("green", "5FP1_A_S20")


cmd.select("5FP1_A_S21", "resi 698-714 & chain A & 5FP1 ")
cmd.color ("cyan", "5FP1_A_S21")


cmd.select("5FP1_barrel", "5FP1_A_S*")
cmd.show("cartoon", "5FP1_barrel")
cmd.zoom("5FP1_barrel")
