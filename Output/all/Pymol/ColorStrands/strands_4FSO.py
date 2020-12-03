from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FSO_A_S0", "resi 7-20 & chain A & 4FSO ")
cmd.color ("red", "4FSO_A_S0")


cmd.select("4FSO_A_S1", "resi 35-51 & chain A & 4FSO ")
cmd.color ("yellow", "4FSO_A_S1")


cmd.select("4FSO_A_S2", "resi 56-67 & chain A & 4FSO ")
cmd.color ("green", "4FSO_A_S2")


cmd.select("4FSO_A_S3", "resi 97-105 & chain A & 4FSO ")
cmd.color ("cyan", "4FSO_A_S3")


cmd.select("4FSO_A_S4", "resi 108-114 & chain A & 4FSO ")
cmd.color ("blue", "4FSO_A_S4")


cmd.select("4FSO_A_S5", "resi 136-143 & chain A & 4FSO ")
cmd.color ("magenta", "4FSO_A_S5")


cmd.select("4FSO_A_S6", "resi 149-156 & chain A & 4FSO ")
cmd.color ("red", "4FSO_A_S6")


cmd.select("4FSO_A_S7", "resi 186-196 & chain A & 4FSO ")
cmd.color ("yellow", "4FSO_A_S7")


cmd.select("4FSO_A_S8", "resi 200-210 & chain A & 4FSO ")
cmd.color ("green", "4FSO_A_S8")


cmd.select("4FSO_A_S9", "resi 212-224 & chain A & 4FSO ")
cmd.color ("cyan", "4FSO_A_S9")


cmd.select("4FSO_A_S10", "resi 230-242 & chain A & 4FSO ")
cmd.color ("blue", "4FSO_A_S10")


cmd.select("4FSO_A_S11", "resi 251-263 & chain A & 4FSO ")
cmd.color ("magenta", "4FSO_A_S11")


cmd.select("4FSO_A_S12", "resi 268-279 & chain A & 4FSO ")
cmd.color ("red", "4FSO_A_S12")


cmd.select("4FSO_A_S13", "resi 306-317 & chain A & 4FSO ")
cmd.color ("yellow", "4FSO_A_S13")


cmd.select("4FSO_A_S14", "resi 322-337 & chain A & 4FSO ")
cmd.color ("green", "4FSO_A_S14")


cmd.select("4FSO_A_S15", "resi 345-357 & chain A & 4FSO ")
cmd.color ("cyan", "4FSO_A_S15")


cmd.select("4FSO_A_S16", "resi 367-378 & chain A & 4FSO ")
cmd.color ("blue", "4FSO_A_S16")


cmd.select("4FSO_A_S17", "resi 386-399 & chain A & 4FSO ")
cmd.color ("magenta", "4FSO_A_S17")


cmd.select("4FSO_barrel", "4FSO_A_S*")
cmd.show("cartoon", "4FSO_barrel")
cmd.zoom("4FSO_barrel")
