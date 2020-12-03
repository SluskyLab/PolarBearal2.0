from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WJR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3+4+5+6+7+8+9+10 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 15+16+17+18+19+20+21+22+23+24+25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30+31+32+33+34+35+36+37+38+39+40+41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 54+55+56+57+58+59+60+61 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 69+70+71+72+73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 83+84+85+86+87+88+89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 100+101+102+103+104+105+106+107+108+109+110+111 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 127+128+129+130+131+132+133+134+135+136+137 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 142+143+144+145+146+147+148+149+150+151+152+153 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 165+166+167+168+169+170+171+172+173+174+175 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 181+182+183+184+185+186+187+188+189 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
