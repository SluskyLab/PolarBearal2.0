from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1TLY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1TLY_A_S0", "resi 14-24 & chain A & 1TLY ")
cmd.color ("red", "1TLY_A_S0")


cmd.select("1TLY_A_S1", "resi 32-43 & chain A & 1TLY ")
cmd.color ("yellow", "1TLY_A_S1")


cmd.select("1TLY_A_S2", "resi 49-56 & chain A & 1TLY ")
cmd.color ("green", "1TLY_A_S2")


cmd.select("1TLY_A_S3", "resi 76-86 & chain A & 1TLY ")
cmd.color ("cyan", "1TLY_A_S3")


cmd.select("1TLY_A_S4", "resi 100-112 & chain A & 1TLY ")
cmd.color ("blue", "1TLY_A_S4")


cmd.select("1TLY_A_S5", "resi 119-132 & chain A & 1TLY ")
cmd.color ("magenta", "1TLY_A_S5")


cmd.select("1TLY_A_S6", "resi 138-152 & chain A & 1TLY ")
cmd.color ("red", "1TLY_A_S6")


cmd.select("1TLY_A_S7", "resi 158-174 & chain A & 1TLY ")
cmd.color ("yellow", "1TLY_A_S7")


cmd.select("1TLY_A_S8", "resi 180-191 & chain A & 1TLY ")
cmd.color ("green", "1TLY_A_S8")


cmd.select("1TLY_A_S9", "resi 210-223 & chain A & 1TLY ")
cmd.color ("cyan", "1TLY_A_S9")


cmd.select("1TLY_A_S10", "resi 228-241 & chain A & 1TLY ")
cmd.color ("blue", "1TLY_A_S10")


cmd.select("1TLY_A_S11", "resi 261-272 & chain A & 1TLY ")
cmd.color ("magenta", "1TLY_A_S11")


cmd.select("1TLY_barrel", "1TLY_A_S*")
cmd.show("cartoon", "1TLY_barrel")
cmd.zoom("1TLY_barrel")
