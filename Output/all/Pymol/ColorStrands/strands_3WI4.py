from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3WI4.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3WI4_A_S0", "resi 4-20 & chain A & 3WI4 ")
cmd.color ("red", "3WI4_A_S0")


cmd.select("3WI4_A_S1", "resi 27-48 & chain A & 3WI4 ")
cmd.color ("yellow", "3WI4_A_S1")


cmd.select("3WI4_A_S2", "resi 55-62 & chain A & 3WI4 ")
cmd.color ("green", "3WI4_A_S2")


cmd.select("3WI4_A_S3", "resi 76-83 & chain A & 3WI4 ")
cmd.color ("cyan", "3WI4_A_S3")


cmd.select("3WI4_A_S4", "resi 88-96 & chain A & 3WI4 ")
cmd.color ("blue", "3WI4_A_S4")


cmd.select("3WI4_A_S5", "resi 126-133 & chain A & 3WI4 ")
cmd.color ("magenta", "3WI4_A_S5")


cmd.select("3WI4_A_S6", "resi 138-146 & chain A & 3WI4 ")
cmd.color ("red", "3WI4_A_S6")


cmd.select("3WI4_A_S7", "resi 156-166 & chain A & 3WI4 ")
cmd.color ("yellow", "3WI4_A_S7")


cmd.select("3WI4_A_S8", "resi 169-181 & chain A & 3WI4 ")
cmd.color ("green", "3WI4_A_S8")


cmd.select("3WI4_A_S9", "resi 190-203 & chain A & 3WI4 ")
cmd.color ("cyan", "3WI4_A_S9")


cmd.select("3WI4_A_S10", "resi 208-219 & chain A & 3WI4 ")
cmd.color ("blue", "3WI4_A_S10")


cmd.select("3WI4_A_S11", "resi 228-238 & chain A & 3WI4 ")
cmd.color ("magenta", "3WI4_A_S11")


cmd.select("3WI4_A_S12", "resi 243-257 & chain A & 3WI4 ")
cmd.color ("red", "3WI4_A_S12")


cmd.select("3WI4_A_S13", "resi 267-277 & chain A & 3WI4 ")
cmd.color ("yellow", "3WI4_A_S13")


cmd.select("3WI4_A_S14", "resi 283-293 & chain A & 3WI4 ")
cmd.color ("green", "3WI4_A_S14")


cmd.select("3WI4_A_S15", "resi 300-313 & chain A & 3WI4 ")
cmd.color ("cyan", "3WI4_A_S15")


cmd.select("3WI4_barrel", "3WI4_A_S*")
cmd.show("cartoon", "3WI4_barrel")
cmd.zoom("3WI4_barrel")
