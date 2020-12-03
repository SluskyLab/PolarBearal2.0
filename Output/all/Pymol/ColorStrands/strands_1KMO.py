from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1KMO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1KMO_A_S0", "resi 224-232 & chain A & 1KMO ")
cmd.color ("red", "1KMO_A_S0")


cmd.select("1KMO_A_S1", "resi 242-252 & chain A & 1KMO ")
cmd.color ("yellow", "1KMO_A_S1")


cmd.select("1KMO_A_S2", "resi 257-270 & chain A & 1KMO ")
cmd.color ("green", "1KMO_A_S2")


cmd.select("1KMO_A_S3", "resi 278-290 & chain A & 1KMO ")
cmd.color ("cyan", "1KMO_A_S3")


cmd.select("1KMO_A_S4", "resi 294-310 & chain A & 1KMO ")
cmd.color ("blue", "1KMO_A_S4")


cmd.select("1KMO_A_S5", "resi 331-347 & chain A & 1KMO ")
cmd.color ("magenta", "1KMO_A_S5")


cmd.select("1KMO_A_S6", "resi 351-369 & chain A & 1KMO ")
cmd.color ("red", "1KMO_A_S6")


cmd.select("1KMO_A_S7", "resi 375-395 & chain A & 1KMO ")
cmd.color ("yellow", "1KMO_A_S7")


cmd.select("1KMO_A_S8", "resi 402-422 & chain A & 1KMO ")
cmd.color ("green", "1KMO_A_S8")


cmd.select("1KMO_A_S9", "resi 435-455 & chain A & 1KMO ")
cmd.color ("cyan", "1KMO_A_S9")


cmd.select("1KMO_A_S10", "resi 461-478 & chain A & 1KMO ")
cmd.color ("blue", "1KMO_A_S10")


cmd.select("1KMO_A_S11", "resi 481-501 & chain A & 1KMO ")
cmd.color ("magenta", "1KMO_A_S11")


cmd.select("1KMO_A_S12", "resi 504-516 & chain A & 1KMO ")
cmd.color ("red", "1KMO_A_S12")


cmd.select("1KMO_A_S13", "resi 535-547 & chain A & 1KMO ")
cmd.color ("yellow", "1KMO_A_S13")


cmd.select("1KMO_A_S14", "resi 552-563 & chain A & 1KMO ")
cmd.color ("green", "1KMO_A_S14")


cmd.select("1KMO_A_S15", "resi 580-594 & chain A & 1KMO ")
cmd.color ("cyan", "1KMO_A_S15")


cmd.select("1KMO_A_S16", "resi 603-618 & chain A & 1KMO ")
cmd.color ("blue", "1KMO_A_S16")


cmd.select("1KMO_A_S17", "resi 633-643 & chain A & 1KMO ")
cmd.color ("magenta", "1KMO_A_S17")


cmd.select("1KMO_A_S18", "resi 646-659 & chain A & 1KMO ")
cmd.color ("red", "1KMO_A_S18")


cmd.select("1KMO_A_S19", "resi 678-691 & chain A & 1KMO ")
cmd.color ("yellow", "1KMO_A_S19")


cmd.select("1KMO_A_S20", "resi 697-717 & chain A & 1KMO ")
cmd.color ("green", "1KMO_A_S20")


cmd.select("1KMO_A_S21", "resi 724-740 & chain A & 1KMO ")
cmd.color ("cyan", "1KMO_A_S21")


cmd.select("1KMO_barrel", "1KMO_A_S*")
cmd.show("cartoon", "1KMO_barrel")
cmd.zoom("1KMO_barrel")
