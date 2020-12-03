from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3GP6.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3GP6_A_S0", "resi 21-32 & chain A & 3GP6 ")
cmd.color ("red", "3GP6_A_S0")


cmd.select("3GP6_A_S1", "resi 53-59 & chain A & 3GP6 ")
cmd.color ("yellow", "3GP6_A_S1")


cmd.select("3GP6_A_S2", "resi 66-76 & chain A & 3GP6 ")
cmd.color ("green", "3GP6_A_S2")


cmd.select("3GP6_A_S3", "resi 80-93 & chain A & 3GP6 ")
cmd.color ("cyan", "3GP6_A_S3")


cmd.select("3GP6_A_S4", "resi 102-114 & chain A & 3GP6 ")
cmd.color ("blue", "3GP6_A_S4")


cmd.select("3GP6_A_S5", "resi 119-132 & chain A & 3GP6 ")
cmd.color ("magenta", "3GP6_A_S5")


cmd.select("3GP6_A_S6", "resi 137-143 & chain A & 3GP6 ")
cmd.color ("red", "3GP6_A_S6")


cmd.select("3GP6_A_S7", "resi 152-161 & chain A & 3GP6 ")
cmd.color ("yellow", "3GP6_A_S7")


cmd.select("3GP6_barrel", "3GP6_A_S*")
cmd.show("cartoon", "3GP6_barrel")
cmd.zoom("3GP6_barrel")
