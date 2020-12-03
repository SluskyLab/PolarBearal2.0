from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A0S.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1A0S_P_S0", "resi 74-85 & chain P & 1A0S ")
cmd.color ("red", "1A0S_P_S0")


cmd.select("1A0S_P_S1", "resi 118-127 & chain P & 1A0S ")
cmd.color ("yellow", "1A0S_P_S1")


cmd.select("1A0S_P_S2", "resi 134-145 & chain P & 1A0S ")
cmd.color ("green", "1A0S_P_S2")


cmd.select("1A0S_P_S3", "resi 159-168 & chain P & 1A0S ")
cmd.color ("cyan", "1A0S_P_S3")


cmd.select("1A0S_P_S4", "resi 181-195 & chain P & 1A0S ")
cmd.color ("blue", "1A0S_P_S4")


cmd.select("1A0S_P_S5", "resi 200-217 & chain P & 1A0S ")
cmd.color ("magenta", "1A0S_P_S5")


cmd.select("1A0S_P_S6", "resi 221-232 & chain P & 1A0S ")
cmd.color ("red", "1A0S_P_S6")


cmd.select("1A0S_P_S7", "resi 242-252 & chain P & 1A0S ")
cmd.color ("yellow", "1A0S_P_S7")


cmd.select("1A0S_P_S8", "resi 255-265 & chain P & 1A0S ")
cmd.color ("green", "1A0S_P_S8")


cmd.select("1A0S_P_S9", "resi 285-296 & chain P & 1A0S ")
cmd.color ("cyan", "1A0S_P_S9")


cmd.select("1A0S_P_S10", "resi 303-315 & chain P & 1A0S ")
cmd.color ("blue", "1A0S_P_S10")


cmd.select("1A0S_P_S11", "resi 335-345 & chain P & 1A0S ")
cmd.color ("magenta", "1A0S_P_S11")


cmd.select("1A0S_P_S12", "resi 351-363 & chain P & 1A0S ")
cmd.color ("red", "1A0S_P_S12")


cmd.select("1A0S_P_S13", "resi 371-385 & chain P & 1A0S ")
cmd.color ("yellow", "1A0S_P_S13")


cmd.select("1A0S_P_S14", "resi 388-403 & chain P & 1A0S ")
cmd.color ("green", "1A0S_P_S14")


cmd.select("1A0S_P_S15", "resi 413-427 & chain P & 1A0S ")
cmd.color ("cyan", "1A0S_P_S15")


cmd.select("1A0S_P_S16", "resi 439-450 & chain P & 1A0S ")
cmd.color ("blue", "1A0S_P_S16")


cmd.select("1A0S_P_S17", "resi 472-483 & chain P & 1A0S ")
cmd.color ("magenta", "1A0S_P_S17")


cmd.select("1A0S_barrel", "1A0S_P_S*")
cmd.show("cartoon", "1A0S_barrel")
cmd.zoom("1A0S_barrel")
