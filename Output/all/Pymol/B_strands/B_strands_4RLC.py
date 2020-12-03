from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RLC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 149+150+151+152+153+154+155+156+157+158+159 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 127+128+129+130+131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 65+66+67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 41+42+43+44+45+46+47+48+49+50+51 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 27+28+29+30+31+32+33+34+35+36 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
