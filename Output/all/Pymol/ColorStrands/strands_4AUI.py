from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AUI.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4AUI_A_S0", "resi 3-18 & chain A & 4AUI ")
cmd.color ("red", "4AUI_A_S0")


cmd.select("4AUI_A_S1", "resi 31-47 & chain A & 4AUI ")
cmd.color ("yellow", "4AUI_A_S1")


cmd.select("4AUI_A_S2", "resi 54-61 & chain A & 4AUI ")
cmd.color ("green", "4AUI_A_S2")


cmd.select("4AUI_A_S3", "resi 75-82 & chain A & 4AUI ")
cmd.color ("cyan", "4AUI_A_S3")


cmd.select("4AUI_A_S4", "resi 87-95 & chain A & 4AUI ")
cmd.color ("blue", "4AUI_A_S4")


cmd.select("4AUI_A_S5", "resi 125-132 & chain A & 4AUI ")
cmd.color ("magenta", "4AUI_A_S5")


cmd.select("4AUI_A_S6", "resi 137-145 & chain A & 4AUI ")
cmd.color ("red", "4AUI_A_S6")


cmd.select("4AUI_A_S7", "resi 154-165 & chain A & 4AUI ")
cmd.color ("yellow", "4AUI_A_S7")


cmd.select("4AUI_A_S8", "resi 168-180 & chain A & 4AUI ")
cmd.color ("green", "4AUI_A_S8")


cmd.select("4AUI_A_S9", "resi 187-197 & chain A & 4AUI ")
cmd.color ("cyan", "4AUI_A_S9")


cmd.select("4AUI_A_S10", "resi 200-214 & chain A & 4AUI ")
cmd.color ("blue", "4AUI_A_S10")


cmd.select("4AUI_A_S11", "resi 221-235 & chain A & 4AUI ")
cmd.color ("magenta", "4AUI_A_S11")


cmd.select("4AUI_A_S12", "resi 240-249 & chain A & 4AUI ")
cmd.color ("red", "4AUI_A_S12")


cmd.select("4AUI_A_S13", "resi 262-271 & chain A & 4AUI ")
cmd.color ("yellow", "4AUI_A_S13")


cmd.select("4AUI_A_S14", "resi 278-288 & chain A & 4AUI ")
cmd.color ("green", "4AUI_A_S14")


cmd.select("4AUI_A_S15", "resi 295-306 & chain A & 4AUI ")
cmd.color ("cyan", "4AUI_A_S15")


cmd.select("4AUI_barrel", "4AUI_A_S*")
cmd.show("cartoon", "4AUI_barrel")
cmd.zoom("4AUI_barrel")
