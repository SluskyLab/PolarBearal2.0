from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2H5O.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2H5O_A_S0", "resi 40-95 & chain A & 2H5O ")
cmd.color ("red", "2H5O_A_S0")


cmd.select("2H5O_A_S1", "resi 104-113 & chain A & 2H5O ")
cmd.color ("yellow", "2H5O_A_S1")


cmd.select("2H5O_A_S2", "resi 127-149 & chain A & 2H5O ")
cmd.color ("green", "2H5O_A_S2")


cmd.select("2H5O_A_S3", "resi 157-160 & chain A & 2H5O ")
cmd.color ("cyan", "2H5O_A_S3")


cmd.select("2H5O_A_S4", "resi 179-194 & chain A & 2H5O ")
cmd.color ("blue", "2H5O_A_S4")


cmd.select("2H5O_A_S5", "resi 210-218 & chain A & 2H5O ")
cmd.color ("magenta", "2H5O_A_S5")


cmd.select("2H5O_barrel", "2H5O_A_S*")
cmd.show("cartoon", "2H5O_barrel")
cmd.zoom("2H5O_barrel")
