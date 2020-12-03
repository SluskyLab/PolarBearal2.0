from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5M9B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5M9B_A_S0", "resi 156-164 & chain A & 5M9B ")
cmd.color ("red", "5M9B_A_S0")


cmd.select("5M9B_A_S1", "resi 174-183 & chain A & 5M9B ")
cmd.color ("yellow", "5M9B_A_S1")


cmd.select("5M9B_A_S2", "resi 189-200 & chain A & 5M9B ")
cmd.color ("green", "5M9B_A_S2")


cmd.select("5M9B_A_S3", "resi 229-243 & chain A & 5M9B ")
cmd.color ("cyan", "5M9B_A_S3")


cmd.select("5M9B_A_S4", "resi 246-262 & chain A & 5M9B ")
cmd.color ("blue", "5M9B_A_S4")


cmd.select("5M9B_A_S5", "resi 284-298 & chain A & 5M9B ")
cmd.color ("magenta", "5M9B_A_S5")


cmd.select("5M9B_A_S6", "resi 303-317 & chain A & 5M9B ")
cmd.color ("red", "5M9B_A_S6")


cmd.select("5M9B_A_S7", "resi 338-355 & chain A & 5M9B ")
cmd.color ("yellow", "5M9B_A_S7")


cmd.select("5M9B_A_S8", "resi 361-376 & chain A & 5M9B ")
cmd.color ("green", "5M9B_A_S8")


cmd.select("5M9B_A_S9", "resi 400-417 & chain A & 5M9B ")
cmd.color ("cyan", "5M9B_A_S9")


cmd.select("5M9B_A_S10", "resi 421-433 & chain A & 5M9B ")
cmd.color ("blue", "5M9B_A_S10")


cmd.select("5M9B_A_S11", "resi 438-449 & chain A & 5M9B ")
cmd.color ("magenta", "5M9B_A_S11")


cmd.select("5M9B_A_S12", "resi 452-479 & chain A & 5M9B ")
cmd.color ("red", "5M9B_A_S12")


cmd.select("5M9B_A_S13", "resi 491-514 & chain A & 5M9B ")
cmd.color ("yellow", "5M9B_A_S13")


cmd.select("5M9B_A_S14", "resi 519-536 & chain A & 5M9B ")
cmd.color ("green", "5M9B_A_S14")


cmd.select("5M9B_A_S15", "resi 557-577 & chain A & 5M9B ")
cmd.color ("cyan", "5M9B_A_S15")


cmd.select("5M9B_A_S16", "resi 581-595 & chain A & 5M9B ")
cmd.color ("blue", "5M9B_A_S16")


cmd.select("5M9B_A_S17", "resi 600-618 & chain A & 5M9B ")
cmd.color ("magenta", "5M9B_A_S17")


cmd.select("5M9B_A_S18", "resi 622-634 & chain A & 5M9B ")
cmd.color ("red", "5M9B_A_S18")


cmd.select("5M9B_A_S19", "resi 654-668 & chain A & 5M9B ")
cmd.color ("yellow", "5M9B_A_S19")


cmd.select("5M9B_A_S20", "resi 671-686 & chain A & 5M9B ")
cmd.color ("green", "5M9B_A_S20")


cmd.select("5M9B_A_S21", "resi 708-720 & chain A & 5M9B ")
cmd.color ("cyan", "5M9B_A_S21")


cmd.select("5M9B_barrel", "5M9B_A_S*")
cmd.show("cartoon", "5M9B_barrel")
cmd.zoom("5M9B_barrel")
