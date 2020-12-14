from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1FEP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1FEP_A_S0", "resi 154-162 & chain A & 1FEP ")
cmd.color ("red", "1FEP_A_S0")


cmd.select("1FEP_A_S1", "resi 172-181 & chain A & 1FEP ")
cmd.color ("yellow", "1FEP_A_S1")


cmd.select("1FEP_A_S2", "resi 187-198 & chain A & 1FEP ")
cmd.color ("green", "1FEP_A_S2")


cmd.select("1FEP_A_S3", "resi 227-239 & chain A & 1FEP ")
cmd.color ("cyan", "1FEP_A_S3")


cmd.select("1FEP_A_S4", "resi 244-259 & chain A & 1FEP ")
cmd.color ("blue", "1FEP_A_S4")


cmd.select("1FEP_A_S5", "resi 282-297 & chain A & 1FEP ")
cmd.color ("magenta", "1FEP_A_S5")


cmd.select("1FEP_A_S6", "resi 301-316 & chain A & 1FEP ")
cmd.color ("red", "1FEP_A_S6")


cmd.select("1FEP_A_S7", "resi 338-355 & chain A & 1FEP ")
cmd.color ("yellow", "1FEP_A_S7")


cmd.select("1FEP_A_S8", "resi 361-376 & chain A & 1FEP ")
cmd.color ("green", "1FEP_A_S8")


cmd.select("1FEP_A_S9", "resi 403-420 & chain A & 1FEP ")
cmd.color ("cyan", "1FEP_A_S9")


cmd.select("1FEP_A_S10", "resi 424-436 & chain A & 1FEP ")
cmd.color ("blue", "1FEP_A_S10")


cmd.select("1FEP_A_S11", "resi 441-452 & chain A & 1FEP ")
cmd.color ("magenta", "1FEP_A_S11")


cmd.select("1FEP_A_S12", "resi 455-482 & chain A & 1FEP ")
cmd.color ("red", "1FEP_A_S12")


cmd.select("1FEP_A_S13", "resi 494-517 & chain A & 1FEP ")
cmd.color ("yellow", "1FEP_A_S13")


cmd.select("1FEP_A_S14", "resi 522-539 & chain A & 1FEP ")
cmd.color ("green", "1FEP_A_S14")


cmd.select("1FEP_A_S15", "resi 554-574 & chain A & 1FEP ")
cmd.color ("cyan", "1FEP_A_S15")


cmd.select("1FEP_A_S16", "resi 578-593 & chain A & 1FEP ")
cmd.color ("blue", "1FEP_A_S16")


cmd.select("1FEP_A_S17", "resi 605-615 & chain A & 1FEP ")
cmd.color ("magenta", "1FEP_A_S17")


cmd.select("1FEP_A_S18", "resi 619-631 & chain A & 1FEP ")
cmd.color ("red", "1FEP_A_S18")


cmd.select("1FEP_A_S19", "resi 651-665 & chain A & 1FEP ")
cmd.color ("yellow", "1FEP_A_S19")


cmd.select("1FEP_A_S20", "resi 668-694 & chain A & 1FEP ")
cmd.color ("green", "1FEP_A_S20")


cmd.select("1FEP_A_S21", "resi 699-723 & chain A & 1FEP ")
cmd.color ("cyan", "1FEP_A_S21")


cmd.select("1FEP_barrel", "1FEP_A_S*")
cmd.show("cartoon", "1FEP_barrel")
cmd.zoom("1FEP_barrel")
