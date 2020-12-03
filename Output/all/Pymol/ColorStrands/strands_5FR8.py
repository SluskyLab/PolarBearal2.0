from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FR8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5FR8_A_S0", "resi 164-172 & chain A & 5FR8 ")
cmd.color ("red", "5FR8_A_S0")


cmd.select("5FR8_A_S1", "resi 182-194 & chain A & 5FR8 ")
cmd.color ("yellow", "5FR8_A_S1")


cmd.select("5FR8_A_S2", "resi 198-209 & chain A & 5FR8 ")
cmd.color ("green", "5FR8_A_S2")


cmd.select("5FR8_A_S3", "resi 229-243 & chain A & 5FR8 ")
cmd.color ("cyan", "5FR8_A_S3")


cmd.select("5FR8_A_S4", "resi 246-262 & chain A & 5FR8 ")
cmd.color ("blue", "5FR8_A_S4")


cmd.select("5FR8_A_S5", "resi 287-301 & chain A & 5FR8 ")
cmd.color ("magenta", "5FR8_A_S5")


cmd.select("5FR8_A_S6", "resi 306-320 & chain A & 5FR8 ")
cmd.color ("red", "5FR8_A_S6")


cmd.select("5FR8_A_S7", "resi 340-357 & chain A & 5FR8 ")
cmd.color ("yellow", "5FR8_A_S7")


cmd.select("5FR8_A_S8", "resi 363-378 & chain A & 5FR8 ")
cmd.color ("green", "5FR8_A_S8")


cmd.select("5FR8_A_S9", "resi 403-420 & chain A & 5FR8 ")
cmd.color ("cyan", "5FR8_A_S9")


cmd.select("5FR8_A_S10", "resi 424-436 & chain A & 5FR8 ")
cmd.color ("blue", "5FR8_A_S10")


cmd.select("5FR8_A_S11", "resi 439-452 & chain A & 5FR8 ")
cmd.color ("magenta", "5FR8_A_S11")


cmd.select("5FR8_A_S12", "resi 455-482 & chain A & 5FR8 ")
cmd.color ("red", "5FR8_A_S12")


cmd.select("5FR8_A_S13", "resi 495-518 & chain A & 5FR8 ")
cmd.color ("yellow", "5FR8_A_S13")


cmd.select("5FR8_A_S14", "resi 521-536 & chain A & 5FR8 ")
cmd.color ("green", "5FR8_A_S14")


cmd.select("5FR8_A_S15", "resi 572-587 & chain A & 5FR8 ")
cmd.color ("cyan", "5FR8_A_S15")


cmd.select("5FR8_A_S16", "resi 592-606 & chain A & 5FR8 ")
cmd.color ("blue", "5FR8_A_S16")


cmd.select("5FR8_A_S17", "resi 617-626 & chain A & 5FR8 ")
cmd.color ("magenta", "5FR8_A_S17")


cmd.select("5FR8_A_S18", "resi 633-642 & chain A & 5FR8 ")
cmd.color ("red", "5FR8_A_S18")


cmd.select("5FR8_A_S19", "resi 675-684 & chain A & 5FR8 ")
cmd.color ("yellow", "5FR8_A_S19")


cmd.select("5FR8_A_S20", "resi 689-707 & chain A & 5FR8 ")
cmd.color ("green", "5FR8_A_S20")


cmd.select("5FR8_A_S21", "resi 713-729 & chain A & 5FR8 ")
cmd.color ("cyan", "5FR8_A_S21")


cmd.select("5FR8_barrel", "5FR8_A_S*")
cmd.show("cartoon", "5FR8_barrel")
cmd.zoom("5FR8_barrel")
