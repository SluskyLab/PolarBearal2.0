from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3KVN_X_S0", "resi 348-360 & chain X & 3KVN ")
cmd.color ("red", "3KVN_X_S0")


cmd.select("3KVN_X_S1", "resi 369-384 & chain X & 3KVN ")
cmd.color ("yellow", "3KVN_X_S1")


cmd.select("3KVN_X_S2", "resi 387-403 & chain X & 3KVN ")
cmd.color ("green", "3KVN_X_S2")


cmd.select("3KVN_X_S3", "resi 408-424 & chain X & 3KVN ")
cmd.color ("cyan", "3KVN_X_S3")


cmd.select("3KVN_X_S4", "resi 429-448 & chain X & 3KVN ")
cmd.color ("blue", "3KVN_X_S4")


cmd.select("3KVN_X_S5", "resi 455-476 & chain X & 3KVN ")
cmd.color ("magenta", "3KVN_X_S5")


cmd.select("3KVN_X_S6", "resi 485-505 & chain X & 3KVN ")
cmd.color ("red", "3KVN_X_S6")


cmd.select("3KVN_X_S7", "resi 512-534 & chain X & 3KVN ")
cmd.color ("yellow", "3KVN_X_S7")


cmd.select("3KVN_X_S8", "resi 538-560 & chain X & 3KVN ")
cmd.color ("green", "3KVN_X_S8")


cmd.select("3KVN_X_S9", "resi 569-591 & chain X & 3KVN ")
cmd.color ("cyan", "3KVN_X_S9")


cmd.select("3KVN_X_S10", "resi 594-605 & chain X & 3KVN ")
cmd.color ("blue", "3KVN_X_S10")


cmd.select("3KVN_X_S11", "resi 611-621 & chain X & 3KVN ")
cmd.color ("magenta", "3KVN_X_S11")


cmd.select("3KVN_barrel", "3KVN_X_S*")
cmd.show("cartoon", "3KVN_barrel")
cmd.zoom("3KVN_barrel")
