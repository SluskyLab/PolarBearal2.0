from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HDI.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2HDI_A_S0", "resi 165-173 & chain A & 2HDI ")
cmd.color ("red", "2HDI_A_S0")


cmd.select("2HDI_A_S1", "resi 183-195 & chain A & 2HDI ")
cmd.color ("yellow", "2HDI_A_S1")


cmd.select("2HDI_A_S2", "resi 198-210 & chain A & 2HDI ")
cmd.color ("green", "2HDI_A_S2")


cmd.select("2HDI_A_S3", "resi 231-244 & chain A & 2HDI ")
cmd.color ("cyan", "2HDI_A_S3")


cmd.select("2HDI_A_S4", "resi 248-263 & chain A & 2HDI ")
cmd.color ("blue", "2HDI_A_S4")


cmd.select("2HDI_A_S5", "resi 271-284 & chain A & 2HDI ")
cmd.color ("magenta", "2HDI_A_S5")


cmd.select("2HDI_A_S6", "resi 289-302 & chain A & 2HDI ")
cmd.color ("red", "2HDI_A_S6")


cmd.select("2HDI_A_S7", "resi 310-325 & chain A & 2HDI ")
cmd.color ("yellow", "2HDI_A_S7")


cmd.select("2HDI_A_S8", "resi 330-344 & chain A & 2HDI ")
cmd.color ("green", "2HDI_A_S8")


cmd.select("2HDI_A_S9", "resi 357-372 & chain A & 2HDI ")
cmd.color ("cyan", "2HDI_A_S9")


cmd.select("2HDI_A_S10", "resi 376-388 & chain A & 2HDI ")
cmd.color ("blue", "2HDI_A_S10")


cmd.select("2HDI_A_S11", "resi 391-404 & chain A & 2HDI ")
cmd.color ("magenta", "2HDI_A_S11")


cmd.select("2HDI_A_S12", "resi 407-434 & chain A & 2HDI ")
cmd.color ("red", "2HDI_A_S12")


cmd.select("2HDI_A_S13", "resi 439-462 & chain A & 2HDI ")
cmd.color ("yellow", "2HDI_A_S13")


cmd.select("2HDI_A_S14", "resi 472-507 & chain A & 2HDI ")
cmd.color ("green", "2HDI_A_S14")


cmd.select("2HDI_A_S15", "resi 515-539 & chain A & 2HDI ")
cmd.color ("cyan", "2HDI_A_S15")


cmd.select("2HDI_A_S16", "resi 542-557 & chain A & 2HDI ")
cmd.color ("blue", "2HDI_A_S16")


cmd.select("2HDI_A_S17", "resi 570-580 & chain A & 2HDI ")
cmd.color ("magenta", "2HDI_A_S17")


cmd.select("2HDI_A_S18", "resi 588-597 & chain A & 2HDI ")
cmd.color ("red", "2HDI_A_S18")


cmd.select("2HDI_A_S19", "resi 612-621 & chain A & 2HDI ")
cmd.color ("yellow", "2HDI_A_S19")


cmd.select("2HDI_A_S20", "resi 626-635 & chain A & 2HDI ")
cmd.color ("green", "2HDI_A_S20")


cmd.select("2HDI_A_S21", "resi 654-662 & chain A & 2HDI ")
cmd.color ("cyan", "2HDI_A_S21")


cmd.select("2HDI_barrel", "2HDI_A_S*")
cmd.show("cartoon", "2HDI_barrel")
cmd.zoom("2HDI_barrel")
