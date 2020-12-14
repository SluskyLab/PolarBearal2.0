from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 26+26+27+28+29+30+31+32+38+39+40+41+42+43+44+45+46+47+48+54+55+56+57+58+59+60+61+62+63+64+69+70+71+72+73+74+75+76+81+82+83+84+85+86+87+88+95+96+97+98+99+100+101+102+103+110+111+112+113+114+115+116+117+118+119+120+123+124+125+126+127+128+129+130+131+137+138+139+140+141+142+143+144+145+146+149+150+151+152+153+154+155+156+157+158+163+164+165+166+167+168+169+170+171+172+173+174+178+179+180+181+182+183+184+185+189+190+191+192+193+194+195+196+197+202+203+204+205+206+207+208+209+210+211+214+215+216+217+218+219+220+221+222+223+224+225+231+232+233+234+235+236+237+238+242+243+244+245+246+247+248+249+250+251+252+255+256+257+258+259+260+261+262+263+264+274+275+276+277+278+279+280+281+282 & chain X")
cmd.load_cgo( [9.0, 6.4477654,46.160313,43.572968, 18.87408, 16.594997, -9.023735, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")