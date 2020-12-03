from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AFK.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4AFK_A_S0", "resi 43-54 & chain A & 4AFK ")
cmd.color ("red", "4AFK_A_S0")


cmd.select("4AFK_A_S1", "resi 66-79 & chain A & 4AFK ")
cmd.color ("yellow", "4AFK_A_S1")


cmd.select("4AFK_A_S2", "resi 85-96 & chain A & 4AFK ")
cmd.color ("green", "4AFK_A_S2")


cmd.select("4AFK_A_S3", "resi 123-135 & chain A & 4AFK ")
cmd.color ("cyan", "4AFK_A_S3")


cmd.select("4AFK_A_S4", "resi 145-150 & chain A & 4AFK ")
cmd.color ("blue", "4AFK_A_S4")


cmd.select("4AFK_A_S5", "resi 166-172 & chain A & 4AFK ")
cmd.color ("magenta", "4AFK_A_S5")


cmd.select("4AFK_A_S6", "resi 178-185 & chain A & 4AFK ")
cmd.color ("red", "4AFK_A_S6")


cmd.select("4AFK_A_S7", "resi 205-215 & chain A & 4AFK ")
cmd.color ("yellow", "4AFK_A_S7")


cmd.select("4AFK_A_S8", "resi 219-230 & chain A & 4AFK ")
cmd.color ("green", "4AFK_A_S8")


cmd.select("4AFK_A_S9", "resi 249-261 & chain A & 4AFK ")
cmd.color ("cyan", "4AFK_A_S9")


cmd.select("4AFK_A_S10", "resi 273-291 & chain A & 4AFK ")
cmd.color ("blue", "4AFK_A_S10")


cmd.select("4AFK_A_S11", "resi 300-318 & chain A & 4AFK ")
cmd.color ("magenta", "4AFK_A_S11")


cmd.select("4AFK_A_S12", "resi 323-334 & chain A & 4AFK ")
cmd.color ("red", "4AFK_A_S12")


cmd.select("4AFK_A_S13", "resi 376-388 & chain A & 4AFK ")
cmd.color ("yellow", "4AFK_A_S13")


cmd.select("4AFK_A_S14", "resi 392-402 & chain A & 4AFK ")
cmd.color ("green", "4AFK_A_S14")


cmd.select("4AFK_A_S15", "resi 426-436 & chain A & 4AFK ")
cmd.color ("cyan", "4AFK_A_S15")


cmd.select("4AFK_A_S16", "resi 457-466 & chain A & 4AFK ")
cmd.color ("blue", "4AFK_A_S16")


cmd.select("4AFK_A_S17", "resi 479-490 & chain A & 4AFK ")
cmd.color ("magenta", "4AFK_A_S17")


cmd.select("4AFK_barrel", "4AFK_A_S*")
cmd.show("cartoon", "4AFK_barrel")
cmd.zoom("4AFK_barrel")
