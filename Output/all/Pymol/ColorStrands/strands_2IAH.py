from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2IAH.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2IAH_A_S0", "resi 278-286 & chain A & 2IAH ")
cmd.color ("red", "2IAH_A_S0")


cmd.select("2IAH_A_S1", "resi 288-299 & chain A & 2IAH ")
cmd.color ("yellow", "2IAH_A_S1")


cmd.select("2IAH_A_S2", "resi 307-319 & chain A & 2IAH ")
cmd.color ("green", "2IAH_A_S2")


cmd.select("2IAH_A_S3", "resi 326-340 & chain A & 2IAH ")
cmd.color ("cyan", "2IAH_A_S3")


cmd.select("2IAH_A_S4", "resi 344-358 & chain A & 2IAH ")
cmd.color ("blue", "2IAH_A_S4")


cmd.select("2IAH_A_S5", "resi 390-404 & chain A & 2IAH ")
cmd.color ("magenta", "2IAH_A_S5")


cmd.select("2IAH_A_S6", "resi 411-429 & chain A & 2IAH ")
cmd.color ("red", "2IAH_A_S6")


cmd.select("2IAH_A_S7", "resi 441-465 & chain A & 2IAH ")
cmd.color ("yellow", "2IAH_A_S7")


cmd.select("2IAH_A_S8", "resi 472-498 & chain A & 2IAH ")
cmd.color ("green", "2IAH_A_S8")


cmd.select("2IAH_A_S9", "resi 519-537 & chain A & 2IAH ")
cmd.color ("cyan", "2IAH_A_S9")


cmd.select("2IAH_A_S10", "resi 542-557 & chain A & 2IAH ")
cmd.color ("blue", "2IAH_A_S10")


cmd.select("2IAH_A_S11", "resi 563-578 & chain A & 2IAH ")
cmd.color ("magenta", "2IAH_A_S11")


cmd.select("2IAH_A_S12", "resi 582-594 & chain A & 2IAH ")
cmd.color ("red", "2IAH_A_S12")


cmd.select("2IAH_A_S13", "resi 611-624 & chain A & 2IAH ")
cmd.color ("yellow", "2IAH_A_S13")


cmd.select("2IAH_A_S14", "resi 628-645 & chain A & 2IAH ")
cmd.color ("green", "2IAH_A_S14")


cmd.select("2IAH_A_S15", "resi 664-681 & chain A & 2IAH ")
cmd.color ("cyan", "2IAH_A_S15")


cmd.select("2IAH_A_S16", "resi 685-698 & chain A & 2IAH ")
cmd.color ("blue", "2IAH_A_S16")


cmd.select("2IAH_A_S17", "resi 702-721 & chain A & 2IAH ")
cmd.color ("magenta", "2IAH_A_S17")


cmd.select("2IAH_A_S18", "resi 728-746 & chain A & 2IAH ")
cmd.color ("red", "2IAH_A_S18")


cmd.select("2IAH_A_S19", "resi 751-769 & chain A & 2IAH ")
cmd.color ("yellow", "2IAH_A_S19")


cmd.select("2IAH_A_S20", "resi 776-792 & chain A & 2IAH ")
cmd.color ("green", "2IAH_A_S20")


cmd.select("2IAH_A_S21", "resi 800-812 & chain A & 2IAH ")
cmd.color ("cyan", "2IAH_A_S21")


cmd.select("2IAH_barrel", "2IAH_A_S*")
cmd.show("cartoon", "2IAH_barrel")
cmd.zoom("2IAH_barrel")
