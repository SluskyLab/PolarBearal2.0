from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1S.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4E1S_A_S0", "resi 212-219 & chain A & 4E1S ")
cmd.color ("red", "4E1S_A_S0")


cmd.select("4E1S_A_S1", "resi 225-235 & chain A & 4E1S ")
cmd.color ("yellow", "4E1S_A_S1")


cmd.select("4E1S_A_S2", "resi 239-250 & chain A & 4E1S ")
cmd.color ("green", "4E1S_A_S2")


cmd.select("4E1S_A_S3", "resi 256-266 & chain A & 4E1S ")
cmd.color ("cyan", "4E1S_A_S3")


cmd.select("4E1S_A_S4", "resi 271-281 & chain A & 4E1S ")
cmd.color ("blue", "4E1S_A_S4")


cmd.select("4E1S_A_S5", "resi 286-296 & chain A & 4E1S ")
cmd.color ("magenta", "4E1S_A_S5")


cmd.select("4E1S_A_S6", "resi 299-314 & chain A & 4E1S ")
cmd.color ("red", "4E1S_A_S6")


cmd.select("4E1S_A_S7", "resi 322-337 & chain A & 4E1S ")
cmd.color ("yellow", "4E1S_A_S7")


cmd.select("4E1S_A_S8", "resi 343-355 & chain A & 4E1S ")
cmd.color ("green", "4E1S_A_S8")


cmd.select("4E1S_A_S9", "resi 367-380 & chain A & 4E1S ")
cmd.color ("cyan", "4E1S_A_S9")


cmd.select("4E1S_A_S10", "resi 384-395 & chain A & 4E1S ")
cmd.color ("blue", "4E1S_A_S10")


cmd.select("4E1S_A_S11", "resi 398-409 & chain A & 4E1S ")
cmd.color ("magenta", "4E1S_A_S11")


cmd.select("4E1S_barrel", "4E1S_A_S*")
cmd.show("cartoon", "4E1S_barrel")
cmd.zoom("4E1S_barrel")
