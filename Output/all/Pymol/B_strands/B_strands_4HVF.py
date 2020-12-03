from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4HVF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18+19+20+21+22+23+24+25+26+27+28+29 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 34+35+36+37+38+39+40+41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 206+207+208+209+210+211+212+213+214+215+216 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 192+193+194+195+196+197+198+199+200+201+202 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 134+135+136+137+140+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 168+169+170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 85+86+87+88+89+90+91+92+93 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 98+99+100+101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 111+112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
