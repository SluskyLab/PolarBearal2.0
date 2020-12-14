from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXM.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5IXM_A_S0", "resi 4-12 & chain A & 5IXM ")
cmd.color ("red", "5IXM_A_S0")


cmd.select("5IXM_A_S1", "resi 15-26 & chain A & 5IXM ")
cmd.color ("yellow", "5IXM_A_S1")


cmd.select("5IXM_A_S2", "resi 29-39 & chain A & 5IXM ")
cmd.color ("green", "5IXM_A_S2")


cmd.select("5IXM_A_S3", "resi 43-53 & chain A & 5IXM ")
cmd.color ("cyan", "5IXM_A_S3")


cmd.select("5IXM_A_S4", "resi 58-66 & chain A & 5IXM ")
cmd.color ("blue", "5IXM_A_S4")


cmd.select("5IXM_A_S5", "resi 84-93 & chain A & 5IXM ")
cmd.color ("magenta", "5IXM_A_S5")


cmd.select("5IXM_A_S6", "resi 98-109 & chain A & 5IXM ")
cmd.color ("red", "5IXM_A_S6")


cmd.select("5IXM_A_S7", "resi 129-138 & chain A & 5IXM ")
cmd.color ("yellow", "5IXM_A_S7")


cmd.select("5IXM_A_S8", "resi 141-152 & chain A & 5IXM ")
cmd.color ("green", "5IXM_A_S8")


cmd.select("5IXM_A_S9", "resi 164-175 & chain A & 5IXM ")
cmd.color ("cyan", "5IXM_A_S9")


cmd.select("5IXM_A_S10", "resi 182-193 & chain A & 5IXM ")
cmd.color ("blue", "5IXM_A_S10")


cmd.select("5IXM_A_S11", "resi 201-215 & chain A & 5IXM ")
cmd.color ("magenta", "5IXM_A_S11")


cmd.select("5IXM_A_S12", "resi 221-236 & chain A & 5IXM ")
cmd.color ("red", "5IXM_A_S12")


cmd.select("5IXM_A_S13", "resi 252-271 & chain A & 5IXM ")
cmd.color ("yellow", "5IXM_A_S13")


cmd.select("5IXM_A_S14", "resi 280-292 & chain A & 5IXM ")
cmd.color ("green", "5IXM_A_S14")


cmd.select("5IXM_A_S15", "resi 329-343 & chain A & 5IXM ")
cmd.color ("cyan", "5IXM_A_S15")


cmd.select("5IXM_A_S16", "resi 347-364 & chain A & 5IXM ")
cmd.color ("blue", "5IXM_A_S16")


cmd.select("5IXM_A_S17", "resi 380-390 & chain A & 5IXM ")
cmd.color ("magenta", "5IXM_A_S17")


cmd.select("5IXM_A_S18", "resi 393-403 & chain A & 5IXM ")
cmd.color ("red", "5IXM_A_S18")


cmd.select("5IXM_A_S19", "resi 410-420 & chain A & 5IXM ")
cmd.color ("yellow", "5IXM_A_S19")


cmd.select("5IXM_A_S20", "resi 424-433 & chain A & 5IXM ")
cmd.color ("green", "5IXM_A_S20")


cmd.select("5IXM_A_S21", "resi 454-463 & chain A & 5IXM ")
cmd.color ("cyan", "5IXM_A_S21")


cmd.select("5IXM_A_S22", "resi 468-478 & chain A & 5IXM ")
cmd.color ("blue", "5IXM_A_S22")


cmd.select("5IXM_A_S23", "resi 483-494 & chain A & 5IXM ")
cmd.color ("magenta", "5IXM_A_S23")


cmd.select("5IXM_A_S24", "resi 500-510 & chain A & 5IXM ")
cmd.color ("red", "5IXM_A_S24")


cmd.select("5IXM_A_S25", "resi 519-527 & chain A & 5IXM ")
cmd.color ("yellow", "5IXM_A_S25")


cmd.select("5IXM_barrel", "5IXM_A_S*")
cmd.show("cartoon", "5IXM_barrel")
cmd.zoom("5IXM_barrel")
