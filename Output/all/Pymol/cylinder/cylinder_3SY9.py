from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+37+38+39+40+41+42+43+44+45+46+47+48+56+57+58+59+60+61+62+63+64+65+66+67+68+69+100+101+102+103+104+105+106+107+108+109+110+111+112+115+116+117+118+119+120+121+122+141+142+143+144+145+146+147+148+154+155+156+157+158+159+160+161+162+163+189+190+191+192+193+194+195+196+197+198+199+200+201+204+205+206+207+208+209+210+211+212+213+217+218+219+220+221+222+223+224+225+226+227+228+229+234+235+236+237+238+239+240+241+242+243+244+245+246+247+257+258+259+260+261+262+263+264+265+266+267+268+269+272+273+274+275+276+277+278+279+280+281+282+313+314+315+316+317+318+319+320+321+322+331+332+333+334+335+336+337+338+339+340+341+366+367+368+369+370+371+372+373+374+375+376+377+387+388+389+390+391+392+393+394+395+396+397+398+408+409+410+411+412+413+414+415+416+417+418+419+420+421 & chain A")
cmd.load_cgo( [9.0, -26.79167,-5.8155518,-28.375952, -2.7255325, -50.832016, 15.809885, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
