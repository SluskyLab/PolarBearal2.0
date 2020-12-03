from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6V81.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6V81_A_S0", "resi 164-172 & chain A & 6V81 ")
cmd.color ("red", "6V81_A_S0")


cmd.select("6V81_A_S1", "resi 176-187 & chain A & 6V81 ")
cmd.color ("yellow", "6V81_A_S1")


cmd.select("6V81_A_S2", "resi 196-207 & chain A & 6V81 ")
cmd.color ("green", "6V81_A_S2")


cmd.select("6V81_A_S3", "resi 216-227 & chain A & 6V81 ")
cmd.color ("cyan", "6V81_A_S3")


cmd.select("6V81_A_S4", "resi 234-245 & chain A & 6V81 ")
cmd.color ("blue", "6V81_A_S4")


cmd.select("6V81_A_S5", "resi 273-287 & chain A & 6V81 ")
cmd.color ("magenta", "6V81_A_S5")


cmd.select("6V81_A_S6", "resi 294-309 & chain A & 6V81 ")
cmd.color ("red", "6V81_A_S6")


cmd.select("6V81_A_S7", "resi 325-342 & chain A & 6V81 ")
cmd.color ("yellow", "6V81_A_S7")


cmd.select("6V81_A_S8", "resi 351-369 & chain A & 6V81 ")
cmd.color ("green", "6V81_A_S8")


cmd.select("6V81_A_S9", "resi 387-405 & chain A & 6V81 ")
cmd.color ("cyan", "6V81_A_S9")


cmd.select("6V81_A_S10", "resi 412-429 & chain A & 6V81 ")
cmd.color ("blue", "6V81_A_S10")


cmd.select("6V81_A_S11", "resi 440-457 & chain A & 6V81 ")
cmd.color ("magenta", "6V81_A_S11")


cmd.select("6V81_A_S12", "resi 461-472 & chain A & 6V81 ")
cmd.color ("red", "6V81_A_S12")


cmd.select("6V81_A_S13", "resi 496-507 & chain A & 6V81 ")
cmd.color ("yellow", "6V81_A_S13")


cmd.select("6V81_A_S14", "resi 513-531 & chain A & 6V81 ")
cmd.color ("green", "6V81_A_S14")


cmd.select("6V81_A_S15", "resi 538-558 & chain A & 6V81 ")
cmd.color ("cyan", "6V81_A_S15")


cmd.select("6V81_A_S16", "resi 561-576 & chain A & 6V81 ")
cmd.color ("blue", "6V81_A_S16")


cmd.select("6V81_A_S17", "resi 595-605 & chain A & 6V81 ")
cmd.color ("magenta", "6V81_A_S17")


cmd.select("6V81_A_S18", "resi 611-624 & chain A & 6V81 ")
cmd.color ("red", "6V81_A_S18")


cmd.select("6V81_A_S19", "resi 630-646 & chain A & 6V81 ")
cmd.color ("yellow", "6V81_A_S19")


cmd.select("6V81_A_S20", "resi 652-667 & chain A & 6V81 ")
cmd.color ("green", "6V81_A_S20")


cmd.select("6V81_A_S21", "resi 682-696 & chain A & 6V81 ")
cmd.color ("cyan", "6V81_A_S21")


cmd.select("6V81_barrel", "6V81_A_S*")
cmd.show("cartoon", "6V81_barrel")
cmd.zoom("6V81_barrel")
