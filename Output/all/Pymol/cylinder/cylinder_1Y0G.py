from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 24+24+25+26+27+55+56+57+58+59+60+70+71+72+73+74+75+76+104+105+106+107+108+109+110+111+112+113+114+115+118+119+120+121+122+123+124+125+126+127+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+151+152+153+154+155+156+157+158+159+160+161+162+178+179+180+181+182+183+184+185+186+187+188+189+34+35+36+37+38+39+40+41+42+46+47+48+49+50+51+52 & chain B")
cmd.load_cgo( [9.0, -24.433405,-11.819828,47.331142, -30.155333, 36.279892, 28.582584, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
