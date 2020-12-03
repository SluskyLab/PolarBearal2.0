from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4DKN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 110+111+112+113+114+115+116+117+118+119+120 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 97+98+99+100+101+102+103+104+105+106+107 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 205+206+207+208+209+210+211+212+213+214+215 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 133+134+135+136+139+140+141+142+143+144+145+146 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 150+151+152+153+154+155+156+157+158+159+160+161 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 166+167+168+169+170+171+172+173+174+175+176+177 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 191+192+193+194+195+196+197+198+199+200+201 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 84+85+86+87+88+89+90+91+92 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 35+36+37+38+39+40+41 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 18+19+20+21+22+23+24+25+26+27+28 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
