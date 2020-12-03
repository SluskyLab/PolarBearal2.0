from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4XMC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 25+25+26+27+28+29+30+31+32+41+42+43+44+45+46+47+48+49+50+53+54+55+56+57+58+59+60+61+62+67+68+69+70+71+72+73+74+75+76+83+84+85+86+87+88+89+90+91+97+98+99+105+106+107+108+109+110+111+112+113+114+115+118+119+120+121+122+123+124+125+126+127+130+131+132+133+134+135+136+137+138+139+140 & chain A")
cmd.load_cgo( [9.0, -15.081934,3.313768,7.5849395, 25.375399, -6.323939, 9.912549, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
