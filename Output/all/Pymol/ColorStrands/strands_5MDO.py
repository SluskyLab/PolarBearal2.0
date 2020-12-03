from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5MDO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5MDO_A_S0", "resi 20-35 & chain A & 5MDO ")
cmd.color ("red", "5MDO_A_S0")


cmd.select("5MDO_A_S1", "resi 47-62 & chain A & 5MDO ")
cmd.color ("yellow", "5MDO_A_S1")


cmd.select("5MDO_A_S2", "resi 70-81 & chain A & 5MDO ")
cmd.color ("green", "5MDO_A_S2")


cmd.select("5MDO_A_S3", "resi 94-102 & chain A & 5MDO ")
cmd.color ("cyan", "5MDO_A_S3")


cmd.select("5MDO_A_S4", "resi 106-111 & chain A & 5MDO ")
cmd.color ("blue", "5MDO_A_S4")


cmd.select("5MDO_A_S5", "resi 149-160 & chain A & 5MDO ")
cmd.color ("magenta", "5MDO_A_S5")


cmd.select("5MDO_A_S6", "resi 164-171 & chain A & 5MDO ")
cmd.color ("red", "5MDO_A_S6")


cmd.select("5MDO_A_S7", "resi 184-192 & chain A & 5MDO ")
cmd.color ("yellow", "5MDO_A_S7")


cmd.select("5MDO_A_S8", "resi 196-209 & chain A & 5MDO ")
cmd.color ("green", "5MDO_A_S8")


cmd.select("5MDO_A_S9", "resi 215-229 & chain A & 5MDO ")
cmd.color ("cyan", "5MDO_A_S9")


cmd.select("5MDO_A_S10", "resi 232-247 & chain A & 5MDO ")
cmd.color ("blue", "5MDO_A_S10")


cmd.select("5MDO_A_S11", "resi 251-264 & chain A & 5MDO ")
cmd.color ("magenta", "5MDO_A_S11")


cmd.select("5MDO_A_S12", "resi 269-283 & chain A & 5MDO ")
cmd.color ("red", "5MDO_A_S12")


cmd.select("5MDO_A_S13", "resi 292-301 & chain A & 5MDO ")
cmd.color ("yellow", "5MDO_A_S13")


cmd.select("5MDO_A_S14", "resi 306-322 & chain A & 5MDO ")
cmd.color ("green", "5MDO_A_S14")


cmd.select("5MDO_A_S15", "resi 328-350 & chain A & 5MDO ")
cmd.color ("cyan", "5MDO_A_S15")


cmd.select("5MDO_barrel", "5MDO_A_S*")
cmd.show("cartoon", "5MDO_barrel")
cmd.zoom("5MDO_barrel")
