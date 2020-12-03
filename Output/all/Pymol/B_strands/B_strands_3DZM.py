from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DZM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3+4+5+6+7+8+9+10+11+12+13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 195+196+197+198+199+200+201+202+203+204+205+206 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 144+145+146+147+148+149+150+151+152+153+154+155 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 120+121+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 93+94+95+96+97+98+99+100+101+102+103+104+105+106+107+160+108+161+109+162+110+163+164+165 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 171+172+173+174+175+176+70+69+71+72+73+74+75+76+77+78+79+80+81+82+83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 33+34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 16+17+18+19+20+21+22+23+24+25 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
