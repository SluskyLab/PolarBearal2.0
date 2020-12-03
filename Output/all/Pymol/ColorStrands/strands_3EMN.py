from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3EMN_X_S0", "resi 25-33 & chain X & 3EMN ")
cmd.color ("red", "3EMN_X_S0")


cmd.select("3EMN_X_S1", "resi 40-47 & chain X & 3EMN ")
cmd.color ("yellow", "3EMN_X_S1")


cmd.select("3EMN_X_S2", "resi 55-64 & chain X & 3EMN ")
cmd.color ("green", "3EMN_X_S2")


cmd.select("3EMN_X_S3", "resi 68-77 & chain X & 3EMN ")
cmd.color ("cyan", "3EMN_X_S3")


cmd.select("3EMN_X_S4", "resi 80-88 & chain X & 3EMN ")
cmd.color ("blue", "3EMN_X_S4")


cmd.select("3EMN_X_S5", "resi 94-104 & chain X & 3EMN ")
cmd.color ("magenta", "3EMN_X_S5")


cmd.select("3EMN_X_S6", "resi 109-119 & chain X & 3EMN ")
cmd.color ("red", "3EMN_X_S6")


cmd.select("3EMN_X_S7", "resi 122-131 & chain X & 3EMN ")
cmd.color ("yellow", "3EMN_X_S7")


cmd.select("3EMN_X_S8", "resi 137-145 & chain X & 3EMN ")
cmd.color ("green", "3EMN_X_S8")


cmd.select("3EMN_X_S9", "resi 148-158 & chain X & 3EMN ")
cmd.color ("cyan", "3EMN_X_S9")


cmd.select("3EMN_X_S10", "resi 163-174 & chain X & 3EMN ")
cmd.color ("blue", "3EMN_X_S10")


cmd.select("3EMN_X_S11", "resi 179-186 & chain X & 3EMN ")
cmd.color ("magenta", "3EMN_X_S11")


cmd.select("3EMN_X_S12", "resi 189-198 & chain X & 3EMN ")
cmd.color ("red", "3EMN_X_S12")


cmd.select("3EMN_X_S13", "resi 202-210 & chain X & 3EMN ")
cmd.color ("yellow", "3EMN_X_S13")


cmd.select("3EMN_X_S14", "resi 218-227 & chain X & 3EMN ")
cmd.color ("green", "3EMN_X_S14")


cmd.select("3EMN_X_S15", "resi 231-239 & chain X & 3EMN ")
cmd.color ("cyan", "3EMN_X_S15")


cmd.select("3EMN_X_S16", "resi 242-251 & chain X & 3EMN ")
cmd.color ("blue", "3EMN_X_S16")


cmd.select("3EMN_X_S17", "resi 254-263 & chain X & 3EMN ")
cmd.color ("magenta", "3EMN_X_S17")


cmd.select("3EMN_X_S18", "resi 274-283 & chain X & 3EMN ")
cmd.color ("red", "3EMN_X_S18")


cmd.select("3EMN_barrel", "3EMN_X_S*")
cmd.show("cartoon", "3EMN_barrel")
cmd.zoom("3EMN_barrel")
