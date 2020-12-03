from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1P4T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+41+40+42+43+8+44+9+45+10+46+11+47+12+13+48+49+14+15+50+16+17+51+18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 98+99+100+101+60+61+62+63+26+27+64+24+25+30+23+31+65+32+66+33+67+34+68+35+69+36+70+71+37 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 122+123+124+125+126+127+128+129+130+131+132+133+134+135+136 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
