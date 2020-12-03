from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 47+48+49+50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 182+183+184+185+186+187+188+189+190+191+192+193+194+195+196+197+198+199 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 203+204+205+206+207+208+209+210+211+212+213+214+215+216+217 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 121+122+123 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 143+144+145+146+147+148 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127+128+129+130 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 133+134+135+136+137 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 152+153+154+155+156+157+158+159 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 89+90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 63+64+65+66+67+68+69+70+71+72+73 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
