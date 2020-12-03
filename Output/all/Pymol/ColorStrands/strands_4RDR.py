from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RDR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RDR_A_S0", "resi 149-157 & chain A & 4RDR ")
cmd.color ("red", "4RDR_A_S0")


cmd.select("4RDR_A_S1", "resi 162-173 & chain A & 4RDR ")
cmd.color ("yellow", "4RDR_A_S1")


cmd.select("4RDR_A_S2", "resi 177-188 & chain A & 4RDR ")
cmd.color ("green", "4RDR_A_S2")


cmd.select("4RDR_A_S3", "resi 207-218 & chain A & 4RDR ")
cmd.color ("cyan", "4RDR_A_S3")


cmd.select("4RDR_A_S4", "resi 225-251 & chain A & 4RDR ")
cmd.color ("blue", "4RDR_A_S4")


cmd.select("4RDR_A_S5", "resi 284-317 & chain A & 4RDR ")
cmd.color ("magenta", "4RDR_A_S5")


cmd.select("4RDR_A_S6", "resi 325-341 & chain A & 4RDR ")
cmd.color ("red", "4RDR_A_S6")


cmd.select("4RDR_A_S7", "resi 348-363 & chain A & 4RDR ")
cmd.color ("yellow", "4RDR_A_S7")


cmd.select("4RDR_A_S8", "resi 368-385 & chain A & 4RDR ")
cmd.color ("green", "4RDR_A_S8")


cmd.select("4RDR_A_S9", "resi 397-414 & chain A & 4RDR ")
cmd.color ("cyan", "4RDR_A_S9")


cmd.select("4RDR_A_S10", "resi 419-432 & chain A & 4RDR ")
cmd.color ("blue", "4RDR_A_S10")


cmd.select("4RDR_A_S11", "resi 456-469 & chain A & 4RDR ")
cmd.color ("magenta", "4RDR_A_S11")


cmd.select("4RDR_A_S12", "resi 474-497 & chain A & 4RDR ")
cmd.color ("red", "4RDR_A_S12")


cmd.select("4RDR_A_S13", "resi 505-527 & chain A & 4RDR ")
cmd.color ("yellow", "4RDR_A_S13")


cmd.select("4RDR_A_S14", "resi 530-567 & chain A & 4RDR ")
cmd.color ("green", "4RDR_A_S14")


cmd.select("4RDR_A_S15", "resi 570-588 & chain A & 4RDR ")
cmd.color ("cyan", "4RDR_A_S15")


cmd.select("4RDR_A_S16", "resi 594-606 & chain A & 4RDR ")
cmd.color ("blue", "4RDR_A_S16")


cmd.select("4RDR_A_S17", "resi 630-648 & chain A & 4RDR ")
cmd.color ("magenta", "4RDR_A_S17")


cmd.select("4RDR_A_S18", "resi 651-664 & chain A & 4RDR ")
cmd.color ("red", "4RDR_A_S18")


cmd.select("4RDR_A_S19", "resi 674-688 & chain A & 4RDR ")
cmd.color ("yellow", "4RDR_A_S19")


cmd.select("4RDR_A_S20", "resi 695-704 & chain A & 4RDR ")
cmd.color ("green", "4RDR_A_S20")


cmd.select("4RDR_A_S21", "resi 725-731 & chain A & 4RDR ")
cmd.color ("cyan", "4RDR_A_S21")


cmd.select("4RDR_barrel", "4RDR_A_S*")
cmd.show("cartoon", "4RDR_barrel")
cmd.zoom("4RDR_barrel")
