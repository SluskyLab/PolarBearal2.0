from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4XMC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 25+26+27+28+29+30+31+32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 130+131+132+133+134+135+136+137+138+139+140 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 53+54+76+75+55+74+56+73+72+57+58+71+59+70+60+69+61+68+62+67 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 83+84+85+86+87+88+89+90+91 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 105+106+107+108+109+110+111+112+113+114+115 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 41+42+43+44+45+46+47+48+49+50 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 118+119+120+121+122+123+124+125+126+127 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
