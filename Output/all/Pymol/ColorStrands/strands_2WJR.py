from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WJR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2WJR_A_S0", "resi 3-10 & chain A & 2WJR ")
cmd.color ("red", "2WJR_A_S0")


cmd.select("2WJR_A_S1", "resi 14-24 & chain A & 2WJR ")
cmd.color ("yellow", "2WJR_A_S1")


cmd.select("2WJR_A_S2", "resi 31-40 & chain A & 2WJR ")
cmd.color ("green", "2WJR_A_S2")


cmd.select("2WJR_A_S3", "resi 54-65 & chain A & 2WJR ")
cmd.color ("cyan", "2WJR_A_S3")


cmd.select("2WJR_A_S4", "resi 69-79 & chain A & 2WJR ")
cmd.color ("blue", "2WJR_A_S4")


cmd.select("2WJR_A_S5", "resi 84-96 & chain A & 2WJR ")
cmd.color ("magenta", "2WJR_A_S5")


cmd.select("2WJR_A_S6", "resi 100-115 & chain A & 2WJR ")
cmd.color ("red", "2WJR_A_S6")


cmd.select("2WJR_A_S7", "resi 123-138 & chain A & 2WJR ")
cmd.color ("yellow", "2WJR_A_S7")


cmd.select("2WJR_A_S8", "resi 142-152 & chain A & 2WJR ")
cmd.color ("green", "2WJR_A_S8")


cmd.select("2WJR_A_S9", "resi 166-175 & chain A & 2WJR ")
cmd.color ("cyan", "2WJR_A_S9")


cmd.select("2WJR_A_S10", "resi 182-191 & chain A & 2WJR ")
cmd.color ("blue", "2WJR_A_S10")


cmd.select("2WJR_A_S11", "resi 204-213 & chain A & 2WJR ")
cmd.color ("magenta", "2WJR_A_S11")


cmd.select("2WJR_barrel", "2WJR_A_S*")
cmd.show("cartoon", "2WJR_barrel")
cmd.zoom("2WJR_barrel")
