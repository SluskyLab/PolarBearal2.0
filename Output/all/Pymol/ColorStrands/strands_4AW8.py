from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AW8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4AW8_A_S0", "resi 111-113 & chain A & 4AW8 ")
cmd.color ("red", "4AW8_A_S0")


cmd.select("4AW8_A_S1", "resi 121-123 & chain A & 4AW8 ")
cmd.color ("yellow", "4AW8_A_S1")


cmd.select("4AW8_barrel", "4AW8_A_S*")
cmd.show("cartoon", "4AW8_barrel")
cmd.zoom("4AW8_barrel")
