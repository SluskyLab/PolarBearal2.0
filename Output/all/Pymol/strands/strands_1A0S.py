from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A0S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Pstrand0", "resi 73-86 & chain P ")
cmd.color ("red", "Pstrand0")


cmd.select("Pstrand1", "resi 117-128 & chain P ")
cmd.color ("green", "Pstrand1")


cmd.select("Pstrand2", "resi 134-145 & chain P ")
cmd.color ("orange", "Pstrand2")


cmd.select("Pstrand3", "resi 159-168 & chain P ")
cmd.color ("teal", "Pstrand3")


cmd.select("Pstrand4", "resi 181-188 & chain P ")
cmd.color ("yellow", "Pstrand4")


cmd.select("Pstrand5", "resi 193-195 & chain P ")
cmd.color ("blue", "Pstrand5")


cmd.select("Pstrand6", "resi 200-203 & chain P ")
cmd.color ("red", "Pstrand6")


cmd.select("Pstrand7", "resi 206-217 & chain P ")
cmd.color ("green", "Pstrand7")


cmd.select("Pstrand8", "resi 221-233 & chain P ")
cmd.color ("orange", "Pstrand8")


cmd.select("Pstrand9", "resi 241-253 & chain P ")
cmd.color ("teal", "Pstrand9")


cmd.select("Pstrand10", "resi 256-264 & chain P ")
cmd.color ("yellow", "Pstrand10")


cmd.select("Pstrand11", "resi 286-296 & chain P ")
cmd.color ("blue", "Pstrand11")


cmd.select("Pstrand12", "resi 306-316 & chain P ")
cmd.color ("red", "Pstrand12")


cmd.select("Pstrand13", "resi 335-344 & chain P ")
cmd.color ("green", "Pstrand13")


cmd.select("Pstrand14", "resi 351-363 & chain P ")
cmd.color ("orange", "Pstrand14")


cmd.select("Pstrand15", "resi 371-384 & chain P ")
cmd.color ("teal", "Pstrand15")


cmd.select("Pstrand16", "resi 389-403 & chain P ")
cmd.color ("yellow", "Pstrand16")


cmd.select("Pstrand17", "resi 413-427 & chain P ")
cmd.color ("blue", "Pstrand17")


cmd.select("Pstrand18", "resi 439-449 & chain P ")
cmd.color ("red", "Pstrand18")


cmd.select("Pstrand19", "resi 472-482 & chain P ")
cmd.color ("green", "Pstrand19")


cmd.select("Qstrand20", "resi 73-86 & chain Q ")
cmd.color ("orange", "Qstrand20")


cmd.select("Qstrand21", "resi 117-128 & chain Q ")
cmd.color ("teal", "Qstrand21")


cmd.select("Qstrand22", "resi 134-145 & chain Q ")
cmd.color ("yellow", "Qstrand22")


cmd.select("Qstrand23", "resi 159-168 & chain Q ")
cmd.color ("blue", "Qstrand23")


cmd.select("Qstrand24", "resi 181-188 & chain Q ")
cmd.color ("red", "Qstrand24")


cmd.select("Qstrand25", "resi 193-195 & chain Q ")
cmd.color ("green", "Qstrand25")


cmd.select("Qstrand26", "resi 200-203 & chain Q ")
cmd.color ("orange", "Qstrand26")


cmd.select("Qstrand27", "resi 206-217 & chain Q ")
cmd.color ("teal", "Qstrand27")


cmd.select("Qstrand28", "resi 221-233 & chain Q ")
cmd.color ("yellow", "Qstrand28")


cmd.select("Qstrand29", "resi 241-253 & chain Q ")
cmd.color ("blue", "Qstrand29")


cmd.select("Qstrand30", "resi 256-264 & chain Q ")
cmd.color ("red", "Qstrand30")


cmd.select("Qstrand31", "resi 286-296 & chain Q ")
cmd.color ("green", "Qstrand31")


cmd.select("Qstrand32", "resi 306-316 & chain Q ")
cmd.color ("orange", "Qstrand32")


cmd.select("Qstrand33", "resi 335-344 & chain Q ")
cmd.color ("teal", "Qstrand33")


cmd.select("Qstrand34", "resi 351-363 & chain Q ")
cmd.color ("yellow", "Qstrand34")


cmd.select("Qstrand35", "resi 371-384 & chain Q ")
cmd.color ("blue", "Qstrand35")


cmd.select("Qstrand36", "resi 389-403 & chain Q ")
cmd.color ("red", "Qstrand36")


cmd.select("Qstrand37", "resi 413-427 & chain Q ")
cmd.color ("green", "Qstrand37")


cmd.select("Qstrand38", "resi 439-449 & chain Q ")
cmd.color ("orange", "Qstrand38")


cmd.select("Qstrand39", "resi 472-482 & chain Q ")
cmd.color ("teal", "Qstrand39")


cmd.select("Rstrand40", "resi 73-86 & chain R ")
cmd.color ("yellow", "Rstrand40")


cmd.select("Rstrand41", "resi 117-128 & chain R ")
cmd.color ("blue", "Rstrand41")


cmd.select("Rstrand42", "resi 134-145 & chain R ")
cmd.color ("red", "Rstrand42")


cmd.select("Rstrand43", "resi 159-168 & chain R ")
cmd.color ("green", "Rstrand43")


cmd.select("Rstrand44", "resi 181-188 & chain R ")
cmd.color ("orange", "Rstrand44")


cmd.select("Rstrand45", "resi 193-195 & chain R ")
cmd.color ("teal", "Rstrand45")


cmd.select("Rstrand46", "resi 200-203 & chain R ")
cmd.color ("yellow", "Rstrand46")


cmd.select("Rstrand47", "resi 206-217 & chain R ")
cmd.color ("blue", "Rstrand47")


cmd.select("Rstrand48", "resi 221-233 & chain R ")
cmd.color ("red", "Rstrand48")


cmd.select("Rstrand49", "resi 241-253 & chain R ")
cmd.color ("green", "Rstrand49")


cmd.select("Rstrand50", "resi 256-264 & chain R ")
cmd.color ("orange", "Rstrand50")


cmd.select("Rstrand51", "resi 286-296 & chain R ")
cmd.color ("teal", "Rstrand51")


cmd.select("Rstrand52", "resi 306-316 & chain R ")
cmd.color ("yellow", "Rstrand52")


cmd.select("Rstrand53", "resi 335-344 & chain R ")
cmd.color ("blue", "Rstrand53")


cmd.select("Rstrand54", "resi 351-363 & chain R ")
cmd.color ("red", "Rstrand54")


cmd.select("Rstrand55", "resi 371-384 & chain R ")
cmd.color ("green", "Rstrand55")


cmd.select("Rstrand56", "resi 389-403 & chain R ")
cmd.color ("orange", "Rstrand56")


cmd.select("Rstrand57", "resi 413-427 & chain R ")
cmd.color ("teal", "Rstrand57")


cmd.select("Rstrand58", "resi 439-449 & chain R ")
cmd.color ("yellow", "Rstrand58")


cmd.select("Rstrand59", "resi 472-482 & chain R ")
cmd.color ("blue", "Rstrand59")


cmd.select("barrel", "Pstrand* or Qstrand* or Rstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
