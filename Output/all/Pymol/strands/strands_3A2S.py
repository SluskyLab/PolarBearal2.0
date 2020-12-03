from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 2-19 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 23-23 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 30-37 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 42-49 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 55-66 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 71-74 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 77-85 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 89-95 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 107-111 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 120-121 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 128-137 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 140-141 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 144-151 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 157-157 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 163-166 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 171-180 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("Xstrand16", "resi 184-198 & chain X ")
cmd.color ("yellow", "Xstrand16")


cmd.select("Xstrand17", "resi 202-204 & chain X ")
cmd.color ("blue", "Xstrand17")


cmd.select("Xstrand18", "resi 212-228 & chain X ")
cmd.color ("red", "Xstrand18")


cmd.select("Xstrand19", "resi 231-243 & chain X ")
cmd.color ("green", "Xstrand19")


cmd.select("Xstrand20", "resi 246-248 & chain X ")
cmd.color ("orange", "Xstrand20")


cmd.select("Xstrand21", "resi 254-268 & chain X ")
cmd.color ("teal", "Xstrand21")


cmd.select("Xstrand22", "resi 271-280 & chain X ")
cmd.color ("yellow", "Xstrand22")


cmd.select("Xstrand23", "resi 284-285 & chain X ")
cmd.color ("blue", "Xstrand23")


cmd.select("Xstrand24", "resi 288-290 & chain X ")
cmd.color ("red", "Xstrand24")


cmd.select("Xstrand25", "resi 295-307 & chain X ")
cmd.color ("green", "Xstrand25")


cmd.select("Xstrand26", "resi 310-323 & chain X ")
cmd.color ("orange", "Xstrand26")


cmd.select("Xstrand27", "resi 328-340 & chain X ")
cmd.color ("teal", "Xstrand27")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
