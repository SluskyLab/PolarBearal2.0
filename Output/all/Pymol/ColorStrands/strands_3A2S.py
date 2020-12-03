from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3A2S_X_S0", "resi 3-19 & chain X & 3A2S ")
cmd.color ("red", "3A2S_X_S0")


cmd.select("3A2S_X_S1", "resi 28-49 & chain X & 3A2S ")
cmd.color ("yellow", "3A2S_X_S1")


cmd.select("3A2S_X_S2", "resi 56-63 & chain X & 3A2S ")
cmd.color ("green", "3A2S_X_S2")


cmd.select("3A2S_X_S3", "resi 77-84 & chain X & 3A2S ")
cmd.color ("cyan", "3A2S_X_S3")


cmd.select("3A2S_X_S4", "resi 89-97 & chain X & 3A2S ")
cmd.color ("blue", "3A2S_X_S4")


cmd.select("3A2S_X_S5", "resi 131-138 & chain X & 3A2S ")
cmd.color ("magenta", "3A2S_X_S5")


cmd.select("3A2S_X_S6", "resi 143-151 & chain X & 3A2S ")
cmd.color ("red", "3A2S_X_S6")


cmd.select("3A2S_X_S7", "resi 171-179 & chain X & 3A2S ")
cmd.color ("yellow", "3A2S_X_S7")


cmd.select("3A2S_X_S8", "resi 182-198 & chain X & 3A2S ")
cmd.color ("green", "3A2S_X_S8")


cmd.select("3A2S_X_S9", "resi 212-227 & chain X & 3A2S ")
cmd.color ("cyan", "3A2S_X_S9")


cmd.select("3A2S_X_S10", "resi 232-243 & chain X & 3A2S ")
cmd.color ("blue", "3A2S_X_S10")


cmd.select("3A2S_X_S11", "resi 255-266 & chain X & 3A2S ")
cmd.color ("magenta", "3A2S_X_S11")


cmd.select("3A2S_X_S12", "resi 272-284 & chain X & 3A2S ")
cmd.color ("red", "3A2S_X_S12")


cmd.select("3A2S_X_S13", "resi 295-306 & chain X & 3A2S ")
cmd.color ("yellow", "3A2S_X_S13")


cmd.select("3A2S_X_S14", "resi 310-321 & chain X & 3A2S ")
cmd.color ("green", "3A2S_X_S14")


cmd.select("3A2S_X_S15", "resi 328-341 & chain X & 3A2S ")
cmd.color ("cyan", "3A2S_X_S15")


cmd.select("3A2S_barrel", "3A2S_X_S*")
cmd.show("cartoon", "3A2S_barrel")
cmd.zoom("3A2S_barrel")
