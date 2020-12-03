from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QLB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3QLB_A_S0", "resi 162-168 & chain A & 3QLB ")
cmd.color ("red", "3QLB_A_S0")


cmd.select("3QLB_A_S1", "resi 175-183 & chain A & 3QLB ")
cmd.color ("yellow", "3QLB_A_S1")


cmd.select("3QLB_A_S2", "resi 190-202 & chain A & 3QLB ")
cmd.color ("green", "3QLB_A_S2")


cmd.select("3QLB_A_S3", "resi 211-223 & chain A & 3QLB ")
cmd.color ("cyan", "3QLB_A_S3")


cmd.select("3QLB_A_S4", "resi 229-241 & chain A & 3QLB ")
cmd.color ("blue", "3QLB_A_S4")


cmd.select("3QLB_A_S5", "resi 274-288 & chain A & 3QLB ")
cmd.color ("magenta", "3QLB_A_S5")


cmd.select("3QLB_A_S6", "resi 293-318 & chain A & 3QLB ")
cmd.color ("red", "3QLB_A_S6")


cmd.select("3QLB_A_S7", "resi 323-347 & chain A & 3QLB ")
cmd.color ("yellow", "3QLB_A_S7")


cmd.select("3QLB_A_S8", "resi 354-376 & chain A & 3QLB ")
cmd.color ("green", "3QLB_A_S8")


cmd.select("3QLB_A_S9", "resi 395-422 & chain A & 3QLB ")
cmd.color ("cyan", "3QLB_A_S9")


cmd.select("3QLB_A_S10", "resi 426-443 & chain A & 3QLB ")
cmd.color ("blue", "3QLB_A_S10")


cmd.select("3QLB_A_S11", "resi 448-465 & chain A & 3QLB ")
cmd.color ("magenta", "3QLB_A_S11")


cmd.select("3QLB_A_S12", "resi 470-482 & chain A & 3QLB ")
cmd.color ("red", "3QLB_A_S12")


cmd.select("3QLB_A_S13", "resi 497-509 & chain A & 3QLB ")
cmd.color ("yellow", "3QLB_A_S13")


cmd.select("3QLB_A_S14", "resi 514-533 & chain A & 3QLB ")
cmd.color ("green", "3QLB_A_S14")


cmd.select("3QLB_A_S15", "resi 539-558 & chain A & 3QLB ")
cmd.color ("cyan", "3QLB_A_S15")


cmd.select("3QLB_A_S16", "resi 562-577 & chain A & 3QLB ")
cmd.color ("blue", "3QLB_A_S16")


cmd.select("3QLB_A_S17", "resi 591-604 & chain A & 3QLB ")
cmd.color ("magenta", "3QLB_A_S17")


cmd.select("3QLB_A_S18", "resi 614-627 & chain A & 3QLB ")
cmd.color ("red", "3QLB_A_S18")


cmd.select("3QLB_A_S19", "resi 633-647 & chain A & 3QLB ")
cmd.color ("yellow", "3QLB_A_S19")


cmd.select("3QLB_A_S20", "resi 658-676 & chain A & 3QLB ")
cmd.color ("green", "3QLB_A_S20")


cmd.select("3QLB_A_S21", "resi 683-697 & chain A & 3QLB ")
cmd.color ("cyan", "3QLB_A_S21")


cmd.select("3QLB_barrel", "3QLB_A_S*")
cmd.show("cartoon", "3QLB_barrel")
cmd.zoom("3QLB_barrel")
