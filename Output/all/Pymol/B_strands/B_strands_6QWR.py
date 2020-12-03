from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6QWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 162+163+164+20+18+19+21+165+22+17+166+23+16+70+68+118+69+72+71+24+67+167+119+73+120+25+168+121+26+122+169+124+123+27+125+126+127+128+172+129+173+174+130+131+175+132+176+177 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 187+188+189+190+191 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 46+47+48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 78+79+80+81+82+83+84 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 94+95+96+140+141+97+98+142+143+99+144+100+145+194+101+195+56+102+146+196+197+57+148+147+103+58+198+149+150+199+104+59+151+200+152+105+60+201+106+153+154+61+202+107+155+203+62+204 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
