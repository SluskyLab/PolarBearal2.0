from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GL4.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1GL4_A_S0", "resi 441-492 & chain A & 1GL4 ")
cmd.color ("red", "1GL4_A_S0")


cmd.select("1GL4_A_S1", "resi 500-509 & chain A & 1GL4 ")
cmd.color ("yellow", "1GL4_A_S1")


cmd.select("1GL4_A_S2", "resi 517-525 & chain A & 1GL4 ")
cmd.color ("green", "1GL4_A_S2")


cmd.select("1GL4_A_S3", "resi 549-561 & chain A & 1GL4 ")
cmd.color ("cyan", "1GL4_A_S3")


cmd.select("1GL4_A_S4", "resi 577-585 & chain A & 1GL4 ")
cmd.color ("blue", "1GL4_A_S4")


cmd.select("1GL4_A_S5", "resi 617-628 & chain A & 1GL4 ")
cmd.color ("magenta", "1GL4_A_S5")


cmd.select("1GL4_barrel", "1GL4_A_S*")
cmd.show("cartoon", "1GL4_barrel")
cmd.zoom("1GL4_barrel")
