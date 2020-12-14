from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2ICR_A_S0", "resi 42-95 & chain A & 2ICR ")
cmd.color ("red", "2ICR_A_S0")


cmd.select("2ICR_A_S1", "resi 104-113 & chain A & 2ICR ")
cmd.color ("yellow", "2ICR_A_S1")


cmd.select("2ICR_A_S2", "resi 119-155 & chain A & 2ICR ")
cmd.color ("green", "2ICR_A_S2")


cmd.select("2ICR_A_S3", "resi 160-170 & chain A & 2ICR ")
cmd.color ("cyan", "2ICR_A_S3")


cmd.select("2ICR_A_S4", "resi 183-201 & chain A & 2ICR ")
cmd.color ("blue", "2ICR_A_S4")


cmd.select("2ICR_A_S5", "resi 216-224 & chain A & 2ICR ")
cmd.color ("magenta", "2ICR_A_S5")


cmd.select("2ICR_barrel", "2ICR_A_S*")
cmd.show("cartoon", "2ICR_barrel")
cmd.zoom("2ICR_barrel")
