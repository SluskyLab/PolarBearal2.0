from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Istrand0", "resi 13-19 & chain I ")
cmd.color ("red", "Istrand0")


cmd.select("Istrand1", "resi 25-35 & chain I ")
cmd.color ("green", "Istrand1")


cmd.select("Istrand2", "resi 40-45 & chain I ")
cmd.color ("orange", "Istrand2")


cmd.select("Istrand3", "resi 60-64 & chain I ")
cmd.color ("teal", "Istrand3")


cmd.select("Istrand4", "resi 67-71 & chain I ")
cmd.color ("yellow", "Istrand4")


cmd.select("Istrand5", "resi 77-85 & chain I ")
cmd.color ("blue", "Istrand5")


cmd.select("Istrand6", "resi 88-92 & chain I ")
cmd.color ("red", "Istrand6")


cmd.select("Istrand7", "resi 98-103 & chain I ")
cmd.color ("green", "Istrand7")


cmd.select("Pstrand8", "resi 55-61 & chain P ")
cmd.color ("orange", "Pstrand8")


cmd.select("Pstrand9", "resi 109-116 & chain P ")
cmd.color ("teal", "Pstrand9")


cmd.select("Pstrand10", "resi 122-127 & chain P ")
cmd.color ("yellow", "Pstrand10")


cmd.select("Pstrand11", "resi 135-137 & chain P ")
cmd.color ("blue", "Pstrand11")


cmd.select("Pstrand12", "resi 149-153 & chain P ")
cmd.color ("red", "Pstrand12")


cmd.select("Pstrand13", "resi 258-260 & chain P ")
cmd.color ("green", "Pstrand13")


cmd.select("Pstrand14", "resi 281-283 & chain P ")
cmd.color ("orange", "Pstrand14")


cmd.select("Pstrand15", "resi 291-293 & chain P ")
cmd.color ("teal", "Pstrand15")


cmd.select("Pstrand16", "resi 302-304 & chain P ")
cmd.color ("yellow", "Pstrand16")


cmd.select("Pstrand17", "resi 310-311 & chain P ")
cmd.color ("blue", "Pstrand17")


cmd.select("Pstrand18", "resi 320-322 & chain P ")
cmd.color ("red", "Pstrand18")


cmd.select("Pstrand19", "resi 330-332 & chain P ")
cmd.color ("green", "Pstrand19")


cmd.select("Pstrand20", "resi 339-341 & chain P ")
cmd.color ("orange", "Pstrand20")


cmd.select("Pstrand21", "resi 348-350 & chain P ")
cmd.color ("teal", "Pstrand21")


cmd.select("Pstrand22", "resi 357-359 & chain P ")
cmd.color ("yellow", "Pstrand22")


cmd.select("Pstrand23", "resi 366-368 & chain P ")
cmd.color ("blue", "Pstrand23")


cmd.select("Pstrand24", "resi 375-377 & chain P ")
cmd.color ("red", "Pstrand24")


cmd.select("Pstrand25", "resi 390-392 & chain P ")
cmd.color ("green", "Pstrand25")


cmd.select("Pstrand26", "resi 401-403 & chain P ")
cmd.color ("orange", "Pstrand26")


cmd.select("Pstrand27", "resi 418-419 & chain P ")
cmd.color ("teal", "Pstrand27")


cmd.select("Pstrand28", "resi 429-435 & chain P ")
cmd.color ("yellow", "Pstrand28")


cmd.select("Pstrand29", "resi 440-446 & chain P ")
cmd.color ("blue", "Pstrand29")


cmd.select("Pstrand30", "resi 455-460 & chain P ")
cmd.color ("red", "Pstrand30")


cmd.select("Pstrand31", "resi 468-469 & chain P ")
cmd.color ("green", "Pstrand31")


cmd.select("barrel", "Istrand* or Pstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
