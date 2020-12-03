from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4CU4.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4CU4_A_S0", "resi 161-169 & chain A & 4CU4 ")
cmd.color ("red", "4CU4_A_S0")


cmd.select("4CU4_A_S1", "resi 173-184 & chain A & 4CU4 ")
cmd.color ("yellow", "4CU4_A_S1")


cmd.select("4CU4_A_S2", "resi 189-201 & chain A & 4CU4 ")
cmd.color ("green", "4CU4_A_S2")


cmd.select("4CU4_A_S3", "resi 210-222 & chain A & 4CU4 ")
cmd.color ("cyan", "4CU4_A_S3")


cmd.select("4CU4_A_S4", "resi 228-240 & chain A & 4CU4 ")
cmd.color ("blue", "4CU4_A_S4")


cmd.select("4CU4_A_S5", "resi 274-290 & chain A & 4CU4 ")
cmd.color ("magenta", "4CU4_A_S5")


cmd.select("4CU4_A_S6", "resi 293-318 & chain A & 4CU4 ")
cmd.color ("red", "4CU4_A_S6")


cmd.select("4CU4_A_S7", "resi 340-365 & chain A & 4CU4 ")
cmd.color ("yellow", "4CU4_A_S7")


cmd.select("4CU4_A_S8", "resi 371-392 & chain A & 4CU4 ")
cmd.color ("green", "4CU4_A_S8")


cmd.select("4CU4_A_S9", "resi 432-452 & chain A & 4CU4 ")
cmd.color ("cyan", "4CU4_A_S9")


cmd.select("4CU4_A_S10", "resi 457-474 & chain A & 4CU4 ")
cmd.color ("blue", "4CU4_A_S10")


cmd.select("4CU4_A_S11", "resi 480-495 & chain A & 4CU4 ")
cmd.color ("magenta", "4CU4_A_S11")


cmd.select("4CU4_A_S12", "resi 500-512 & chain A & 4CU4 ")
cmd.color ("red", "4CU4_A_S12")


cmd.select("4CU4_A_S13", "resi 527-539 & chain A & 4CU4 ")
cmd.color ("yellow", "4CU4_A_S13")


cmd.select("4CU4_A_S14", "resi 546-561 & chain A & 4CU4 ")
cmd.color ("green", "4CU4_A_S14")


cmd.select("4CU4_A_S15", "resi 571-589 & chain A & 4CU4 ")
cmd.color ("cyan", "4CU4_A_S15")


cmd.select("4CU4_A_S16", "resi 592-608 & chain A & 4CU4 ")
cmd.color ("blue", "4CU4_A_S16")


cmd.select("4CU4_A_S17", "resi 622-633 & chain A & 4CU4 ")
cmd.color ("magenta", "4CU4_A_S17")


cmd.select("4CU4_A_S18", "resi 641-655 & chain A & 4CU4 ")
cmd.color ("red", "4CU4_A_S18")


cmd.select("4CU4_A_S19", "resi 661-677 & chain A & 4CU4 ")
cmd.color ("yellow", "4CU4_A_S19")


cmd.select("4CU4_A_S20", "resi 682-704 & chain A & 4CU4 ")
cmd.color ("green", "4CU4_A_S20")


cmd.select("4CU4_A_S21", "resi 708-722 & chain A & 4CU4 ")
cmd.color ("cyan", "4CU4_A_S21")


cmd.select("4CU4_barrel", "4CU4_A_S*")
cmd.show("cartoon", "4CU4_barrel")
cmd.zoom("4CU4_barrel")
