from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FR2.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2FR2_A_S0", "resi 17-26 & chain A & 2FR2 ")
cmd.color ("red", "2FR2_A_S0")


cmd.select("2FR2_A_S1", "resi 33-42 & chain A & 2FR2 ")
cmd.color ("yellow", "2FR2_A_S1")


cmd.select("2FR2_A_S2", "resi 47-56 & chain A & 2FR2 ")
cmd.color ("green", "2FR2_A_S2")


cmd.select("2FR2_A_S3", "resi 64-73 & chain A & 2FR2 ")
cmd.color ("cyan", "2FR2_A_S3")


cmd.select("2FR2_A_S4", "resi 77-85 & chain A & 2FR2 ")
cmd.color ("blue", "2FR2_A_S4")


cmd.select("2FR2_A_S5", "resi 89-98 & chain A & 2FR2 ")
cmd.color ("magenta", "2FR2_A_S5")


cmd.select("2FR2_A_S6", "resi 104-117 & chain A & 2FR2 ")
cmd.color ("red", "2FR2_A_S6")


cmd.select("2FR2_A_S7", "resi 126-134 & chain A & 2FR2 ")
cmd.color ("yellow", "2FR2_A_S7")


cmd.select("2FR2_A_S8", "resi 139-146 & chain A & 2FR2 ")
cmd.color ("green", "2FR2_A_S8")


cmd.select("2FR2_A_S9", "resi 155-163 & chain A & 2FR2 ")
cmd.color ("cyan", "2FR2_A_S9")


cmd.select("2FR2_barrel", "2FR2_A_S*")
cmd.show("cartoon", "2FR2_barrel")
cmd.zoom("2FR2_barrel")
