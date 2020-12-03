from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Y25.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4Y25_A_S0", "resi 518-531 & chain A & 4Y25 ")
cmd.color ("red", "4Y25_A_S0")


cmd.select("4Y25_A_S1", "resi 537-548 & chain A & 4Y25 ")
cmd.color ("yellow", "4Y25_A_S1")


cmd.select("4Y25_A_S2", "resi 554-565 & chain A & 4Y25 ")
cmd.color ("green", "4Y25_A_S2")


cmd.select("4Y25_A_S3", "resi 575-585 & chain A & 4Y25 ")
cmd.color ("cyan", "4Y25_A_S3")


cmd.select("4Y25_A_S4", "resi 588-599 & chain A & 4Y25 ")
cmd.color ("blue", "4Y25_A_S4")


cmd.select("4Y25_A_S5", "resi 605-615 & chain A & 4Y25 ")
cmd.color ("magenta", "4Y25_A_S5")


cmd.select("4Y25_A_S6", "resi 619-628 & chain A & 4Y25 ")
cmd.color ("red", "4Y25_A_S6")


cmd.select("4Y25_A_S7", "resi 644-654 & chain A & 4Y25 ")
cmd.color ("yellow", "4Y25_A_S7")


cmd.select("4Y25_A_S8", "resi 659-669 & chain A & 4Y25 ")
cmd.color ("green", "4Y25_A_S8")


cmd.select("4Y25_A_S9", "resi 676-688 & chain A & 4Y25 ")
cmd.color ("cyan", "4Y25_A_S9")


cmd.select("4Y25_A_S10", "resi 694-706 & chain A & 4Y25 ")
cmd.color ("blue", "4Y25_A_S10")


cmd.select("4Y25_A_S11", "resi 717-733 & chain A & 4Y25 ")
cmd.color ("magenta", "4Y25_A_S11")


cmd.select("4Y25_A_S12", "resi 739-754 & chain A & 4Y25 ")
cmd.color ("red", "4Y25_A_S12")


cmd.select("4Y25_A_S13", "resi 757-772 & chain A & 4Y25 ")
cmd.color ("yellow", "4Y25_A_S13")


cmd.select("4Y25_A_S14", "resi 775-787 & chain A & 4Y25 ")
cmd.color ("green", "4Y25_A_S14")


cmd.select("4Y25_A_S15", "resi 794-807 & chain A & 4Y25 ")
cmd.color ("cyan", "4Y25_A_S15")


cmd.select("4Y25_barrel", "4Y25_A_S*")
cmd.show("cartoon", "4Y25_barrel")
cmd.zoom("4Y25_barrel")
