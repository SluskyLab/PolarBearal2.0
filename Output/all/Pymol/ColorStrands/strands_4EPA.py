from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4EPA.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4EPA_A_S0", "resi 140-149 & chain A & 4EPA ")
cmd.color ("red", "4EPA_A_S0")


cmd.select("4EPA_A_S1", "resi 152-164 & chain A & 4EPA ")
cmd.color ("yellow", "4EPA_A_S1")


cmd.select("4EPA_A_S2", "resi 167-178 & chain A & 4EPA ")
cmd.color ("green", "4EPA_A_S2")


cmd.select("4EPA_A_S3", "resi 194-208 & chain A & 4EPA ")
cmd.color ("cyan", "4EPA_A_S3")


cmd.select("4EPA_A_S4", "resi 213-228 & chain A & 4EPA ")
cmd.color ("blue", "4EPA_A_S4")


cmd.select("4EPA_A_S5", "resi 253-268 & chain A & 4EPA ")
cmd.color ("magenta", "4EPA_A_S5")


cmd.select("4EPA_A_S6", "resi 273-289 & chain A & 4EPA ")
cmd.color ("red", "4EPA_A_S6")


cmd.select("4EPA_A_S7", "resi 295-313 & chain A & 4EPA ")
cmd.color ("yellow", "4EPA_A_S7")


cmd.select("4EPA_A_S8", "resi 321-340 & chain A & 4EPA ")
cmd.color ("green", "4EPA_A_S8")


cmd.select("4EPA_A_S9", "resi 347-368 & chain A & 4EPA ")
cmd.color ("cyan", "4EPA_A_S9")


cmd.select("4EPA_A_S10", "resi 372-392 & chain A & 4EPA ")
cmd.color ("blue", "4EPA_A_S10")


cmd.select("4EPA_A_S11", "resi 398-419 & chain A & 4EPA ")
cmd.color ("magenta", "4EPA_A_S11")


cmd.select("4EPA_A_S12", "resi 422-437 & chain A & 4EPA ")
cmd.color ("red", "4EPA_A_S12")


cmd.select("4EPA_A_S13", "resi 451-466 & chain A & 4EPA ")
cmd.color ("yellow", "4EPA_A_S13")


cmd.select("4EPA_A_S14", "resi 471-486 & chain A & 4EPA ")
cmd.color ("green", "4EPA_A_S14")


cmd.select("4EPA_A_S15", "resi 499-513 & chain A & 4EPA ")
cmd.color ("cyan", "4EPA_A_S15")


cmd.select("4EPA_A_S16", "resi 520-533 & chain A & 4EPA ")
cmd.color ("blue", "4EPA_A_S16")


cmd.select("4EPA_A_S17", "resi 544-558 & chain A & 4EPA ")
cmd.color ("magenta", "4EPA_A_S17")


cmd.select("4EPA_A_S18", "resi 568-581 & chain A & 4EPA ")
cmd.color ("red", "4EPA_A_S18")


cmd.select("4EPA_A_S19", "resi 587-601 & chain A & 4EPA ")
cmd.color ("yellow", "4EPA_A_S19")


cmd.select("4EPA_A_S20", "resi 606-626 & chain A & 4EPA ")
cmd.color ("green", "4EPA_A_S20")


cmd.select("4EPA_A_S21", "resi 633-650 & chain A & 4EPA ")
cmd.color ("cyan", "4EPA_A_S21")


cmd.select("4EPA_barrel", "4EPA_A_S*")
cmd.show("cartoon", "4EPA_barrel")
cmd.zoom("4EPA_barrel")
