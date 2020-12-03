from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IVA.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5IVA_A_S0", "resi 50-54 & chain A & 5IVA ")
cmd.color ("red", "5IVA_A_S0")


cmd.select("5IVA_A_S1", "resi 61-68 & chain A & 5IVA ")
cmd.color ("yellow", "5IVA_A_S1")


cmd.select("5IVA_A_S2", "resi 73-82 & chain A & 5IVA ")
cmd.color ("green", "5IVA_A_S2")


cmd.select("5IVA_A_S3", "resi 89-97 & chain A & 5IVA ")
cmd.color ("cyan", "5IVA_A_S3")


cmd.select("5IVA_A_S4", "resi 102-110 & chain A & 5IVA ")
cmd.color ("blue", "5IVA_A_S4")


cmd.select("5IVA_A_S5", "resi 127-136 & chain A & 5IVA ")
cmd.color ("magenta", "5IVA_A_S5")


cmd.select("5IVA_A_S6", "resi 141-152 & chain A & 5IVA ")
cmd.color ("red", "5IVA_A_S6")


cmd.select("5IVA_A_S7", "resi 172-181 & chain A & 5IVA ")
cmd.color ("yellow", "5IVA_A_S7")


cmd.select("5IVA_A_S8", "resi 184-195 & chain A & 5IVA ")
cmd.color ("green", "5IVA_A_S8")


cmd.select("5IVA_A_S9", "resi 206-217 & chain A & 5IVA ")
cmd.color ("cyan", "5IVA_A_S9")


cmd.select("5IVA_A_S10", "resi 225-246 & chain A & 5IVA ")
cmd.color ("blue", "5IVA_A_S10")


cmd.select("5IVA_A_S11", "resi 250-281 & chain A & 5IVA ")
cmd.color ("magenta", "5IVA_A_S11")


cmd.select("5IVA_A_S12", "resi 285-302 & chain A & 5IVA ")
cmd.color ("red", "5IVA_A_S12")


cmd.select("5IVA_A_S13", "resi 322-339 & chain A & 5IVA ")
cmd.color ("yellow", "5IVA_A_S13")


cmd.select("5IVA_A_S14", "resi 348-361 & chain A & 5IVA ")
cmd.color ("green", "5IVA_A_S14")


cmd.select("5IVA_A_S15", "resi 399-411 & chain A & 5IVA ")
cmd.color ("cyan", "5IVA_A_S15")


cmd.select("5IVA_A_S16", "resi 418-429 & chain A & 5IVA ")
cmd.color ("blue", "5IVA_A_S16")


cmd.select("5IVA_A_S17", "resi 461-471 & chain A & 5IVA ")
cmd.color ("magenta", "5IVA_A_S17")


cmd.select("5IVA_A_S18", "resi 475-484 & chain A & 5IVA ")
cmd.color ("red", "5IVA_A_S18")


cmd.select("5IVA_A_S19", "resi 489-499 & chain A & 5IVA ")
cmd.color ("yellow", "5IVA_A_S19")


cmd.select("5IVA_A_S20", "resi 508-523 & chain A & 5IVA ")
cmd.color ("green", "5IVA_A_S20")


cmd.select("5IVA_A_S21", "resi 528-547 & chain A & 5IVA ")
cmd.color ("cyan", "5IVA_A_S21")


cmd.select("5IVA_A_S22", "resi 552-562 & chain A & 5IVA ")
cmd.color ("blue", "5IVA_A_S22")


cmd.select("5IVA_A_S23", "resi 567-578 & chain A & 5IVA ")
cmd.color ("magenta", "5IVA_A_S23")


cmd.select("5IVA_A_S24", "resi 583-595 & chain A & 5IVA ")
cmd.color ("red", "5IVA_A_S24")


cmd.select("5IVA_A_S25", "resi 603-615 & chain A & 5IVA ")
cmd.color ("yellow", "5IVA_A_S25")


cmd.select("5IVA_barrel", "5IVA_A_S*")
cmd.show("cartoon", "5IVA_barrel")
cmd.zoom("5IVA_barrel")
