from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2N93.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2N93_A_S0", "resi 6-14 & chain A & 2N93 ")
cmd.color ("red", "2N93_A_S0")


cmd.select("2N93_A_S1", "resi 42-43 & chain A & 2N93 ")
cmd.color ("yellow", "2N93_A_S1")


cmd.select("2N93_A_S2", "resi 50-53 & chain A & 2N93 ")
cmd.color ("green", "2N93_A_S2")


cmd.select("2N93_A_S3", "resi 61-69 & chain A & 2N93 ")
cmd.color ("cyan", "2N93_A_S3")


cmd.select("2N93_A_S4", "resi 78-83 & chain A & 2N93 ")
cmd.color ("blue", "2N93_A_S4")


cmd.select("2N93_A_S5", "resi 89-94 & chain A & 2N93 ")
cmd.color ("magenta", "2N93_A_S5")


cmd.select("2N93_A_S6", "resi 101-106 & chain A & 2N93 ")
cmd.color ("red", "2N93_A_S6")


cmd.select("2N93_A_S7", "resi 113-117 & chain A & 2N93 ")
cmd.color ("yellow", "2N93_A_S7")


cmd.select("2N93_A_S8", "resi 123-130 & chain A & 2N93 ")
cmd.color ("green", "2N93_A_S8")


cmd.select("2N93_barrel", "2N93_A_S*")
cmd.show("cartoon", "2N93_barrel")
cmd.zoom("2N93_barrel")
