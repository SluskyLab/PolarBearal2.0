from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6E4V.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6E4V_A_S0", "resi 191-199 & chain A & 6E4V ")
cmd.color ("red", "6E4V_A_S0")


cmd.select("6E4V_A_S1", "resi 201-212 & chain A & 6E4V ")
cmd.color ("yellow", "6E4V_A_S1")


cmd.select("6E4V_A_S2", "resi 220-232 & chain A & 6E4V ")
cmd.color ("green", "6E4V_A_S2")


cmd.select("6E4V_A_S3", "resi 239-253 & chain A & 6E4V ")
cmd.color ("cyan", "6E4V_A_S3")


cmd.select("6E4V_A_S4", "resi 257-271 & chain A & 6E4V ")
cmd.color ("blue", "6E4V_A_S4")


cmd.select("6E4V_A_S5", "resi 283-316 & chain A & 6E4V ")
cmd.color ("magenta", "6E4V_A_S5")


cmd.select("6E4V_A_S6", "resi 323-346 & chain A & 6E4V ")
cmd.color ("red", "6E4V_A_S6")


cmd.select("6E4V_A_S7", "resi 367-390 & chain A & 6E4V ")
cmd.color ("yellow", "6E4V_A_S7")


cmd.select("6E4V_A_S8", "resi 397-419 & chain A & 6E4V ")
cmd.color ("green", "6E4V_A_S8")


cmd.select("6E4V_A_S9", "resi 443-463 & chain A & 6E4V ")
cmd.color ("cyan", "6E4V_A_S9")


cmd.select("6E4V_A_S10", "resi 467-481 & chain A & 6E4V ")
cmd.color ("blue", "6E4V_A_S10")


cmd.select("6E4V_A_S11", "resi 487-502 & chain A & 6E4V ")
cmd.color ("magenta", "6E4V_A_S11")


cmd.select("6E4V_A_S12", "resi 505-521 & chain A & 6E4V ")
cmd.color ("red", "6E4V_A_S12")


cmd.select("6E4V_A_S13", "resi 529-545 & chain A & 6E4V ")
cmd.color ("yellow", "6E4V_A_S13")


cmd.select("6E4V_A_S14", "resi 549-570 & chain A & 6E4V ")
cmd.color ("green", "6E4V_A_S14")


cmd.select("6E4V_A_S15", "resi 580-600 & chain A & 6E4V ")
cmd.color ("cyan", "6E4V_A_S15")


cmd.select("6E4V_A_S16", "resi 604-616 & chain A & 6E4V ")
cmd.color ("blue", "6E4V_A_S16")


cmd.select("6E4V_A_S17", "resi 625-640 & chain A & 6E4V ")
cmd.color ("magenta", "6E4V_A_S17")


cmd.select("6E4V_A_S18", "resi 646-662 & chain A & 6E4V ")
cmd.color ("red", "6E4V_A_S18")


cmd.select("6E4V_A_S19", "resi 669-685 & chain A & 6E4V ")
cmd.color ("yellow", "6E4V_A_S19")


cmd.select("6E4V_A_S20", "resi 690-705 & chain A & 6E4V ")
cmd.color ("green", "6E4V_A_S20")


cmd.select("6E4V_A_S21", "resi 714-728 & chain A & 6E4V ")
cmd.color ("cyan", "6E4V_A_S21")


cmd.select("6E4V_barrel", "6E4V_A_S*")
cmd.show("cartoon", "6E4V_barrel")
cmd.zoom("6E4V_barrel")
