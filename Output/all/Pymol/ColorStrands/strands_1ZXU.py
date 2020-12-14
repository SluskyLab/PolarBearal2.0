from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1ZXU.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1ZXU_A_S0", "resi 38-43 & chain A & 1ZXU ")
cmd.color ("red", "1ZXU_A_S0")


cmd.select("1ZXU_A_S1", "resi 54-57 & chain A & 1ZXU ")
cmd.color ("yellow", "1ZXU_A_S1")


cmd.select("1ZXU_A_S2", "resi 64-68 & chain A & 1ZXU ")
cmd.color ("green", "1ZXU_A_S2")


cmd.select("1ZXU_A_S3", "resi 78-81 & chain A & 1ZXU ")
cmd.color ("cyan", "1ZXU_A_S3")


cmd.select("1ZXU_A_S4", "resi 88-92 & chain A & 1ZXU ")
cmd.color ("blue", "1ZXU_A_S4")


cmd.select("1ZXU_A_S5", "resi 102-105 & chain A & 1ZXU ")
cmd.color ("magenta", "1ZXU_A_S5")


cmd.select("1ZXU_A_S6", "resi 116-120 & chain A & 1ZXU ")
cmd.color ("red", "1ZXU_A_S6")


cmd.select("1ZXU_A_S7", "resi 130-134 & chain A & 1ZXU ")
cmd.color ("yellow", "1ZXU_A_S7")


cmd.select("1ZXU_A_S8", "resi 145-151 & chain A & 1ZXU ")
cmd.color ("green", "1ZXU_A_S8")


cmd.select("1ZXU_A_S9", "resi 155-160 & chain A & 1ZXU ")
cmd.color ("cyan", "1ZXU_A_S9")


cmd.select("1ZXU_A_S10", "resi 168-174 & chain A & 1ZXU ")
cmd.color ("blue", "1ZXU_A_S10")


cmd.select("1ZXU_A_S11", "resi 186-191 & chain A & 1ZXU ")
cmd.color ("magenta", "1ZXU_A_S11")


cmd.select("1ZXU_barrel", "1ZXU_A_S*")
cmd.show("cartoon", "1ZXU_barrel")
cmd.zoom("1ZXU_barrel")
