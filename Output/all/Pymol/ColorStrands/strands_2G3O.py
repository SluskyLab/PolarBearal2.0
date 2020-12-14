from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2G3O.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2G3O_A_S0", "resi 34-87 & chain A & 2G3O ")
cmd.color ("red", "2G3O_A_S0")


cmd.select("2G3O_A_S1", "resi 96-104 & chain A & 2G3O ")
cmd.color ("yellow", "2G3O_A_S1")


cmd.select("2G3O_A_S2", "resi 111-145 & chain A & 2G3O ")
cmd.color ("green", "2G3O_A_S2")


cmd.select("2G3O_A_S3", "resi 149-159 & chain A & 2G3O ")
cmd.color ("cyan", "2G3O_A_S3")


cmd.select("2G3O_A_S4", "resi 172-198 & chain A & 2G3O ")
cmd.color ("blue", "2G3O_A_S4")


cmd.select("2G3O_A_S5", "resi 208-213 & chain A & 2G3O ")
cmd.color ("magenta", "2G3O_A_S5")


cmd.select("2G3O_barrel", "2G3O_A_S*")
cmd.show("cartoon", "2G3O_barrel")
cmd.zoom("2G3O_barrel")
