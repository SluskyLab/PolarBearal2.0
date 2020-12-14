from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3B07.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 74+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+162+163+164+165+166+167+168+169+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+239+240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281+282+287+288+289+290+291+292+293+294+295+296+297+298+299 & chain A or resi 102+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+153+154+155+156+157+158+159+160+161+162+163+164+165+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+59+60+61+62+168+169+170+171+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+244+245+246+247+248+249+250+251+252+253+254+255+256+257+258+259+260+261+262+263+264+265+266+271+272+273+274+275+276+277+278 & chain B or resi 108+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+162+163+164+165+166+167+168+169+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+239+240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281+282+287+288+289+290+291+292+293+294+295+296+297+298+299 & chain C or resi 102+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+153+154+155+156+157+158+159+160+161+162+163+164+165+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+59+60+61+62+168+169+170+171+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+244+245+246+247+248+249+250+251+252+253+254+255+256+257+258+259+260+261+262+263+264+265+266+271+272+273+274+275+276+277+278 & chain D or resi 108+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+162+163+164+165+166+167+168+169+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+239+240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281+282+287+288+289+290+291+292+293+294+295+296+297+298+299 & chain E or resi 102+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+153+154+155+156+157+158+159+160+161+162+163+164+165+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+59+60+61+62+168+169+170+171+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+244+245+246+247+248+249+250+251+252+253+254+255+256+257+258+259+260+261+262+263+264+265+266+271+272+273+274+275+276+277+278 & chain F or resi 108+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+162+163+164+165+166+167+168+169+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+239+240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281+282+287+288+289+290+291+292+293+294+295+296+297+298+299 & chain G or resi 102+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+153+154+155+156+157+158+159+160+161+162+163+164+165+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+59+60+61+62+168+169+170+171+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+244+245+246+247+248+249+250+251+252+253+254+255+256+257+258+259+260+261+262+263+264+265+266+271+272+273+274+275+276+277+278 & chain H")
cmd.load_cgo( [9.0, -2.8183746,41.25624,-11.1159725, 106.09796, 41.256516, -51.3021, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")