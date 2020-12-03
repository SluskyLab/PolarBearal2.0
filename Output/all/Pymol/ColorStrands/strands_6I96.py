from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6I96_A_S0", "resi 291-299 & chain A & 6I96 ")
cmd.color ("red", "6I96_A_S0")


cmd.select("6I96_A_S1", "resi 303-314 & chain A & 6I96 ")
cmd.color ("yellow", "6I96_A_S1")


cmd.select("6I96_A_S2", "resi 320-331 & chain A & 6I96 ")
cmd.color ("green", "6I96_A_S2")


cmd.select("6I96_A_S3", "resi 339-353 & chain A & 6I96 ")
cmd.color ("cyan", "6I96_A_S3")


cmd.select("6I96_A_S4", "resi 357-370 & chain A & 6I96 ")
cmd.color ("blue", "6I96_A_S4")


cmd.select("6I96_A_S5", "resi 404-418 & chain A & 6I96 ")
cmd.color ("magenta", "6I96_A_S5")


cmd.select("6I96_A_S6", "resi 423-448 & chain A & 6I96 ")
cmd.color ("red", "6I96_A_S6")


cmd.select("6I96_A_S7", "resi 454-479 & chain A & 6I96 ")
cmd.color ("yellow", "6I96_A_S7")


cmd.select("6I96_A_S8", "resi 485-506 & chain A & 6I96 ")
cmd.color ("green", "6I96_A_S8")


cmd.select("6I96_A_S9", "resi 526-547 & chain A & 6I96 ")
cmd.color ("cyan", "6I96_A_S9")


cmd.select("6I96_A_S10", "resi 550-569 & chain A & 6I96 ")
cmd.color ("blue", "6I96_A_S10")


cmd.select("6I96_A_S11", "resi 575-591 & chain A & 6I96 ")
cmd.color ("magenta", "6I96_A_S11")


cmd.select("6I96_A_S12", "resi 595-611 & chain A & 6I96 ")
cmd.color ("red", "6I96_A_S12")


cmd.select("6I96_A_S13", "resi 619-634 & chain A & 6I96 ")
cmd.color ("yellow", "6I96_A_S13")


cmd.select("6I96_A_S14", "resi 641-656 & chain A & 6I96 ")
cmd.color ("green", "6I96_A_S14")


cmd.select("6I96_A_S15", "resi 665-683 & chain A & 6I96 ")
cmd.color ("cyan", "6I96_A_S15")


cmd.select("6I96_A_S16", "resi 686-702 & chain A & 6I96 ")
cmd.color ("blue", "6I96_A_S16")


cmd.select("6I96_A_S17", "resi 717-727 & chain A & 6I96 ")
cmd.color ("magenta", "6I96_A_S17")


cmd.select("6I96_A_S18", "resi 737-750 & chain A & 6I96 ")
cmd.color ("red", "6I96_A_S18")


cmd.select("6I96_A_S19", "resi 756-772 & chain A & 6I96 ")
cmd.color ("yellow", "6I96_A_S19")


cmd.select("6I96_A_S20", "resi 777-799 & chain A & 6I96 ")
cmd.color ("green", "6I96_A_S20")


cmd.select("6I96_A_S21", "resi 803-817 & chain A & 6I96 ")
cmd.color ("cyan", "6I96_A_S21")


cmd.select("6I96_barrel", "6I96_A_S*")
cmd.show("cartoon", "6I96_barrel")
cmd.zoom("6I96_barrel")
