from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HZQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 24+24+25+26+27+28+29+30+31+40+41+42+43+44+45+46+47+48+54+55+56+57+58+59+60+61+67+68+69+70+71+72+73+74+75+76+84+85+86+87+88+96+97+98+99+100+101+102+103+108+109+110+111+112+113+114+115+116+121+122+123+124+125+126+127+128+129+130 & chain A")
cmd.load_cgo( [9.0, 5.5986977,7.413868,45.403465, -2.597563, 49.58715, 69.71465, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
