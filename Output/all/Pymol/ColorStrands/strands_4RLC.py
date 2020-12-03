from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RLC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RLC_A_S0", "resi 6-16 & chain A & 4RLC ")
cmd.color ("red", "4RLC_A_S0")


cmd.select("4RLC_A_S1", "resi 27-37 & chain A & 4RLC ")
cmd.color ("yellow", "4RLC_A_S1")


cmd.select("4RLC_A_S2", "resi 40-51 & chain A & 4RLC ")
cmd.color ("green", "4RLC_A_S2")


cmd.select("4RLC_A_S3", "resi 65-76 & chain A & 4RLC ")
cmd.color ("cyan", "4RLC_A_S3")


cmd.select("4RLC_A_S4", "resi 85-99 & chain A & 4RLC ")
cmd.color ("blue", "4RLC_A_S4")


cmd.select("4RLC_A_S5", "resi 106-123 & chain A & 4RLC ")
cmd.color ("magenta", "4RLC_A_S5")


cmd.select("4RLC_A_S6", "resi 126-137 & chain A & 4RLC ")
cmd.color ("red", "4RLC_A_S6")


cmd.select("4RLC_A_S7", "resi 149-160 & chain A & 4RLC ")
cmd.color ("yellow", "4RLC_A_S7")


cmd.select("4RLC_barrel", "4RLC_A_S*")
cmd.show("cartoon", "4RLC_barrel")
cmd.zoom("4RLC_barrel")
