from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZO6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+12+13+14+15+16+17+18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21+22+23+24+25+26+27+28+29+30+31+32 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 37+38+39+40+41+42+43+44+45+46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 203+204+205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 189+190+191+192+193+194+195+196+197+198+199+200 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 135+136+137+138+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 167+168+169+170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 100+101+102+103+104+105+106+107+108+109+110 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 113+114+115+116+117+118+119+120+121+122+123 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
