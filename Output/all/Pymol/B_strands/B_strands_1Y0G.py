from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 24+25+26+27+34+35+36+37+38+39+40+41+42 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 104+105+106+107+108+109+110+111+112+113+114+115 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 118+119+120+121+122+123+124+125+126+127 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 70+71+72+73+74+75+76 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 46+47+48+49+50+51+52+55+56+57+58+59+60 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
