from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2POR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2POR_A_S0", "resi 3-14 & chain A & 2POR ")
cmd.color ("red", "2POR_A_S0")


cmd.select("2POR_A_S1", "resi 20-33 & chain A & 2POR ")
cmd.color ("yellow", "2POR_A_S1")


cmd.select("2POR_A_S2", "resi 40-52 & chain A & 2POR ")
cmd.color ("green", "2POR_A_S2")


cmd.select("2POR_A_S3", "resi 58-64 & chain A & 2POR ")
cmd.color ("cyan", "2POR_A_S3")


cmd.select("2POR_A_S4", "resi 69-73 & chain A & 2POR ")
cmd.color ("blue", "2POR_A_S4")


cmd.select("2POR_A_S5", "resi 118-123 & chain A & 2POR ")
cmd.color ("magenta", "2POR_A_S5")


cmd.select("2POR_A_S6", "resi 127-137 & chain A & 2POR ")
cmd.color ("red", "2POR_A_S6")


cmd.select("2POR_A_S7", "resi 146-157 & chain A & 2POR ")
cmd.color ("yellow", "2POR_A_S7")


cmd.select("2POR_A_S8", "resi 160-174 & chain A & 2POR ")
cmd.color ("green", "2POR_A_S8")


cmd.select("2POR_A_S9", "resi 178-191 & chain A & 2POR ")
cmd.color ("cyan", "2POR_A_S9")


cmd.select("2POR_A_S10", "resi 194-208 & chain A & 2POR ")
cmd.color ("blue", "2POR_A_S10")


cmd.select("2POR_A_S11", "resi 225-239 & chain A & 2POR ")
cmd.color ("magenta", "2POR_A_S11")


cmd.select("2POR_A_S12", "resi 244-254 & chain A & 2POR ")
cmd.color ("red", "2POR_A_S12")


cmd.select("2POR_A_S13", "resi 258-271 & chain A & 2POR ")
cmd.color ("yellow", "2POR_A_S13")


cmd.select("2POR_A_S14", "resi 274-285 & chain A & 2POR ")
cmd.color ("green", "2POR_A_S14")


cmd.select("2POR_A_S15", "resi 292-301 & chain A & 2POR ")
cmd.color ("cyan", "2POR_A_S15")


cmd.select("2POR_barrel", "2POR_A_S*")
cmd.show("cartoon", "2POR_barrel")
cmd.zoom("2POR_barrel")
