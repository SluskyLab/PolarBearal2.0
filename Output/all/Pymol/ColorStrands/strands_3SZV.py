from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZV.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SZV_A_S0", "resi 7-20 & chain A & 3SZV ")
cmd.color ("red", "3SZV_A_S0")


cmd.select("3SZV_A_S1", "resi 32-46 & chain A & 3SZV ")
cmd.color ("yellow", "3SZV_A_S1")


cmd.select("3SZV_A_S2", "resi 51-62 & chain A & 3SZV ")
cmd.color ("green", "3SZV_A_S2")


cmd.select("3SZV_A_S3", "resi 89-99 & chain A & 3SZV ")
cmd.color ("cyan", "3SZV_A_S3")


cmd.select("3SZV_A_S4", "resi 102-108 & chain A & 3SZV ")
cmd.color ("blue", "3SZV_A_S4")


cmd.select("3SZV_A_S5", "resi 130-137 & chain A & 3SZV ")
cmd.color ("magenta", "3SZV_A_S5")


cmd.select("3SZV_A_S6", "resi 143-150 & chain A & 3SZV ")
cmd.color ("red", "3SZV_A_S6")


cmd.select("3SZV_A_S7", "resi 174-184 & chain A & 3SZV ")
cmd.color ("yellow", "3SZV_A_S7")


cmd.select("3SZV_A_S8", "resi 187-198 & chain A & 3SZV ")
cmd.color ("green", "3SZV_A_S8")


cmd.select("3SZV_A_S9", "resi 200-212 & chain A & 3SZV ")
cmd.color ("cyan", "3SZV_A_S9")


cmd.select("3SZV_A_S10", "resi 219-230 & chain A & 3SZV ")
cmd.color ("blue", "3SZV_A_S10")


cmd.select("3SZV_A_S11", "resi 239-250 & chain A & 3SZV ")
cmd.color ("magenta", "3SZV_A_S11")


cmd.select("3SZV_A_S12", "resi 253-266 & chain A & 3SZV ")
cmd.color ("red", "3SZV_A_S12")


cmd.select("3SZV_A_S13", "resi 294-304 & chain A & 3SZV ")
cmd.color ("yellow", "3SZV_A_S13")


cmd.select("3SZV_A_S14", "resi 309-322 & chain A & 3SZV ")
cmd.color ("green", "3SZV_A_S14")


cmd.select("3SZV_A_S15", "resi 333-344 & chain A & 3SZV ")
cmd.color ("cyan", "3SZV_A_S15")


cmd.select("3SZV_A_S16", "resi 354-365 & chain A & 3SZV ")
cmd.color ("blue", "3SZV_A_S16")


cmd.select("3SZV_A_S17", "resi 370-384 & chain A & 3SZV ")
cmd.color ("magenta", "3SZV_A_S17")


cmd.select("3SZV_barrel", "3SZV_A_S*")
cmd.show("cartoon", "3SZV_barrel")
cmd.zoom("3SZV_barrel")
