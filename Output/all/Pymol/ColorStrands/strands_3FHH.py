from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FHH.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3FHH_A_S0", "resi 136-146 & chain A & 3FHH ")
cmd.color ("red", "3FHH_A_S0")


cmd.select("3FHH_A_S1", "resi 150-161 & chain A & 3FHH ")
cmd.color ("yellow", "3FHH_A_S1")


cmd.select("3FHH_A_S2", "resi 166-177 & chain A & 3FHH ")
cmd.color ("green", "3FHH_A_S2")


cmd.select("3FHH_A_S3", "resi 190-202 & chain A & 3FHH ")
cmd.color ("cyan", "3FHH_A_S3")


cmd.select("3FHH_A_S4", "resi 207-222 & chain A & 3FHH ")
cmd.color ("blue", "3FHH_A_S4")


cmd.select("3FHH_A_S5", "resi 240-256 & chain A & 3FHH ")
cmd.color ("magenta", "3FHH_A_S5")


cmd.select("3FHH_A_S6", "resi 264-279 & chain A & 3FHH ")
cmd.color ("red", "3FHH_A_S6")


cmd.select("3FHH_A_S7", "resi 288-303 & chain A & 3FHH ")
cmd.color ("yellow", "3FHH_A_S7")


cmd.select("3FHH_A_S8", "resi 310-325 & chain A & 3FHH ")
cmd.color ("green", "3FHH_A_S8")


cmd.select("3FHH_A_S9", "resi 344-359 & chain A & 3FHH ")
cmd.color ("cyan", "3FHH_A_S9")


cmd.select("3FHH_A_S10", "resi 364-378 & chain A & 3FHH ")
cmd.color ("blue", "3FHH_A_S10")


cmd.select("3FHH_A_S11", "resi 387-398 & chain A & 3FHH ")
cmd.color ("magenta", "3FHH_A_S11")


cmd.select("3FHH_A_S12", "resi 403-429 & chain A & 3FHH ")
cmd.color ("red", "3FHH_A_S12")


cmd.select("3FHH_A_S13", "resi 437-461 & chain A & 3FHH ")
cmd.color ("yellow", "3FHH_A_S13")


cmd.select("3FHH_A_S14", "resi 470-495 & chain A & 3FHH ")
cmd.color ("green", "3FHH_A_S14")


cmd.select("3FHH_A_S15", "resi 498-517 & chain A & 3FHH ")
cmd.color ("cyan", "3FHH_A_S15")


cmd.select("3FHH_A_S16", "resi 522-533 & chain A & 3FHH ")
cmd.color ("blue", "3FHH_A_S16")


cmd.select("3FHH_A_S17", "resi 548-555 & chain A & 3FHH ")
cmd.color ("magenta", "3FHH_A_S17")


cmd.select("3FHH_A_S18", "resi 563-574 & chain A & 3FHH ")
cmd.color ("red", "3FHH_A_S18")


cmd.select("3FHH_A_S19", "resi 584-596 & chain A & 3FHH ")
cmd.color ("yellow", "3FHH_A_S19")


cmd.select("3FHH_A_S20", "resi 604-619 & chain A & 3FHH ")
cmd.color ("green", "3FHH_A_S20")


cmd.select("3FHH_A_S21", "resi 625-639 & chain A & 3FHH ")
cmd.color ("cyan", "3FHH_A_S21")


cmd.select("3FHH_barrel", "3FHH_A_S*")
cmd.show("cartoon", "3FHH_barrel")
cmd.zoom("3FHH_barrel")
