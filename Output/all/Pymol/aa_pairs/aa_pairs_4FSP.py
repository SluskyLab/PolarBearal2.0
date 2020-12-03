from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 8+9+10+11+12+13+14+15+16+17+18+19+20+21+22 & chain A ")


cmd.select("Astrand1", "resi 362+363+364+365+366+367+368+369+370+371+372 & chain A ")


cmd.select("Astrand2", "resi 31+32+33+34+35+36+37+89+38+90+39+91+129+92+40+93+41+130+181+94+131+42+95+182+183+43+132+133+96+184+185+97+134+135+187+186+98+188+136+189+99+190+191+100 & chain A ")


cmd.select("Astrand3", "resi 194+195+196+197+142+198+143+199+144+145+200+146+103+201+104+147+105+202+110+106+148+149+203+107+109+56+52+51+108+54+53+150+152+55+58+57+151+59+60+61+62+63+64 & chain A ")


cmd.select("Astrand4", "resi 246+247+248+249+250+251+252+253+254+255+256+257 & chain A ")


cmd.select("Astrand5", "resi 224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")


cmd.select("Astrand6", "resi 207+208+209+210+211+212+213+214+215+216+217+218+219 & chain A ")


cmd.select("Astrand7", "resi 262+263+264+265+266+267+268+269+270+271+272 & chain A ")


cmd.select("Astrand8", "resi 302+303+304+305+306+307+308+309+310+311 & chain A ")


cmd.select("Astrand9", "resi 320+321+322+323+324+325+326+327+328+329+330 & chain A ")


cmd.select("Astrand10", "resi 342+343+344+345+346+347+348+349+350+351+352 & chain A ")


