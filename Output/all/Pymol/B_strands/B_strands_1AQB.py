from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AQB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22+23+24+25+26+27+28+29+30 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39+40+41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 99+100+101+102+103+104+105+106+107+108+109+110 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 85+86+87+88+89+90+91+92 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 67+68+69+70+71+72+73+74+75+76+77+78 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 114+115+116+117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 129+130+131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")