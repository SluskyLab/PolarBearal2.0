from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GSK.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2GSK_A_S0", "resi 137-145 & chain A & 2GSK ")
cmd.color ("red", "2GSK_A_S0")


cmd.select("2GSK_A_S1", "resi 149-158 & chain A & 2GSK ")
cmd.color ("yellow", "2GSK_A_S1")


cmd.select("2GSK_A_S2", "resi 164-178 & chain A & 2GSK ")
cmd.color ("green", "2GSK_A_S2")


cmd.select("2GSK_A_S3", "resi 188-210 & chain A & 2GSK ")
cmd.color ("cyan", "2GSK_A_S3")


cmd.select("2GSK_A_S4", "resi 213-233 & chain A & 2GSK ")
cmd.color ("blue", "2GSK_A_S4")


cmd.select("2GSK_A_S5", "resi 241-257 & chain A & 2GSK ")
cmd.color ("magenta", "2GSK_A_S5")


cmd.select("2GSK_A_S6", "resi 262-277 & chain A & 2GSK ")
cmd.color ("red", "2GSK_A_S6")


cmd.select("2GSK_A_S7", "resi 289-304 & chain A & 2GSK ")
cmd.color ("yellow", "2GSK_A_S7")


cmd.select("2GSK_A_S8", "resi 310-323 & chain A & 2GSK ")
cmd.color ("green", "2GSK_A_S8")


cmd.select("2GSK_A_S9", "resi 333-346 & chain A & 2GSK ")
cmd.color ("cyan", "2GSK_A_S9")


cmd.select("2GSK_A_S10", "resi 352-363 & chain A & 2GSK ")
cmd.color ("blue", "2GSK_A_S10")


cmd.select("2GSK_A_S11", "resi 366-379 & chain A & 2GSK ")
cmd.color ("magenta", "2GSK_A_S11")


cmd.select("2GSK_A_S12", "resi 383-394 & chain A & 2GSK ")
cmd.color ("red", "2GSK_A_S12")


cmd.select("2GSK_A_S13", "resi 413-424 & chain A & 2GSK ")
cmd.color ("yellow", "2GSK_A_S13")


cmd.select("2GSK_A_S14", "resi 430-447 & chain A & 2GSK ")
cmd.color ("green", "2GSK_A_S14")


cmd.select("2GSK_A_S15", "resi 451-470 & chain A & 2GSK ")
cmd.color ("cyan", "2GSK_A_S15")


cmd.select("2GSK_A_S16", "resi 476-489 & chain A & 2GSK ")
cmd.color ("blue", "2GSK_A_S16")


cmd.select("2GSK_A_S17", "resi 497-509 & chain A & 2GSK ")
cmd.color ("magenta", "2GSK_A_S17")


cmd.select("2GSK_A_S18", "resi 515-528 & chain A & 2GSK ")
cmd.color ("red", "2GSK_A_S18")


cmd.select("2GSK_A_S19", "resi 539-555 & chain A & 2GSK ")
cmd.color ("yellow", "2GSK_A_S19")


cmd.select("2GSK_A_S20", "resi 558-567 & chain A & 2GSK ")
cmd.color ("green", "2GSK_A_S20")


cmd.select("2GSK_A_S21", "resi 585-593 & chain A & 2GSK ")
cmd.color ("cyan", "2GSK_A_S21")


cmd.select("2GSK_barrel", "2GSK_A_S*")
cmd.show("cartoon", "2GSK_barrel")
cmd.zoom("2GSK_barrel")