cmd.select("Astrand11", "resi 378+379+380+381+382+383+384+385+386+387+388+389+390 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH64A", pos=[-37.30571,14.684274,-22.012058])
cmd.pseudoatom ("PseudoH35A", pos=[-34.822845,13.656525,-21.398243])
cmd.pseudoatom ("PseudoH62A", pos=[-32.954956,19.650608,-22.398972])
cmd.pseudoatom ("PseudoH37A", pos=[-30.748854,19.010042,-21.711824])
cmd.pseudoatom ("PseudoH61A", pos=[-32.59677,23.635437,-24.24959])
cmd.pseudoatom ("PseudoH60A", pos=[-29.305115,25.098259,-21.629719])
cmd.pseudoatom ("PseudoH90A", pos=[-34.15547,25.533741,-24.430513])
cmd.pseudoatom ("PseudoH39A", pos=[-26.945343,24.348484,-21.112135])
cmd.pseudoatom ("PseudoH59A", pos=[-28.991224,29.30931,-22.794918])
cmd.pseudoatom ("PseudoH109A", pos=[-31.734428,35.738213,-14.01705])
cmd.pseudoatom ("PseudoH129A", pos=[-35.55148,33.660477,-10.946458])
cmd.pseudoatom ("PseudoH92A", pos=[-30.57198,31.257042,-22.462416])
cmd.pseudoatom ("PseudoH58A", pos=[-25.913076,30.069122,-19.66288])
cmd.pseudoatom ("PseudoH57A", pos=[-25.960938,34.467644,-20.184374])
cmd.pseudoatom ("PseudoH41A", pos=[-23.25225,29.131386,-19.465689])
cmd.pseudoatom ("PseudoH149A", pos=[-35.33793,39.170708,-7.871812])
cmd.pseudoatom ("PseudoH130A", pos=[-33.724186,37.3504,-12.625625])
cmd.pseudoatom ("PseudoH181A", pos=[-39.20808,38.589916,-1.8141773])
cmd.pseudoatom ("PseudoH148A", pos=[-34.92437,41.2064,-3.947762])
cmd.pseudoatom ("PseudoH94A", pos=[-27.576494,36.411343,-19.700727])
cmd.pseudoatom ("PseudoH107A", pos=[-29.325132,41.99814,-11.814268])
cmd.pseudoatom ("PseudoH56A", pos=[-21.981176,35.640427,-18.601513])
cmd.pseudoatom ("PseudoH95A", pos=[-27.769972,39.044155,-16.081144])
cmd.pseudoatom ("PseudoH55A", pos=[-22.843975,40.056076,-18.482332])
cmd.pseudoatom ("PseudoH201A", pos=[-35.088642,37.605484,2.6419117])
cmd.pseudoatom ("PseudoH182A", pos=[-35.6892,41.18087,-1.5702507])
cmd.pseudoatom ("PseudoH183A", pos=[-33.43301,39.17795,1.6396933])
cmd.pseudoatom ("PseudoH146A", pos=[-29.241285,42.30051,0.16251045])
cmd.pseudoatom ("PseudoH147A", pos=[-30.422115,42.167847,-3.9800158])
cmd.pseudoatom ("PseudoH132A", pos=[-29.885534,41.89351,-9.556931])
cmd.pseudoatom ("PseudoH133A", pos=[-28.70839,41.232155,-5.3739495])
cmd.pseudoatom ("PseudoH105A", pos=[-24.2622,43.545918,-7.8020844])
cmd.pseudoatom ("PseudoH106A", pos=[-24.905441,41.55768,-11.693176])
cmd.pseudoatom ("PseudoH96A", pos=[-24.475615,41.856384,-17.240904])
cmd.pseudoatom ("PseudoH199A", pos=[-29.14141,37.357647,6.1764717])
cmd.pseudoatom ("PseudoH184A", pos=[-29.341803,41.23358,2.088689])
cmd.pseudoatom ("PseudoH185A", pos=[-27.875427,39.19867,5.5753336])
cmd.pseudoatom ("PseudoH144A", pos=[-23.08893,41.267273,3.628947])
cmd.pseudoatom ("PseudoH97A", pos=[-23.11594,42.224007,-13.082779])
cmd.pseudoatom ("PseudoH53A", pos=[-19.581467,45.75555,-15.933132])
cmd.pseudoatom ("PseudoH145A", pos=[-24.744978,41.574406,-0.40635484])
cmd.pseudoatom ("PseudoH134A", pos=[-24.703941,43.127575,-5.5216494])
cmd.pseudoatom ("PseudoH135A", pos=[-22.940853,41.38147,-1.8247757])
cmd.pseudoatom ("PseudoH103A", pos=[-18.495852,44.114784,-3.7988105])
cmd.pseudoatom ("PseudoH187A", pos=[-21.681736,35.983673,7.5098896])
cmd.pseudoatom ("PseudoH142A", pos=[-17.49095,39.84626,6.853247])
cmd.pseudoatom ("PseudoH197A", pos=[-23.339478,35.24399,8.966093])
cmd.pseudoatom ("PseudoH186A", pos=[-23.228554,39.737694,5.6252203])
cmd.pseudoatom ("PseudoH104A", pos=[-19.817106,43.96728,-8.1032])
cmd.pseudoatom ("PseudoH98A", pos=[-20.258535,45.642254,-13.364518])
cmd.pseudoatom ("PseudoH195A", pos=[-17.34375,32.74367,10.557876])
cmd.pseudoatom ("PseudoH143A", pos=[-18.83242,40.563465,2.6382887])
cmd.pseudoatom ("PseudoH189A", pos=[-15.375053,34.30049,9.513129])
cmd.pseudoatom ("PseudoH99A", pos=[-18.057287,44.976692,-9.570465])
cmd.pseudoatom ("PseudoH51A", pos=[-16.216276,49.790203,-11.786325])
cmd.pseudoatom ("PseudoH246A", pos=[-44.46093,31.742521,12.742642])
cmd.pseudoatom ("PseudoH233A", pos=[-38.0378,31.490488,13.055273])
cmd.pseudoatom ("PseudoH248A", pos=[-38.383,29.151352,14.140764])
cmd.pseudoatom ("PseudoH231A", pos=[-32.205154,27.96527,13.921042])
cmd.pseudoatom ("PseudoH250A", pos=[-32.684265,25.290213,14.254398])
cmd.pseudoatom ("PseudoH252A", pos=[-27.195936,22.160563,12.310988])
cmd.pseudoatom ("PseudoH227A", pos=[-20.786018,20.868189,13.142856])
cmd.pseudoatom ("PseudoH254A", pos=[-20.974487,18.320007,13.487365])
cmd.pseudoatom ("PseudoH225A", pos=[-15.180395,17.025171,13.041744])
cmd.pseudoatom ("PseudoH256A", pos=[-15.578814,14.524006,12.347692])
cmd.pseudoatom ("PseudoH224A", pos=[-10.664139,17.614,12.6412945])
cmd.pseudoatom ("PseudoH217A", pos=[-14.478894,22.350552,12.5765705])
cmd.pseudoatom ("PseudoH226A", pos=[-16.433819,21.104038,12.052097])
cmd.pseudoatom ("PseudoH215A", pos=[-20.448898,26.079472,11.53763])
cmd.pseudoatom ("PseudoH228A", pos=[-22.582182,24.617847,11.296061])
cmd.pseudoatom ("PseudoH213A", pos=[-26.423988,29.610518,12.1748705])
cmd.pseudoatom ("PseudoH230A", pos=[-28.219765,27.89157,11.890784])
cmd.pseudoatom ("PseudoH211A", pos=[-32.09249,32.305897,10.27418])
cmd.pseudoatom ("PseudoH232A", pos=[-33.805946,31.29171,11.554736])
cmd.pseudoatom ("PseudoH209A", pos=[-38.12689,34.302986,8.506166])
cmd.pseudoatom ("PseudoH234A", pos=[-39.88842,33.568764,9.631123])
cmd.pseudoatom ("PseudoH207A", pos=[-44.141876,35.913162,5.820545])
cmd.pseudoatom ("PseudoH262A", pos=[-14.901919,8.351221,4.611502])
cmd.pseudoatom ("PseudoH308A", pos=[-20.870173,8.489451,6.985159])
cmd.pseudoatom ("PseudoH264A", pos=[-19.983845,9.690237,9.263315])
cmd.pseudoatom ("PseudoH306A", pos=[-26.04266,10.121515,11.224996])
cmd.pseudoatom ("PseudoH266A", pos=[-25.569208,12.5609045,12.704234])
cmd.pseudoatom ("PseudoH304A", pos=[-31.582066,13.628031,13.979337])
cmd.pseudoatom ("PseudoH268A", pos=[-31.072332,16.100546,14.231595])
cmd.pseudoatom ("PseudoH302A", pos=[-37.40593,17.474031,15.32307])
cmd.pseudoatom ("PseudoH329A", pos=[-37.86118,12.543674,12.981572])
cmd.pseudoatom ("PseudoH303A", pos=[-36.128166,13.555586,13.723728])
cmd.pseudoatom ("PseudoH327A", pos=[-32.542843,10.529523,9.725671])
cmd.pseudoatom ("PseudoH305A", pos=[-30.385067,11.079743,10.556024])
cmd.pseudoatom ("PseudoH325A", pos=[-27.026747,8.297503,6.1866307])
cmd.pseudoatom ("PseudoH307A", pos=[-25.273224,9.114181,7.0328445])
cmd.pseudoatom ("PseudoH323A", pos=[-22.004107,8.0233755,1.5128725])
cmd.pseudoatom ("PseudoH309A", pos=[-20.075928,8.699321,2.6038468])
cmd.pseudoatom ("PseudoH321A", pos=[-16.650925,7.411856,-3.0931053])
cmd.pseudoatom ("PseudoH311A", pos=[-14.67658,8.315852,-1.781812])
cmd.pseudoatom ("PseudoH320A", pos=[-16.310436,6.4300075,-7.4265695])
cmd.pseudoatom ("PseudoH349A", pos=[-22.251808,6.0061646,-4.7850704])
cmd.pseudoatom ("PseudoH322A", pos=[-20.998426,6.5021324,-2.5889144])
cmd.pseudoatom ("PseudoH347A", pos=[-27.111305,6.097883,0.034033418])
cmd.pseudoatom ("PseudoH324A", pos=[-26.256653,6.7365036,2.0974805])
cmd.pseudoatom ("PseudoH345A", pos=[-32.148483,6.644103,4.5578933])
cmd.pseudoatom ("PseudoH326A", pos=[-31.401857,7.468408,6.717514])
cmd.pseudoatom ("PseudoH343A", pos=[-37.693027,8.880183,8.570686])
cmd.pseudoatom ("PseudoH328A", pos=[-36.539192,9.0027685,10.831609])
cmd.pseudoatom ("PseudoH378A", pos=[-42.96884,6.083743,-2.5363648])
cmd.pseudoatom ("PseudoH20A", pos=[-39.993496,6.7657638,-7.8428874])
cmd.pseudoatom ("PseudoH380A", pos=[-37.897865,6.3574643,-6.60395])
cmd.pseudoatom ("PseudoH18A", pos=[-35.132034,9.114586,-11.76801])
cmd.pseudoatom ("PseudoH382A", pos=[-32.997974,9.172822,-10.686741])
cmd.pseudoatom ("PseudoH16A", pos=[-30.33856,12.016477,-15.471267])
cmd.pseudoatom ("PseudoH384A", pos=[-27.946634,11.521789,-14.526612])
cmd.pseudoatom ("PseudoH14A", pos=[-25.734058,15.358448,-18.164991])
cmd.pseudoatom ("PseudoH386A", pos=[-23.516617,14.575012,-17.312248])
cmd.pseudoatom ("PseudoH12A", pos=[-21.46773,20.231232,-19.768751])
cmd.pseudoatom ("PseudoH388A", pos=[-19.374578,19.438776,-19.13754])
cmd.pseudoatom ("PseudoH10A", pos=[-17.522463,25.15479,-22.067854])
cmd.pseudoatom ("PseudoH390A", pos=[-15.398175,24.138603,-21.369377])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR37A", pos=[-29.950926,18.910448,-20.152319])
cmd.pseudoatom ("PseudoR62A", pos=[-34.382557,20.41779,-21.736849])
cmd.pseudoatom ("PseudoR59A", pos=[-27.514088,28.724659,-23.606985])
cmd.pseudoatom ("PseudoR109A", pos=[-30.430183,35.198994,-15.084448])
cmd.pseudoatom ("PseudoR201A", pos=[-35.36014,35.89967,3.0857062])
cmd.pseudoatom ("PseudoR147A", pos=[-30.801699,40.544434,-3.5277843])
cmd.pseudoatom ("PseudoR185A", pos=[-27.094719,38.2719,4.3410926])
cmd.pseudoatom ("PseudoR252A", pos=[-27.269957,21.639301,13.9656315])
cmd.pseudoatom ("PseudoR219A", pos=[-7.42349,19.9238,14.08011])
cmd.pseudoatom ("PseudoR213A", pos=[-25.784616,29.9494,10.599282])
cmd.pseudoatom ("PseudoR329A", pos=[-39.0523,12.632418,11.733242])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 36 & chain A & name O", "resi 63 & chain A & name N")
cmd.distance("StrongHBond", "resi 36 & chain A & name N", "resi 63 & chain A & name O")
cmd.distance("StrongHBond", "resi 89 & chain A & name O", "resi 62 & chain A & name N")
cmd.distance("StrongHBond", "resi 89 & chain A & name N", "resi 62 & chain A & name O")
cmd.distance("StrongHBond", "resi 38 & chain A & name O", "resi 61 & chain A & name N")
cmd.distance("StrongHBond", "resi 38 & chain A & name N", "resi 61 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 60 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 60 & chain A & name O")
cmd.distance("StrongHBond", "resi 129 & chain A & name O", "resi 110 & chain A & name N")
cmd.distance("StrongHBond", "resi 129 & chain A & name N", "resi 110 & chain A & name O")
cmd.distance("StrongHBond", "resi 40 & chain A & name O", "resi 59 & chain A & name N")
cmd.distance("StrongHBond", "resi 40 & chain A & name N", "resi 59 & chain A & name O")
cmd.distance("StrongHBond", "resi 93 & chain A & name O", "resi 58 & chain A & name N")
cmd.distance("StrongHBond", "resi 93 & chain A & name N", "resi 58 & chain A & name O")
cmd.distance("StrongHBond", "resi 181 & chain A & name O", "resi 149 & chain A & name N")
cmd.distance("StrongHBond", "resi 181 & chain A & name N", "resi 149 & chain A & name O")
cmd.distance("StrongHBond", "resi 131 & chain A & name O", "resi 108 & chain A & name N")
cmd.distance("StrongHBond", "resi 131 & chain A & name N", "resi 108 & chain A & name O")
cmd.distance("StrongHBond", "resi 42 & chain A & name O", "resi 57 & chain A & name N")
cmd.distance("StrongHBond", "resi 42 & chain A & name N", "resi 57 & chain A & name O")
cmd.distance("StrongHBond", "resi 95 & chain A & name O", "resi 56 & chain A & name N")
cmd.distance("StrongHBond", "resi 95 & chain A & name N", "resi 56 & chain A & name O")
cmd.distance("StrongHBond", "resi 182 & chain A & name O", "resi 202 & chain A & name N")
cmd.distance("StrongHBond", "resi 182 & chain A & name N", "resi 202 & chain A & name O")
cmd.distance("StrongHBond", "resi 183 & chain A & name O", "resi 147 & chain A & name N")
cmd.distance("StrongHBond", "resi 183 & chain A & name N", "resi 147 & chain A & name O")
cmd.distance("StrongHBond", "resi 132 & chain A & name O", "resi 148 & chain A & name N")
cmd.distance("StrongHBond", "resi 132 & chain A & name N", "resi 148 & chain A & name O")
cmd.distance("StrongHBond", "resi 133 & chain A & name O", "resi 106 & chain A & name N")
cmd.distance("StrongHBond", "resi 133 & chain A & name N", "resi 106 & chain A & name O")
cmd.distance("StrongHBond", "resi 96 & chain A & name O", "resi 107 & chain A & name N")
cmd.distance("StrongHBond", "resi 96 & chain A & name N", "resi 107 & chain A & name O")
cmd.distance("StrongHBond", "resi 184 & chain A & name O", "resi 200 & chain A & name N")
cmd.distance("StrongHBond", "resi 184 & chain A & name N", "resi 200 & chain A & name O")
cmd.distance("StrongHBond", "resi 185 & chain A & name O", "resi 145 & chain A & name N")
cmd.distance("StrongHBond", "resi 185 & chain A & name N", "resi 145 & chain A & name O")
cmd.distance("StrongHBond", "resi 97 & chain A & name O", "resi 54 & chain A & name N")
cmd.distance("StrongHBond", "resi 97 & chain A & name N", "resi 54 & chain A & name O")
cmd.distance("StrongHBond", "resi 134 & chain A & name O", "resi 146 & chain A & name N")
cmd.distance("StrongHBond", "resi 134 & chain A & name N", "resi 146 & chain A & name O")
cmd.distance("StrongHBond", "resi 135 & chain A & name O", "resi 104 & chain A & name N")
cmd.distance("StrongHBond", "resi 135 & chain A & name N", "resi 104 & chain A & name O")
cmd.distance("StrongHBond", "resi 187 & chain A & name O", "resi 143 & chain A & name N")
cmd.distance("StrongHBond", "resi 187 & chain A & name N", "resi 143 & chain A & name O")
cmd.distance("StrongHBond", "resi 186 & chain A & name O", "resi 198 & chain A & name N")
cmd.distance("StrongHBond", "resi 186 & chain A & name N", "resi 198 & chain A & name O")
cmd.distance("StrongHBond", "resi 98 & chain A & name O", "resi 105 & chain A & name N")
cmd.distance("StrongHBond", "resi 98 & chain A & name N", "resi 105 & chain A & name O")
cmd.distance("StrongHBond", "resi 188 & chain A & name O", "resi 196 & chain A & name N")
cmd.distance("StrongHBond", "resi 188 & chain A & name N", "resi 196 & chain A & name O")
cmd.distance("StrongHBond", "resi 136 & chain A & name O", "resi 144 & chain A & name N")
cmd.distance("StrongHBond", "resi 136 & chain A & name N", "resi 144 & chain A & name O")
cmd.distance("StrongHBond", "resi 99 & chain A & name O", "resi 52 & chain A & name N")
cmd.distance("StrongHBond", "resi 99 & chain A & name N", "resi 52 & chain A & name O")
cmd.distance("StrongHBond", "resi 191 & chain A & name O", "resi 194 & chain A & name N")
cmd.distance("StrongHBond", "resi 191 & chain A & name N", "resi 194 & chain A & name O")
cmd.distance("StrongHBond", "resi 100 & chain A & name O", "resi 103 & chain A & name N")
cmd.distance("StrongHBond", "resi 100 & chain A & name N", "resi 103 & chain A & name O")
cmd.distance("StrongHBond", "resi 247 & chain A & name O", "resi 234 & chain A & name N")
cmd.distance("StrongHBond", "resi 247 & chain A & name N", "resi 234 & chain A & name O")
cmd.distance("StrongHBond", "resi 249 & chain A & name O", "resi 232 & chain A & name N")
cmd.distance("StrongHBond", "resi 249 & chain A & name N", "resi 232 & chain A & name O")
cmd.distance("StrongHBond", "resi 251 & chain A & name O", "resi 230 & chain A & name N")
cmd.distance("StrongHBond", "resi 251 & chain A & name N", "resi 230 & chain A & name O")
cmd.distance("StrongHBond", "resi 253 & chain A & name O", "resi 228 & chain A & name N")
cmd.distance("StrongHBond", "resi 253 & chain A & name N", "resi 228 & chain A & name O")
cmd.distance("StrongHBond", "resi 255 & chain A & name O", "resi 226 & chain A & name N")
cmd.distance("StrongHBond", "resi 255 & chain A & name N", "resi 226 & chain A & name O")
cmd.distance("StrongHBond", "resi 257 & chain A & name O", "resi 224 & chain A & name N")
cmd.distance("StrongHBond", "resi 257 & chain A & name N", "resi 224 & chain A & name O")
cmd.distance("StrongHBond", "resi 225 & chain A & name O", "resi 218 & chain A & name N")
cmd.distance("StrongHBond", "resi 225 & chain A & name N", "resi 218 & chain A & name O")
cmd.distance("StrongHBond", "resi 227 & chain A & name O", "resi 216 & chain A & name N")
cmd.distance("StrongHBond", "resi 227 & chain A & name N", "resi 216 & chain A & name O")
cmd.distance("StrongHBond", "resi 229 & chain A & name O", "resi 214 & chain A & name N")
cmd.distance("StrongHBond", "resi 229 & chain A & name N", "resi 214 & chain A & name O")
cmd.distance("StrongHBond", "resi 231 & chain A & name O", "resi 212 & chain A & name N")
cmd.distance("StrongHBond", "resi 231 & chain A & name N", "resi 212 & chain A & name O")
cmd.distance("StrongHBond", "resi 233 & chain A & name O", "resi 210 & chain A & name N")
cmd.distance("StrongHBond", "resi 233 & chain A & name N", "resi 210 & chain A & name O")
cmd.distance("StrongHBond", "resi 235 & chain A & name O", "resi 208 & chain A & name N")
cmd.distance("StrongHBond", "resi 235 & chain A & name N", "resi 208 & chain A & name O")
cmd.distance("StrongHBond", "resi 263 & chain A & name O", "resi 309 & chain A & name N")
cmd.distance("StrongHBond", "resi 263 & chain A & name N", "resi 309 & chain A & name O")
cmd.distance("StrongHBond", "resi 265 & chain A & name O", "resi 307 & chain A & name N")
cmd.distance("StrongHBond", "resi 265 & chain A & name N", "resi 307 & chain A & name O")
cmd.distance("StrongHBond", "resi 267 & chain A & name O", "resi 305 & chain A & name N")
cmd.distance("StrongHBond", "resi 267 & chain A & name N", "resi 305 & chain A & name O")
cmd.distance("StrongHBond", "resi 269 & chain A & name O", "resi 303 & chain A & name N")
cmd.distance("StrongHBond", "resi 269 & chain A & name N", "resi 303 & chain A & name O")
cmd.distance("StrongHBond", "resi 302 & chain A & name O", "resi 330 & chain A & name N")
cmd.distance("StrongHBond", "resi 302 & chain A & name N", "resi 330 & chain A & name O")
cmd.distance("StrongHBond", "resi 304 & chain A & name O", "resi 328 & chain A & name N")
cmd.distance("StrongHBond", "resi 304 & chain A & name N", "resi 328 & chain A & name O")
cmd.distance("StrongHBond", "resi 306 & chain A & name O", "resi 326 & chain A & name N")
cmd.distance("StrongHBond", "resi 306 & chain A & name N", "resi 326 & chain A & name O")
cmd.distance("StrongHBond", "resi 308 & chain A & name O", "resi 324 & chain A & name N")
cmd.distance("StrongHBond", "resi 308 & chain A & name N", "resi 324 & chain A & name O")
cmd.distance("StrongHBond", "resi 310 & chain A & name O", "resi 322 & chain A & name N")
cmd.distance("StrongHBond", "resi 310 & chain A & name N", "resi 322 & chain A & name O")
cmd.distance("StrongHBond", "resi 321 & chain A & name O", "resi 350 & chain A & name N")
cmd.distance("StrongHBond", "resi 321 & chain A & name N", "resi 350 & chain A & name O")
cmd.distance("StrongHBond", "resi 323 & chain A & name O", "resi 348 & chain A & name N")
cmd.distance("StrongHBond", "resi 323 & chain A & name N", "resi 348 & chain A & name O")
cmd.distance("StrongHBond", "resi 325 & chain A & name O", "resi 346 & chain A & name N")
cmd.distance("StrongHBond", "resi 325 & chain A & name N", "resi 346 & chain A & name O")
cmd.distance("StrongHBond", "resi 327 & chain A & name O", "resi 344 & chain A & name N")
cmd.distance("StrongHBond", "resi 327 & chain A & name N", "resi 344 & chain A & name O")
cmd.distance("StrongHBond", "resi 329 & chain A & name O", "resi 342 & chain A & name N")
cmd.distance("StrongHBond", "resi 329 & chain A & name N", "resi 342 & chain A & name O")
cmd.distance("StrongHBond", "resi 379 & chain A & name O", "resi 21 & chain A & name N")
cmd.distance("StrongHBond", "resi 379 & chain A & name N", "resi 21 & chain A & name O")
cmd.distance("StrongHBond", "resi 381 & chain A & name O", "resi 19 & chain A & name N")
cmd.distance("StrongHBond", "resi 381 & chain A & name N", "resi 19 & chain A & name O")
cmd.distance("StrongHBond", "resi 383 & chain A & name O", "resi 17 & chain A & name N")
cmd.distance("StrongHBond", "resi 383 & chain A & name N", "resi 17 & chain A & name O")
cmd.distance("StrongHBond", "resi 385 & chain A & name O", "resi 15 & chain A & name N")
cmd.distance("StrongHBond", "resi 385 & chain A & name N", "resi 15 & chain A & name O")
cmd.distance("StrongHBond", "resi 387 & chain A & name O", "resi 13 & chain A & name N")
cmd.distance("StrongHBond", "resi 387 & chain A & name N", "resi 13 & chain A & name O")
cmd.distance("StrongHBond", "resi 389 & chain A & name O", "resi 11 & chain A & name N")
cmd.distance("StrongHBond", "resi 389 & chain A & name N", "resi 11 & chain A & name O")
cmd.distance("WeakHBond", "resi 34 & chain A & name O", "PseudoH64A")
cmd.distance("WeakHBond", "resi 63 & chain A & name O", "PseudoH35A")
cmd.distance("WeakHBond", "resi 36 & chain A & name O", "PseudoH62A")
cmd.distance("WeakHBond", "resi 61 & chain A & name O", "PseudoH37A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH61A")
cmd.distance("WeakHBond", "resi 38 & chain A & name O", "PseudoH60A")
cmd.distance("WeakHBond", "resi 60 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 59 & chain A & name O", "PseudoH39A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH59A")
cmd.distance("WeakHBond", "resi 129 & chain A & name O", "PseudoH109A")
cmd.distance("WeakHBond", "resi 151 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 58 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 40 & chain A & name O", "PseudoH58A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH57A")
cmd.distance("WeakHBond", "resi 57 & chain A & name O", "PseudoH41A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH149A")
cmd.distance("WeakHBond", "resi 108 & chain A & name O", "PseudoH130A")
cmd.distance("WeakHBond", "resi 202 & chain A & name O", "PseudoH181A")
cmd.distance("WeakHBond", "resi 181 & chain A & name O", "PseudoH148A")
cmd.distance("WeakHBond", "resi 56 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 131 & chain A & name O", "PseudoH107A")
cmd.distance("WeakHBond", "resi 42 & chain A & name O", "PseudoH56A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 95 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 182 & chain A & name O", "PseudoH201A")
cmd.distance("WeakHBond", "resi 147 & chain A & name O", "PseudoH182A")
cmd.distance("WeakHBond", "resi 200 & chain A & name O", "PseudoH183A")
cmd.distance("WeakHBond", "resi 183 & chain A & name O", "PseudoH146A")
cmd.distance("WeakHBond", "resi 132 & chain A & name O", "PseudoH147A")
cmd.distance("WeakHBond", "resi 106 & chain A & name O", "PseudoH132A")
cmd.distance("WeakHBond", "resi 146 & chain A & name O", "PseudoH133A")
cmd.distance("WeakHBond", "resi 133 & chain A & name O", "PseudoH105A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH96A")
cmd.distance("WeakHBond", "resi 184 & chain A & name O", "PseudoH199A")
cmd.distance("WeakHBond", "resi 145 & chain A & name O", "PseudoH184A")
cmd.distance("WeakHBond", "resi 198 & chain A & name O", "PseudoH185A")
cmd.distance("WeakHBond", "resi 185 & chain A & name O", "PseudoH144A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH53A")
cmd.distance("WeakHBond", "resi 134 & chain A & name O", "PseudoH145A")
cmd.distance("WeakHBond", "resi 104 & chain A & name O", "PseudoH134A")
cmd.distance("WeakHBond", "resi 144 & chain A & name O", "PseudoH135A")
cmd.distance("WeakHBond", "resi 135 & chain A & name O", "PseudoH103A")
cmd.distance("WeakHBond", "resi 196 & chain A & name O", "PseudoH187A")
cmd.distance("WeakHBond", "resi 187 & chain A & name O", "PseudoH142A")
cmd.distance("WeakHBond", "resi 186 & chain A & name O", "PseudoH197A")
cmd.distance("WeakHBond", "resi 143 & chain A & name O", "PseudoH186A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH98A")
cmd.distance("WeakHBond", "resi 188 & chain A & name O", "PseudoH195A")
cmd.distance("WeakHBond", "resi 136 & chain A & name O", "PseudoH143A")
cmd.distance("WeakHBond", "resi 194 & chain A & name O", "PseudoH189A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH99A")
cmd.distance("WeakHBond", "resi 99 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 234 & chain A & name O", "PseudoH246A")
cmd.distance("WeakHBond", "resi 247 & chain A & name O", "PseudoH233A")
cmd.distance("WeakHBond", "resi 232 & chain A & name O", "PseudoH248A")
cmd.distance("WeakHBond", "resi 249 & chain A & name O", "PseudoH231A")
cmd.distance("WeakHBond", "resi 230 & chain A & name O", "PseudoH250A")
cmd.distance("WeakHBond", "resi 228 & chain A & name O", "PseudoH252A")
cmd.distance("WeakHBond", "resi 253 & chain A & name O", "PseudoH227A")
cmd.distance("WeakHBond", "resi 226 & chain A & name O", "PseudoH254A")
cmd.distance("WeakHBond", "resi 255 & chain A & name O", "PseudoH225A")
cmd.distance("WeakHBond", "resi 224 & chain A & name O", "PseudoH256A")
cmd.distance("WeakHBond", "resi 218 & chain A & name O", "PseudoH224A")
cmd.distance("WeakHBond", "resi 225 & chain A & name O", "PseudoH217A")
cmd.distance("WeakHBond", "resi 216 & chain A & name O", "PseudoH226A")
cmd.distance("WeakHBond", "resi 227 & chain A & name O", "PseudoH215A")
cmd.distance("WeakHBond", "resi 214 & chain A & name O", "PseudoH228A")
cmd.distance("WeakHBond", "resi 229 & chain A & name O", "PseudoH213A")
cmd.distance("WeakHBond", "resi 212 & chain A & name O", "PseudoH230A")
cmd.distance("WeakHBond", "resi 231 & chain A & name O", "PseudoH211A")
cmd.distance("WeakHBond", "resi 210 & chain A & name O", "PseudoH232A")
cmd.distance("WeakHBond", "resi 233 & chain A & name O", "PseudoH209A")
cmd.distance("WeakHBond", "resi 208 & chain A & name O", "PseudoH234A")
cmd.distance("WeakHBond", "resi 235 & chain A & name O", "PseudoH207A")
cmd.distance("WeakHBond", "resi 309 & chain A & name O", "PseudoH262A")
cmd.distance("WeakHBond", "resi 263 & chain A & name O", "PseudoH308A")
cmd.distance("WeakHBond", "resi 307 & chain A & name O", "PseudoH264A")
cmd.distance("WeakHBond", "resi 265 & chain A & name O", "PseudoH306A")
cmd.distance("WeakHBond", "resi 305 & chain A & name O", "PseudoH266A")
cmd.distance("WeakHBond", "resi 267 & chain A & name O", "PseudoH304A")
cmd.distance("WeakHBond", "resi 303 & chain A & name O", "PseudoH268A")
cmd.distance("WeakHBond", "resi 269 & chain A & name O", "PseudoH302A")
cmd.distance("WeakHBond", "resi 302 & chain A & name O", "PseudoH329A")
cmd.distance("WeakHBond", "resi 328 & chain A & name O", "PseudoH303A")
cmd.distance("WeakHBond", "resi 304 & chain A & name O", "PseudoH327A")
cmd.distance("WeakHBond", "resi 326 & chain A & name O", "PseudoH305A")
cmd.distance("WeakHBond", "resi 306 & chain A & name O", "PseudoH325A")
cmd.distance("WeakHBond", "resi 324 & chain A & name O", "PseudoH307A")
cmd.distance("WeakHBond", "resi 308 & chain A & name O", "PseudoH323A")
cmd.distance("WeakHBond", "resi 322 & chain A & name O", "PseudoH309A")
cmd.distance("WeakHBond", "resi 310 & chain A & name O", "PseudoH321A")
cmd.distance("WeakHBond", "resi 320 & chain A & name O", "PseudoH311A")
cmd.distance("WeakHBond", "resi 350 & chain A & name O", "PseudoH320A")
cmd.distance("WeakHBond", "resi 321 & chain A & name O", "PseudoH349A")
cmd.distance("WeakHBond", "resi 348 & chain A & name O", "PseudoH322A")
cmd.distance("WeakHBond", "resi 323 & chain A & name O", "PseudoH347A")
cmd.distance("WeakHBond", "resi 346 & chain A & name O", "PseudoH324A")
cmd.distance("WeakHBond", "resi 325 & chain A & name O", "PseudoH345A")
cmd.distance("WeakHBond", "resi 344 & chain A & name O", "PseudoH326A")
cmd.distance("WeakHBond", "resi 327 & chain A & name O", "PseudoH343A")
cmd.distance("WeakHBond", "resi 342 & chain A & name O", "PseudoH328A")
cmd.distance("WeakHBond", "resi 21 & chain A & name O", "PseudoH378A")
cmd.distance("WeakHBond", "resi 379 & chain A & name O", "PseudoH20A")
cmd.distance("WeakHBond", "resi 19 & chain A & name O", "PseudoH380A")
cmd.distance("WeakHBond", "resi 381 & chain A & name O", "PseudoH18A")
cmd.distance("WeakHBond", "resi 17 & chain A & name O", "PseudoH382A")
cmd.distance("WeakHBond", "resi 383 & chain A & name O", "PseudoH16A")
cmd.distance("WeakHBond", "resi 15 & chain A & name O", "PseudoH384A")
cmd.distance("WeakHBond", "resi 385 & chain A & name O", "PseudoH14A")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH386A")
cmd.distance("WeakHBond", "resi 387 & chain A & name O", "PseudoH12A")
cmd.distance("WeakHBond", "resi 11 & chain A & name O", "PseudoH388A")
cmd.distance("WeakHBond", "resi 389 & chain A & name O", "PseudoH10A")
cmd.distance("WeakHBond", "resi 9 & chain A & name O", "PseudoH390A")
cmd.distance("NonHBond", "resi 35 & chain A & name CB", "resi 64 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR37A", "PseudoR62A")
cmd.distance("NonHBond", "resi 90 & chain A & name CB", "resi 61 & chain A & name CB")
cmd.distance("NonHBond", "resi 39 & chain A & name CB", "resi 60 & chain A & name CB")
cmd.distance("NonHBond", "resi 129 & chain A & name CB", "resi 152 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "PseudoR59A")
cmd.distance("NonHBond", "resi 41 & chain A & name CB", "resi 58 & chain A & name CB")
cmd.distance("NonHBond", "resi 130 & chain A & name CB", "PseudoR109A")
cmd.distance("NonHBond", "resi 181 & chain A & name CB", "resi 203 & chain A & name CB")
cmd.distance("NonHBond", "resi 94 & chain A & name CB", "resi 57 & chain A & name CB")
cmd.distance("NonHBond", "resi 182 & chain A & name CB", "resi 148 & chain A & name CB")
cmd.distance("NonHBond", "resi 183 & chain A & name CB", "PseudoR201A")
cmd.distance("NonHBond", "resi 43 & chain A & name CB", "resi 56 & chain A & name CB")
cmd.distance("NonHBond", "resi 132 & chain A & name CB", "resi 107 & chain A & name CB")
cmd.distance("NonHBond", "resi 133 & chain A & name CB", "PseudoR147A")
cmd.distance("NonHBond", "resi 96 & chain A & name CB", "resi 55 & chain A & name CB")
cmd.distance("NonHBond", "resi 184 & chain A & name CB", "resi 146 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR185A", "resi 199 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "resi 106 & chain A & name CB")
cmd.distance("NonHBond", "resi 134 & chain A & name CB", "resi 105 & chain A & name CB")
cmd.distance("NonHBond", "resi 135 & chain A & name CB", "resi 145 & chain A & name CB")
cmd.distance("NonHBond", "resi 187 & chain A & name CB", "resi 197 & chain A & name CB")
cmd.distance("NonHBond", "resi 186 & chain A & name CB", "resi 144 & chain A & name CB")
cmd.distance("NonHBond", "resi 98 & chain A & name CB", "resi 53 & chain A & name CB")
cmd.distance("NonHBond", "resi 188 & chain A & name CB", "resi 142 & chain A & name CB")
cmd.distance("NonHBond", "resi 136 & chain A & name CB", "resi 103 & chain A & name CB")
cmd.distance("NonHBond", "resi 189 & chain A & name CB", "resi 195 & chain A & name CB")
cmd.distance("NonHBond", "resi 99 & chain A & name CB", "resi 104 & chain A & name CB")
cmd.distance("NonHBond", "resi 100 & chain A & name CB", "resi 51 & chain A & name CB")
cmd.distance("NonHBond", "resi 246 & chain A & name CB", "resi 235 & chain A & name CB")
cmd.distance("NonHBond", "resi 248 & chain A & name CB", "resi 233 & chain A & name CB")
cmd.distance("NonHBond", "resi 250 & chain A & name CB", "resi 231 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR252A", "resi 229 & chain A & name CB")
cmd.distance("NonHBond", "resi 254 & chain A & name CB", "resi 227 & chain A & name CB")
cmd.distance("NonHBond", "resi 256 & chain A & name CB", "resi 225 & chain A & name CB")
cmd.distance("NonHBond", "resi 224 & chain A & name CB", "PseudoR219A")
cmd.distance("NonHBond", "resi 226 & chain A & name CB", "resi 217 & chain A & name CB")
cmd.distance("NonHBond", "resi 228 & chain A & name CB", "resi 215 & chain A & name CB")
cmd.distance("NonHBond", "resi 230 & chain A & name CB", "PseudoR213A")
cmd.distance("NonHBond", "resi 232 & chain A & name CB", "resi 211 & chain A & name CB")
cmd.distance("NonHBond", "resi 234 & chain A & name CB", "resi 209 & chain A & name CB")
cmd.distance("NonHBond", "resi 236 & chain A & name CB", "resi 207 & chain A & name CB")
cmd.distance("NonHBond", "resi 262 & chain A & name CB", "resi 310 & chain A & name CB")
cmd.distance("NonHBond", "resi 264 & chain A & name CB", "resi 308 & chain A & name CB")
cmd.distance("NonHBond", "resi 266 & chain A & name CB", "resi 306 & chain A & name CB")
cmd.distance("NonHBond", "resi 268 & chain A & name CB", "resi 304 & chain A & name CB")
cmd.distance("NonHBond", "resi 270 & chain A & name CB", "resi 302 & chain A & name CB")
cmd.distance("NonHBond", "resi 303 & chain A & name CB", "PseudoR329A")
cmd.distance("NonHBond", "resi 305 & chain A & name CB", "resi 327 & chain A & name CB")
cmd.distance("NonHBond", "resi 307 & chain A & name CB", "resi 325 & chain A & name CB")
cmd.distance("NonHBond", "resi 309 & chain A & name CB", "resi 323 & chain A & name CB")
cmd.distance("NonHBond", "resi 311 & chain A & name CB", "resi 321 & chain A & name CB")
cmd.distance("NonHBond", "resi 320 & chain A & name CB", "resi 351 & chain A & name CB")
cmd.distance("NonHBond", "resi 322 & chain A & name CB", "resi 349 & chain A & name CB")
cmd.distance("NonHBond", "resi 324 & chain A & name CB", "resi 347 & chain A & name CB")
cmd.distance("NonHBond", "resi 326 & chain A & name CB", "resi 345 & chain A & name CB")
cmd.distance("NonHBond", "resi 328 & chain A & name CB", "resi 343 & chain A & name CB")
cmd.distance("NonHBond", "resi 378 & chain A & name CB", "resi 22 & chain A & name CB")
cmd.distance("NonHBond", "resi 380 & chain A & name CB", "resi 20 & chain A & name CB")
cmd.distance("NonHBond", "resi 382 & chain A & name CB", "resi 18 & chain A & name CB")
cmd.distance("NonHBond", "resi 384 & chain A & name CB", "resi 16 & chain A & name CB")
cmd.distance("NonHBond", "resi 386 & chain A & name CB", "resi 14 & chain A & name CB")
cmd.distance("NonHBond", "resi 388 & chain A & name CB", "resi 12 & chain A & name CB")
cmd.distance("NonHBond", "resi 390 & chain A & name CB", "resi 10 & chain A & name CB")
cmd.show("stick", "barrel")
cmd.color("red","StrongHBond")
cmd.color("green","WeakHBond")
cmd.color("purpleblue","NonHBond")
cmd.color("magenta","PseudoR*")
cmd.color("green","name CA & barrel")
cmd.color("red","name O & barrel")
cmd.color("blue","name N & barrel")
cmd.hide("labels")
cmd.zoom("barrel")
