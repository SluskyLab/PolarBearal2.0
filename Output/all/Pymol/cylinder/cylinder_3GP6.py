from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3GP6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 22+22+23+24+25+26+27+28+29+30+31+32+33+52+53+54+55+56+57+58+59+60+66+67+68+69+70+71+72+73+74+75+81+82+83+84+85+86+87+88+89+90+91+92+93+101+102+103+104+105+106+107+108+109+110+111+112+113+121+122+123+124+125+126+127+128+129+130+131+132+133+136+137+138+139+140+141+142+143+152+153+154+155+156+157+158+159+160+161 & chain A")
cmd.load_cgo( [9.0, 7.2590637,32.022522,56.96173, 12.803301, 53.912323, 22.690018, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
