from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3V8X.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3V8X_A_S0", "resi 187-197 & chain A & 3V8X ")
cmd.color ("red", "3V8X_A_S0")


cmd.select("3V8X_A_S1", "resi 200-212 & chain A & 3V8X ")
cmd.color ("yellow", "3V8X_A_S1")


cmd.select("3V8X_A_S2", "resi 218-249 & chain A & 3V8X ")
cmd.color ("green", "3V8X_A_S2")


cmd.select("3V8X_A_S3", "resi 281-320 & chain A & 3V8X ")
cmd.color ("cyan", "3V8X_A_S3")


cmd.select("3V8X_A_S4", "resi 325-342 & chain A & 3V8X ")
cmd.color ("blue", "3V8X_A_S4")


cmd.select("3V8X_A_S5", "resi 394-416 & chain A & 3V8X ")
cmd.color ("magenta", "3V8X_A_S5")


cmd.select("3V8X_A_S6", "resi 424-445 & chain A & 3V8X ")
cmd.color ("red", "3V8X_A_S6")


cmd.select("3V8X_A_S7", "resi 463-488 & chain A & 3V8X ")
cmd.color ("yellow", "3V8X_A_S7")


cmd.select("3V8X_A_S8", "resi 495-527 & chain A & 3V8X ")
cmd.color ("green", "3V8X_A_S8")


cmd.select("3V8X_A_S9", "resi 548-592 & chain A & 3V8X ")
cmd.color ("cyan", "3V8X_A_S9")


cmd.select("3V8X_A_S10", "resi 595-610 & chain A & 3V8X ")
cmd.color ("blue", "3V8X_A_S10")


cmd.select("3V8X_A_S11", "resi 619-633 & chain A & 3V8X ")
cmd.color ("magenta", "3V8X_A_S11")


cmd.select("3V8X_A_S12", "resi 637-649 & chain A & 3V8X ")
cmd.color ("red", "3V8X_A_S12")


cmd.select("3V8X_A_S13", "resi 673-685 & chain A & 3V8X ")
cmd.color ("yellow", "3V8X_A_S13")


cmd.select("3V8X_A_S14", "resi 690-707 & chain A & 3V8X ")
cmd.color ("green", "3V8X_A_S14")


cmd.select("3V8X_A_S15", "resi 720-742 & chain A & 3V8X ")
cmd.color ("cyan", "3V8X_A_S15")


cmd.select("3V8X_A_S16", "resi 756-770 & chain A & 3V8X ")
cmd.color ("blue", "3V8X_A_S16")


cmd.select("3V8X_A_S17", "resi 790-799 & chain A & 3V8X ")
cmd.color ("magenta", "3V8X_A_S17")


cmd.select("3V8X_A_S18", "resi 803-827 & chain A & 3V8X ")
cmd.color ("red", "3V8X_A_S18")


cmd.select("3V8X_A_S19", "resi 833-856 & chain A & 3V8X ")
cmd.color ("yellow", "3V8X_A_S19")


cmd.select("3V8X_A_S20", "resi 859-874 & chain A & 3V8X ")
cmd.color ("green", "3V8X_A_S20")


cmd.select("3V8X_A_S21", "resi 902-914 & chain A & 3V8X ")
cmd.color ("cyan", "3V8X_A_S21")


cmd.select("3V8X_barrel", "3V8X_A_S*")
cmd.show("cartoon", "3V8X_barrel")
cmd.zoom("3V8X_barrel")
