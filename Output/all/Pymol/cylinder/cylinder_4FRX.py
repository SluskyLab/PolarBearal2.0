from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FRX.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 11+11+12+13+14+15+16+17+18+19+20+21+22+31+32+33+34+35+36+37+38+39+40+41+42+43+44+53+54+55+56+57+58+59+60+61+62+63+64+65+96+97+98+99+100+101+102+103+104+105+106+107+108+111+112+113+114+115+116+117+118+136+137+138+139+140+141+142+143+144+150+151+152+153+154+155+156+157+158+159+160+161+168+169+170+189+190+191+192+193+194+195+196+197+202+203+204+205+206+207+208+209+210+211+215+216+217+218+219+220+221+222+223+224+225+226+227+228+231+232+233+234+235+236+237+238+239+240+241+242+243+244+274+275+276+277+278+279+280+281+282+283+284+285+286+289+290+291+292+293+294+295+296+297+298+299+334+335+336+337+338+339+340+341+342+343+352+353+354+355+356+357+358+359+360+361+362+363+364+371+372+373+374+375+376+377+378+379+380+381+382+383+393+394+395+396+397+398+399+400+401+402+403+404+416+417+418+419+420+421+422+423+424+425+426+427+428 & chain A")
cmd.load_cgo( [9.0, 41.21917,-2.0372639,19.16512, 12.314188, -20.42831, 74.92447, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")