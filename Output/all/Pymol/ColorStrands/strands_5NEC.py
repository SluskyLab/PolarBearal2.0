from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NEC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5NEC_A_S0", "resi 157-165 & chain A & 5NEC ")
cmd.color ("red", "5NEC_A_S0")


cmd.select("5NEC_A_S1", "resi 169-180 & chain A & 5NEC ")
cmd.color ("yellow", "5NEC_A_S1")


cmd.select("5NEC_A_S2", "resi 185-196 & chain A & 5NEC ")
cmd.color ("green", "5NEC_A_S2")


cmd.select("5NEC_A_S3", "resi 205-217 & chain A & 5NEC ")
cmd.color ("cyan", "5NEC_A_S3")


cmd.select("5NEC_A_S4", "resi 224-237 & chain A & 5NEC ")
cmd.color ("blue", "5NEC_A_S4")


cmd.select("5NEC_A_S5", "resi 274-290 & chain A & 5NEC ")
cmd.color ("magenta", "5NEC_A_S5")


cmd.select("5NEC_A_S6", "resi 293-313 & chain A & 5NEC ")
cmd.color ("red", "5NEC_A_S6")


cmd.select("5NEC_A_S7", "resi 329-350 & chain A & 5NEC ")
cmd.color ("yellow", "5NEC_A_S7")


cmd.select("5NEC_A_S8", "resi 357-376 & chain A & 5NEC ")
cmd.color ("green", "5NEC_A_S8")


cmd.select("5NEC_A_S9", "resi 420-441 & chain A & 5NEC ")
cmd.color ("cyan", "5NEC_A_S9")


cmd.select("5NEC_A_S10", "resi 444-462 & chain A & 5NEC ")
cmd.color ("blue", "5NEC_A_S10")


cmd.select("5NEC_A_S11", "resi 469-487 & chain A & 5NEC ")
cmd.color ("magenta", "5NEC_A_S11")


cmd.select("5NEC_A_S12", "resi 491-502 & chain A & 5NEC ")
cmd.color ("red", "5NEC_A_S12")


cmd.select("5NEC_A_S13", "resi 531-543 & chain A & 5NEC ")
cmd.color ("yellow", "5NEC_A_S13")


cmd.select("5NEC_A_S14", "resi 547-560 & chain A & 5NEC ")
cmd.color ("green", "5NEC_A_S14")


cmd.select("5NEC_A_S15", "resi 576-590 & chain A & 5NEC ")
cmd.color ("cyan", "5NEC_A_S15")


cmd.select("5NEC_A_S16", "resi 594-608 & chain A & 5NEC ")
cmd.color ("blue", "5NEC_A_S16")


cmd.select("5NEC_A_S17", "resi 636-645 & chain A & 5NEC ")
cmd.color ("magenta", "5NEC_A_S17")


cmd.select("5NEC_A_S18", "resi 652-665 & chain A & 5NEC ")
cmd.color ("red", "5NEC_A_S18")


cmd.select("5NEC_A_S19", "resi 671-687 & chain A & 5NEC ")
cmd.color ("yellow", "5NEC_A_S19")


cmd.select("5NEC_A_S20", "resi 690-710 & chain A & 5NEC ")
cmd.color ("green", "5NEC_A_S20")


cmd.select("5NEC_A_S21", "resi 714-730 & chain A & 5NEC ")
cmd.color ("cyan", "5NEC_A_S21")


cmd.select("5NEC_barrel", "5NEC_A_S*")
cmd.show("cartoon", "5NEC_barrel")
cmd.zoom("5NEC_barrel")
