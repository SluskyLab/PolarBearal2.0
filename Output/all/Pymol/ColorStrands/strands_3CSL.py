from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3CSL.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3CSL_A_S0", "resi 242-252 & chain A & 3CSL ")
cmd.color ("red", "3CSL_A_S0")


cmd.select("3CSL_A_S1", "resi 255-267 & chain A & 3CSL ")
cmd.color ("yellow", "3CSL_A_S1")


cmd.select("3CSL_A_S2", "resi 270-283 & chain A & 3CSL ")
cmd.color ("green", "3CSL_A_S2")


cmd.select("3CSL_A_S3", "resi 322-335 & chain A & 3CSL ")
cmd.color ("cyan", "3CSL_A_S3")


cmd.select("3CSL_A_S4", "resi 338-361 & chain A & 3CSL ")
cmd.color ("blue", "3CSL_A_S4")


cmd.select("3CSL_A_S5", "resi 368-391 & chain A & 3CSL ")
cmd.color ("magenta", "3CSL_A_S5")


cmd.select("3CSL_A_S6", "resi 396-415 & chain A & 3CSL ")
cmd.color ("red", "3CSL_A_S6")


cmd.select("3CSL_A_S7", "resi 426-447 & chain A & 3CSL ")
cmd.color ("yellow", "3CSL_A_S7")


cmd.select("3CSL_A_S8", "resi 451-471 & chain A & 3CSL ")
cmd.color ("green", "3CSL_A_S8")


cmd.select("3CSL_A_S9", "resi 482-497 & chain A & 3CSL ")
cmd.color ("cyan", "3CSL_A_S9")


cmd.select("3CSL_A_S10", "resi 501-524 & chain A & 3CSL ")
cmd.color ("blue", "3CSL_A_S10")


cmd.select("3CSL_A_S11", "resi 548-571 & chain A & 3CSL ")
cmd.color ("magenta", "3CSL_A_S11")


cmd.select("3CSL_A_S12", "resi 577-589 & chain A & 3CSL ")
cmd.color ("red", "3CSL_A_S12")


cmd.select("3CSL_A_S13", "resi 607-630 & chain A & 3CSL ")
cmd.color ("yellow", "3CSL_A_S13")


cmd.select("3CSL_A_S14", "resi 639-672 & chain A & 3CSL ")
cmd.color ("green", "3CSL_A_S14")


cmd.select("3CSL_A_S15", "resi 675-695 & chain A & 3CSL ")
cmd.color ("cyan", "3CSL_A_S15")


cmd.select("3CSL_A_S16", "resi 700-716 & chain A & 3CSL ")
cmd.color ("blue", "3CSL_A_S16")


cmd.select("3CSL_A_S17", "resi 749-775 & chain A & 3CSL ")
cmd.color ("magenta", "3CSL_A_S17")


cmd.select("3CSL_A_S18", "resi 779-794 & chain A & 3CSL ")
cmd.color ("red", "3CSL_A_S18")


cmd.select("3CSL_A_S19", "resi 805-819 & chain A & 3CSL ")
cmd.color ("yellow", "3CSL_A_S19")


cmd.select("3CSL_A_S20", "resi 826-839 & chain A & 3CSL ")
cmd.color ("green", "3CSL_A_S20")


cmd.select("3CSL_A_S21", "resi 852-862 & chain A & 3CSL ")
cmd.color ("cyan", "3CSL_A_S21")


cmd.select("3CSL_barrel", "3CSL_A_S*")
cmd.show("cartoon", "3CSL_barrel")
cmd.zoom("3CSL_barrel")
