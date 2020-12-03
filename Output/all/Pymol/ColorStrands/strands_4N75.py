from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4N75.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4N75_A_S0", "resi 427-434 & chain A & 4N75 ")
cmd.color ("red", "4N75_A_S0")


cmd.select("4N75_A_S1", "resi 437-449 & chain A & 4N75 ")
cmd.color ("yellow", "4N75_A_S1")


cmd.select("4N75_A_S2", "resi 454-462 & chain A & 4N75 ")
cmd.color ("green", "4N75_A_S2")


cmd.select("4N75_A_S3", "resi 465-479 & chain A & 4N75 ")
cmd.color ("cyan", "4N75_A_S3")


cmd.select("4N75_A_S4", "resi 483-495 & chain A & 4N75 ")
cmd.color ("blue", "4N75_A_S4")


cmd.select("4N75_A_S5", "resi 504-517 & chain A & 4N75 ")
cmd.color ("magenta", "4N75_A_S5")


cmd.select("4N75_A_S6", "resi 522-537 & chain A & 4N75 ")
cmd.color ("red", "4N75_A_S6")


cmd.select("4N75_A_S7", "resi 565-582 & chain A & 4N75 ")
cmd.color ("yellow", "4N75_A_S7")


cmd.select("4N75_A_S8", "resi 589-605 & chain A & 4N75 ")
cmd.color ("green", "4N75_A_S8")


cmd.select("4N75_A_S9", "resi 607-621 & chain A & 4N75 ")
cmd.color ("cyan", "4N75_A_S9")


cmd.select("4N75_A_S10", "resi 627-639 & chain A & 4N75 ")
cmd.color ("blue", "4N75_A_S10")


cmd.select("4N75_A_S11", "resi 709-720 & chain A & 4N75 ")
cmd.color ("magenta", "4N75_A_S11")


cmd.select("4N75_A_S12", "resi 734-745 & chain A & 4N75 ")
cmd.color ("red", "4N75_A_S12")


cmd.select("4N75_A_S13", "resi 767-776 & chain A & 4N75 ")
cmd.color ("yellow", "4N75_A_S13")


cmd.select("4N75_A_S14", "resi 782-792 & chain A & 4N75 ")
cmd.color ("green", "4N75_A_S14")


cmd.select("4N75_A_S15", "resi 801-810 & chain A & 4N75 ")
cmd.color ("cyan", "4N75_A_S15")


cmd.select("4N75_barrel", "4N75_A_S*")
cmd.show("cartoon", "4N75_barrel")
cmd.zoom("4N75_barrel")
