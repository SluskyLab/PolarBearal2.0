from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3GP6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22+23+24+25+26+27+28+29+30+31+32+33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 152+153+154+155+156+157+158+159+160+161 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 136+137+138+139+140+141+142+143 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 121+122+123+124+125+126+127+128+129+130+131+132+133 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 101+102+103+104+105+106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 66+67+68+69+70+71+72+73+74+75 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
