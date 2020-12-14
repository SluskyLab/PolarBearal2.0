from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IV9.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5IV9_A_S0", "resi 208-212 & chain A & 5IV9 ")
cmd.color ("red", "5IV9_A_S0")


cmd.select("5IV9_A_S1", "resi 216-225 & chain A & 5IV9 ")
cmd.color ("yellow", "5IV9_A_S1")


cmd.select("5IV9_A_S2", "resi 232-240 & chain A & 5IV9 ")
cmd.color ("green", "5IV9_A_S2")


cmd.select("5IV9_A_S3", "resi 244-254 & chain A & 5IV9 ")
cmd.color ("cyan", "5IV9_A_S3")


cmd.select("5IV9_A_S4", "resi 260-274 & chain A & 5IV9 ")
cmd.color ("blue", "5IV9_A_S4")


cmd.select("5IV9_A_S5", "resi 278-295 & chain A & 5IV9 ")
cmd.color ("magenta", "5IV9_A_S5")


cmd.select("5IV9_A_S6", "resi 300-311 & chain A & 5IV9 ")
cmd.color ("red", "5IV9_A_S6")


cmd.select("5IV9_A_S7", "resi 331-340 & chain A & 5IV9 ")
cmd.color ("yellow", "5IV9_A_S7")


cmd.select("5IV9_A_S8", "resi 343-354 & chain A & 5IV9 ")
cmd.color ("green", "5IV9_A_S8")


cmd.select("5IV9_A_S9", "resi 365-376 & chain A & 5IV9 ")
cmd.color ("cyan", "5IV9_A_S9")


cmd.select("5IV9_A_S10", "resi 383-394 & chain A & 5IV9 ")
cmd.color ("blue", "5IV9_A_S10")


cmd.select("5IV9_A_S11", "resi 402-416 & chain A & 5IV9 ")
cmd.color ("magenta", "5IV9_A_S11")


cmd.select("5IV9_A_S12", "resi 420-437 & chain A & 5IV9 ")
cmd.color ("red", "5IV9_A_S12")


cmd.select("5IV9_A_S13", "resi 454-473 & chain A & 5IV9 ")
cmd.color ("yellow", "5IV9_A_S13")


cmd.select("5IV9_A_S14", "resi 477-490 & chain A & 5IV9 ")
cmd.color ("green", "5IV9_A_S14")


cmd.select("5IV9_A_S15", "resi 527-541 & chain A & 5IV9 ")
cmd.color ("cyan", "5IV9_A_S15")


cmd.select("5IV9_A_S16", "resi 545-562 & chain A & 5IV9 ")
cmd.color ("blue", "5IV9_A_S16")


cmd.select("5IV9_A_S17", "resi 577-587 & chain A & 5IV9 ")
cmd.color ("magenta", "5IV9_A_S17")


cmd.select("5IV9_A_S18", "resi 595-601 & chain A & 5IV9 ")
cmd.color ("red", "5IV9_A_S18")


cmd.select("5IV9_A_S19", "resi 609-617 & chain A & 5IV9 ")
cmd.color ("yellow", "5IV9_A_S19")


cmd.select("5IV9_A_S20", "resi 624-632 & chain A & 5IV9 ")
cmd.color ("green", "5IV9_A_S20")


cmd.select("5IV9_A_S21", "resi 654-662 & chain A & 5IV9 ")
cmd.color ("cyan", "5IV9_A_S21")


cmd.select("5IV9_A_S22", "resi 670-678 & chain A & 5IV9 ")
cmd.color ("blue", "5IV9_A_S22")


cmd.select("5IV9_A_S23", "resi 683-693 & chain A & 5IV9 ")
cmd.color ("magenta", "5IV9_A_S23")


cmd.select("5IV9_A_S24", "resi 699-712 & chain A & 5IV9 ")
cmd.color ("red", "5IV9_A_S24")


cmd.select("5IV9_A_S25", "resi 719-731 & chain A & 5IV9 ")
cmd.color ("yellow", "5IV9_A_S25")


cmd.select("5IV9_barrel", "5IV9_A_S*")
cmd.show("cartoon", "5IV9_barrel")
cmd.zoom("5IV9_barrel")
