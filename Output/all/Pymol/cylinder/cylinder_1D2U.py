from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1D2U.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 22+22+23+24+25+26+27+28+29+30+41+42+43+44+45+46+47+48+49+52+53+54+55+56+57+58+59+60+67+68+69+70+71+72+73+74+75+76+77+78+81+82+83+84+85+86+87+88+89+104+105+106+107+108+109+110+111+112+116+117+118+119+120+121+122+123+124+132+133+134+135+136+137+138 & chain A")
cmd.load_cgo( [9.0, 17.686853,6.788002,42.699486, -10.074414, 28.223972, 34.84268, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
