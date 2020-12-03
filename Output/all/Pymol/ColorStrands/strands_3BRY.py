from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BRY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3BRY_A_S0", "resi 43-54 & chain A & 3BRY ")
cmd.color ("red", "3BRY_A_S0")


cmd.select("3BRY_A_S1", "resi 84-90 & chain A & 3BRY ")
cmd.color ("yellow", "3BRY_A_S1")


cmd.select("3BRY_A_S2", "resi 95-108 & chain A & 3BRY ")
cmd.color ("green", "3BRY_A_S2")


cmd.select("3BRY_A_S3", "resi 130-146 & chain A & 3BRY ")
cmd.color ("cyan", "3BRY_A_S3")


cmd.select("3BRY_A_S4", "resi 150-169 & chain A & 3BRY ")
cmd.color ("blue", "3BRY_A_S4")


cmd.select("3BRY_A_S5", "resi 198-229 & chain A & 3BRY ")
cmd.color ("magenta", "3BRY_A_S5")


cmd.select("3BRY_A_S6", "resi 232-257 & chain A & 3BRY ")
cmd.color ("red", "3BRY_A_S6")


cmd.select("3BRY_A_S7", "resi 264-289 & chain A & 3BRY ")
cmd.color ("yellow", "3BRY_A_S7")


cmd.select("3BRY_A_S8", "resi 293-316 & chain A & 3BRY ")
cmd.color ("green", "3BRY_A_S8")


cmd.select("3BRY_A_S9", "resi 326-346 & chain A & 3BRY ")
cmd.color ("cyan", "3BRY_A_S9")


cmd.select("3BRY_A_S10", "resi 350-360 & chain A & 3BRY ")
cmd.color ("blue", "3BRY_A_S10")


cmd.select("3BRY_A_S11", "resi 378-388 & chain A & 3BRY ")
cmd.color ("magenta", "3BRY_A_S11")


cmd.select("3BRY_A_S12", "resi 391-402 & chain A & 3BRY ")
cmd.color ("red", "3BRY_A_S12")


cmd.select("3BRY_A_S13", "resi 424-435 & chain A & 3BRY ")
cmd.color ("yellow", "3BRY_A_S13")


cmd.select("3BRY_barrel", "3BRY_A_S*")
cmd.show("cartoon", "3BRY_barrel")
cmd.zoom("3BRY_barrel")
