from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1I78.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1I78_A_S0", "resi 8-31 & chain A & 1I78 ")
cmd.color ("red", "1I78_A_S0")


cmd.select("1I78_A_S1", "resi 39-60 & chain A & 1I78 ")
cmd.color ("yellow", "1I78_A_S1")


cmd.select("1I78_A_S2", "resi 65-86 & chain A & 1I78 ")
cmd.color ("green", "1I78_A_S2")


cmd.select("1I78_A_S3", "resi 96-121 & chain A & 1I78 ")
cmd.color ("cyan", "1I78_A_S3")


cmd.select("1I78_A_S4", "resi 125-149 & chain A & 1I78 ")
cmd.color ("blue", "1I78_A_S4")


cmd.select("1I78_A_S5", "resi 169-188 & chain A & 1I78 ")
cmd.color ("magenta", "1I78_A_S5")


cmd.select("1I78_A_S6", "resi 193-212 & chain A & 1I78 ")
cmd.color ("red", "1I78_A_S6")


cmd.select("1I78_A_S7", "resi 219-241 & chain A & 1I78 ")
cmd.color ("yellow", "1I78_A_S7")


cmd.select("1I78_A_S8", "resi 245-267 & chain A & 1I78 ")
cmd.color ("green", "1I78_A_S8")


cmd.select("1I78_A_S9", "resi 272-297 & chain A & 1I78 ")
cmd.color ("cyan", "1I78_A_S9")


cmd.select("1I78_barrel", "1I78_A_S*")
cmd.show("cartoon", "1I78_barrel")
cmd.zoom("1I78_barrel")
