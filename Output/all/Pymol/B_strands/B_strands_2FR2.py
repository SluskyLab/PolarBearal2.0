from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FR2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17+18+19+20+21+22+23+24+25 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 150+151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 138+139+140+141+142+143+144+145+146+147 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 125+126+127+128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89+90+91+92+93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 103+104+105+106+107+108+109+115+116+117+118 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 63+64+65+66+67+68+69+70+71+72+73 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 48+49+50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 33+34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
