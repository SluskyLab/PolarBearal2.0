from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EK9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Bstrand1", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Cstrand5", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("Cstrand8", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Astrand9", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
