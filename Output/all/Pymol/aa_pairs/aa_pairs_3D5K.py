from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain A ")


cmd.select("Astrand1", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain A ")


cmd.select("Astrand2", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain A ")


cmd.select("Astrand3", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")


cmd.select("Cstrand4", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain C ")


cmd.select("Cstrand5", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain C ")


cmd.select("Cstrand6", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain C ")


cmd.select("Cstrand7", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain C ")


cmd.select("Bstrand8", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain B ")


cmd.select("Bstrand9", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain B ")


cmd.select("Bstrand10", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain B ")


cmd.select("Bstrand11", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain B ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand* or Cstrand* or Bstrand*")
cmd.pseudoatom ("PseudoH88A", pos=[-17.754963,14.530258,-3.3976011])
cmd.pseudoatom ("PseudoH119A", pos=[-21.1143,16.67635,1.0853884])
cmd.pseudoatom ("PseudoH90A", pos=[-23.317566,17.158857,-0.20917332])
cmd.pseudoatom ("PseudoH117A", pos=[-27.16591,16.28038,4.464654])
cmd.pseudoatom ("PseudoH92A", pos=[-28.564333,14.935138,3.1620789])
cmd.pseudoatom ("PseudoH115A", pos=[-31.59462,12.13064,8.501211])
cmd.pseudoatom ("PseudoH94A", pos=[-33.211414,11.14565,6.8226666])
cmd.pseudoatom ("PseudoH113A", pos=[-35.504456,7.7961845,12.239139])
cmd.pseudoatom ("PseudoH96A", pos=[-37.24102,6.677585,10.587152])
cmd.pseudoatom ("PseudoH111A", pos=[-39.817623,3.3947108,15.040727])
cmd.pseudoatom ("PseudoH98A", pos=[-40.694637,1.7787963,13.873994])
cmd.pseudoatom ("PseudoH114A", pos=[-31.539293,9.974775,12.4016695])
cmd.pseudoatom ("PseudoH309A", pos=[-27.164286,14.600466,10.791565])
cmd.pseudoatom ("PseudoH116A", pos=[-27.861406,14.689766,8.701941])
cmd.pseudoatom ("PseudoH118A", pos=[-22.912495,16.568357,5.290486])
cmd.pseudoatom ("PseudoH305A", pos=[-17.440046,13.393311,3.550531])
cmd.pseudoatom ("PseudoH303A", pos=[-16.21685,7.2242656,0.6756527])
cmd.pseudoatom ("PseudoH301A", pos=[-12.060597,2.6491294,-2.9305804])
cmd.pseudoatom ("PseudoH125A", pos=[-11.762042,3.0170336,-5.3261123])
cmd.pseudoatom ("PseudoH330A", pos=[-9.430783,-2.7258322,-0.525997])
cmd.pseudoatom ("PseudoH300A", pos=[-9.23927,-0.658693,-1.8009558])
cmd.pseudoatom ("PseudoH328A", pos=[-11.613373,3.237368,2.887847])
cmd.pseudoatom ("PseudoH302A", pos=[-12.672678,4.445529,1.0743607])
cmd.pseudoatom ("PseudoH326A", pos=[-14.099924,8.054498,6.139283])
cmd.pseudoatom ("PseudoH304A", pos=[-15.626507,9.422252,4.456184])
cmd.pseudoatom ("PseudoH324A", pos=[-18.38975,13.203617,9.046301])
cmd.pseudoatom ("PseudoH306A", pos=[-18.589235,14.935062,7.7504888])
cmd.pseudoatom ("PseudoH322A", pos=[-21.799908,18.234959,12.638455])
cmd.pseudoatom ("PseudoH323A", pos=[-20.154486,14.018797,13.086829])
cmd.pseudoatom ("PseudoH97C", pos=[-16.910656,8.585397,11.886992])
cmd.pseudoatom ("PseudoH325A", pos=[-17.24106,8.764373,9.281])
cmd.pseudoatom ("PseudoH95C", pos=[-14.980661,3.0652747,8.990183])
cmd.pseudoatom ("PseudoH327A", pos=[-14.403692,3.7343183,6.5449777])
cmd.pseudoatom ("PseudoH93C", pos=[-12.753459,-2.4777977,5.298113])
cmd.pseudoatom ("PseudoH329A", pos=[-11.850836,-1.2941897,3.0712166])
cmd.pseudoatom ("PseudoH91C", pos=[-12.130278,-7.4712186,1.5614475])
cmd.pseudoatom ("PseudoH331A", pos=[-11.162786,-6.75267,-0.9054445])
cmd.pseudoatom ("PseudoH89C", pos=[-11.554271,-13.475891,-2.2753444])
cmd.pseudoatom ("PseudoH88C", pos=[-15.674889,-15.048069,-2.4384336])
cmd.pseudoatom ("PseudoH119C", pos=[-12.986344,-13.299956,2.9009192])
cmd.pseudoatom ("PseudoH90C", pos=[-11.248243,-11.776383,1.8679562])
cmd.pseudoatom ("PseudoH117C", pos=[-10.610463,-8.257923,6.8361306])
cmd.pseudoatom ("PseudoH92C", pos=[-10.386097,-6.150656,5.500208])
cmd.pseudoatom ("PseudoH115C", pos=[-12.3621235,-2.2684064,10.73474])
cmd.pseudoatom ("PseudoH94C", pos=[-12.1275215,-0.3669055,9.258017])
cmd.pseudoatom ("PseudoH113C", pos=[-14.91742,3.14,14.278102])
cmd.pseudoatom ("PseudoH96C", pos=[-14.750464,4.958234,13.019273])
cmd.pseudoatom ("PseudoH111C", pos=[-17.030638,8.478834,17.1661])
cmd.pseudoatom ("PseudoH98C", pos=[-18.07973,10.205266,15.960976])
cmd.pseudoatom ("PseudoH114C", pos=[-13.969027,-1.1698859,14.807071])
cmd.pseudoatom ("PseudoH309C", pos=[-13.0712,-7.4940467,12.70056])
cmd.pseudoatom ("PseudoH116C", pos=[-12.316714,-6.8038173,10.824154])
cmd.pseudoatom ("PseudoH118C", pos=[-13.016262,-11.858107,7.187435])
cmd.pseudoatom ("PseudoH305C", pos=[-17.83703,-14.9016075,4.315111])
cmd.pseudoatom ("PseudoH303C", pos=[-23.208803,-12.850546,0.41282725])
cmd.pseudoatom ("PseudoH301C", pos=[-28.627813,-14.3497095,-4.201788])
cmd.pseudoatom ("PseudoH125C", pos=[-27.920347,-14.463401,-6.487075])
cmd.pseudoatom ("PseudoH330C", pos=[-34.69111,-13.509819,-2.8558602])
cmd.pseudoatom ("PseudoH300C", pos=[-33.034653,-15.045443,-3.8805504])
cmd.pseudoatom ("PseudoH328C", pos=[-29.062826,-14.682969,1.441185])
cmd.pseudoatom ("PseudoH302C", pos=[-27.391113,-14.566882,0.1024037])
cmd.pseudoatom ("PseudoH326C", pos=[-24.621613,-15.554422,5.810233])
cmd.pseudoatom ("PseudoH304C", pos=[-22.282581,-14.411438,4.4251137])
cmd.pseudoatom ("PseudoH324C", pos=[-18.559938,-14.724742,9.825387])
cmd.pseudoatom ("PseudoH306C", pos=[-16.745104,-15.236945,8.775057])
cmd.pseudoatom ("PseudoH322C", pos=[-13.266247,-14.069961,14.474874])
cmd.pseudoatom ("PseudoH323C", pos=[-17.723558,-13.373969,14.004691])
cmd.pseudoatom ("PseudoH97B", pos=[-23.498325,-13.445908,11.706367])
cmd.pseudoatom ("PseudoH325C", pos=[-22.886986,-13.378209,9.358095])
cmd.pseudoatom ("PseudoH95B", pos=[-28.451004,-12.088527,7.988728])
cmd.pseudoatom ("PseudoH327C", pos=[-28.015366,-12.795638,5.518777])
cmd.pseudoatom ("PseudoH93B", pos=[-33.81325,-11.055815,3.3187475])
cmd.pseudoatom ("PseudoH329C", pos=[-32.953728,-12.380316,1.1622972])
cmd.pseudoatom ("PseudoH91B", pos=[-37.932217,-9.111483,-1.1616906])
cmd.pseudoatom ("PseudoH331C", pos=[-37.557137,-10.211496,-3.3876529])
cmd.pseudoatom ("PseudoH89B", pos=[-42.766357,-6.522356,-5.7135925])
cmd.pseudoatom ("PseudoH88B", pos=[-42.58548,-2.140893,-5.426184])
cmd.pseudoatom ("PseudoH119B", pos=[-43.1841,-5.6132746,-0.53408456])
cmd.pseudoatom ("PseudoH90B", pos=[-42.103497,-7.765266,-1.430072])
cmd.pseudoatom ("PseudoH117B", pos=[-40.047462,-10.032025,3.7961237])
cmd.pseudoatom ("PseudoH92B", pos=[-38.155365,-11.251908,2.7999732])
cmd.pseudoatom ("PseudoH115B", pos=[-34.990982,-11.763457,8.641971])
cmd.pseudoatom ("PseudoH94B", pos=[-32.90027,-12.691281,7.5022774])
cmd.pseudoatom ("PseudoH113B", pos=[-29.701874,-12.474824,13.118211])
cmd.pseudoatom ("PseudoH96B", pos=[-27.830963,-13.785891,12.061469])
cmd.pseudoatom ("PseudoH111B", pos=[-24.51799,-13.98269,16.903252])
cmd.pseudoatom ("PseudoH98B", pos=[-22.103256,-13.7992,16.022839])
cmd.pseudoatom ("PseudoH114B", pos=[-33.896854,-10.949871,12.929694])
cmd.pseudoatom ("PseudoH309B", pos=[-39.41858,-8.832148,10.182114])
cmd.pseudoatom ("PseudoH116B", pos=[-38.68571,-9.427263,8.09813])
cmd.pseudoatom ("PseudoH118B", pos=[-42.631924,-6.567952,3.8889296])
cmd.pseudoatom ("PseudoH305B", pos=[-42.3386,-0.53181547,1.3679607])
cmd.pseudoatom ("PseudoH303B", pos=[-37.105003,2.9520066,-1.3829815])
cmd.pseudoatom ("PseudoH301B", pos=[-34.87529,8.533345,-5.3744564])
cmd.pseudoatom ("PseudoH125B", pos=[-35.242382,8.354925,-7.917615])
cmd.pseudoatom ("PseudoH330B", pos=[-31.4761,13.411024,-3.2194993])
cmd.pseudoatom ("PseudoH300B", pos=[-33.51971,12.7268915,-4.647189])
cmd.pseudoatom ("PseudoH328B", pos=[-35.826744,8.775359,0.14042968])
cmd.pseudoatom ("PseudoH302B", pos=[-36.36914,7.396747,-1.2803401])
cmd.pseudoatom ("PseudoH326B", pos=[-39.392773,5.2413526,3.7683117])
cmd.pseudoatom ("PseudoH304B", pos=[-39.79102,3.0089626,2.0858364])
cmd.pseudoatom ("PseudoH324B", pos=[-42.363323,-0.66567206,6.944964])
cmd.pseudoatom ("PseudoH306B", pos=[-43.61215,-1.7174927,5.707375])
cmd.pseudoatom ("PseudoH322B", pos=[-45.553265,-5.572426,11.06875])
cmd.pseudoatom ("PseudoH323B", pos=[-42.66657,-2.0660763,11.269558])
cmd.pseudoatom ("PseudoH97A", pos=[-39.229748,2.9207675,9.723515])
cmd.pseudoatom ("PseudoH325B", pos=[-39.003212,2.3864505,7.2356443])
cmd.pseudoatom ("PseudoH95A", pos=[-34.891533,6.9378695,6.820087])
cmd.pseudoatom ("PseudoH327B", pos=[-35.370064,6.85901,4.354077])
cmd.pseudoatom ("PseudoH93A", pos=[-31.10234,11.372045,2.8353548])
cmd.pseudoatom ("PseudoH329B", pos=[-31.86253,10.963984,0.51863134])
cmd.pseudoatom ("PseudoH91A", pos=[-26.363884,14.043246,-0.65701556])
cmd.pseudoatom ("PseudoH331B", pos=[-27.17706,14.433995,-3.0213504])
cmd.pseudoatom ("PseudoH89A", pos=[-21.240057,17.030867,-4.282009])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR92A", pos=[-29.725138,15.49311,1.9338348])
cmd.pseudoatom ("PseudoR94A", pos=[-34.55359,11.180549,5.6578836])
cmd.pseudoatom ("PseudoR116A", pos=[-27.367092,13.345361,7.7422495])
cmd.pseudoatom ("PseudoR120A", pos=[-18.193094,13.179368,1.4811108])
cmd.pseudoatom ("PseudoR322A", pos=[-20.474512,18.304192,13.77088])
cmd.pseudoatom ("PseudoR89C", pos=[-12.419055,-11.982231,-2.481628])
cmd.pseudoatom ("PseudoR92C", pos=[-9.361393,-5.278541,4.3374915])
cmd.pseudoatom ("PseudoR94C", pos=[-11.322183,0.6916854,8.090593])
cmd.pseudoatom ("PseudoR116C", pos=[-13.4489155,-6.3952813,9.575432])
cmd.pseudoatom ("PseudoR120C", pos=[-17.291422,-14.55412,2.4041598])
cmd.pseudoatom ("PseudoR322C", pos=[-14.095344,-15.332015,15.333874])
cmd.pseudoatom ("PseudoR89B", pos=[-41.048225,-6.342293,-5.508915])
cmd.pseudoatom ("PseudoR92B", pos=[-37.703403,-12.565084,1.6860826])
cmd.pseudoatom ("PseudoR94B", pos=[-32.168762,-13.844361,6.3692365])
cmd.pseudoatom ("PseudoR116B", pos=[-37.568077,-8.582674,7.065666])
cmd.pseudoatom ("PseudoR322B", pos=[-46.267113,-4.287404,11.976598])
cmd.pseudoatom ("PseudoR89A", pos=[-22.075043,15.508005,-4.1652527])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 89 & chain A & name O", "resi 120 & chain A & name N")
cmd.distance("StrongHBond", "resi 89 & chain A & name N", "resi 120 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 118 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 118 & chain A & name O")
cmd.distance("StrongHBond", "resi 93 & chain A & name O", "resi 116 & chain A & name N")
cmd.distance("StrongHBond", "resi 93 & chain A & name N", "resi 116 & chain A & name O")
cmd.distance("StrongHBond", "resi 95 & chain A & name O", "resi 114 & chain A & name N")
cmd.distance("StrongHBond", "resi 95 & chain A & name N", "resi 114 & chain A & name O")
cmd.distance("StrongHBond", "resi 97 & chain A & name O", "resi 112 & chain A & name N")
cmd.distance("StrongHBond", "resi 97 & chain A & name N", "resi 112 & chain A & name O")
cmd.distance("StrongHBond", "resi 99 & chain A & name O", "resi 110 & chain A & name N")
cmd.distance("StrongHBond", "resi 99 & chain A & name N", "resi 110 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 310 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 310 & chain A & name O")
cmd.distance("StrongHBond", "resi 117 & chain A & name O", "resi 308 & chain A & name N")
cmd.distance("StrongHBond", "resi 117 & chain A & name N", "resi 308 & chain A & name O")
cmd.distance("StrongHBond", "resi 119 & chain A & name O", "resi 306 & chain A & name N")
cmd.distance("StrongHBond", "resi 119 & chain A & name N", "resi 306 & chain A & name O")
cmd.distance("StrongHBond", "resi 121 & chain A & name O", "resi 304 & chain A & name N")
cmd.distance("StrongHBond", "resi 121 & chain A & name N", "resi 304 & chain A & name O")
cmd.distance("StrongHBond", "resi 124 & chain A & name O", "resi 302 & chain A & name N")
cmd.distance("StrongHBond", "resi 124 & chain A & name N", "resi 302 & chain A & name O")
cmd.distance("StrongHBond", "resi 299 & chain A & name O", "resi 331 & chain A & name N")
cmd.distance("StrongHBond", "resi 299 & chain A & name N", "resi 331 & chain A & name O")
cmd.distance("StrongHBond", "resi 301 & chain A & name O", "resi 329 & chain A & name N")
cmd.distance("StrongHBond", "resi 301 & chain A & name N", "resi 329 & chain A & name O")
cmd.distance("StrongHBond", "resi 303 & chain A & name O", "resi 327 & chain A & name N")
cmd.distance("StrongHBond", "resi 303 & chain A & name N", "resi 327 & chain A & name O")
cmd.distance("StrongHBond", "resi 305 & chain A & name O", "resi 325 & chain A & name N")
cmd.distance("StrongHBond", "resi 305 & chain A & name N", "resi 325 & chain A & name O")
cmd.distance("StrongHBond", "resi 307 & chain A & name O", "resi 323 & chain A & name N")
cmd.distance("StrongHBond", "resi 307 & chain A & name N", "resi 323 & chain A & name O")
cmd.distance("StrongHBond", "resi 324 & chain A & name O", "resi 98 & chain C & name N")
cmd.distance("StrongHBond", "resi 324 & chain A & name N", "resi 98 & chain C & name O")
cmd.distance("StrongHBond", "resi 326 & chain A & name O", "resi 96 & chain C & name N")
cmd.distance("StrongHBond", "resi 326 & chain A & name N", "resi 96 & chain C & name O")
cmd.distance("StrongHBond", "resi 328 & chain A & name O", "resi 94 & chain C & name N")
cmd.distance("StrongHBond", "resi 328 & chain A & name N", "resi 94 & chain C & name O")
cmd.distance("StrongHBond", "resi 330 & chain A & name O", "resi 92 & chain C & name N")
cmd.distance("StrongHBond", "resi 330 & chain A & name N", "resi 92 & chain C & name O")
cmd.distance("StrongHBond", "resi 332 & chain A & name O", "resi 90 & chain C & name N")
cmd.distance("StrongHBond", "resi 332 & chain A & name N", "resi 90 & chain C & name O")
cmd.distance("StrongHBond", "resi 335 & chain A & name O", "resi 88 & chain C & name N")
cmd.distance("StrongHBond", "resi 335 & chain A & name N", "resi 88 & chain C & name O")
cmd.distance("StrongHBond", "resi 89 & chain C & name O", "resi 120 & chain C & name N")
cmd.distance("StrongHBond", "resi 89 & chain C & name N", "resi 120 & chain C & name O")
cmd.distance("StrongHBond", "resi 91 & chain C & name O", "resi 118 & chain C & name N")
cmd.distance("StrongHBond", "resi 91 & chain C & name N", "resi 118 & chain C & name O")
cmd.distance("StrongHBond", "resi 93 & chain C & name O", "resi 116 & chain C & name N")
cmd.distance("StrongHBond", "resi 93 & chain C & name N", "resi 116 & chain C & name O")
cmd.distance("StrongHBond", "resi 95 & chain C & name O", "resi 114 & chain C & name N")
cmd.distance("StrongHBond", "resi 95 & chain C & name N", "resi 114 & chain C & name O")
cmd.distance("StrongHBond", "resi 97 & chain C & name O", "resi 112 & chain C & name N")
cmd.distance("StrongHBond", "resi 97 & chain C & name N", "resi 112 & chain C & name O")
cmd.distance("StrongHBond", "resi 99 & chain C & name O", "resi 110 & chain C & name N")
cmd.distance("StrongHBond", "resi 99 & chain C & name N", "resi 110 & chain C & name O")
cmd.distance("StrongHBond", "resi 115 & chain C & name O", "resi 310 & chain C & name N")
cmd.distance("StrongHBond", "resi 115 & chain C & name N", "resi 310 & chain C & name O")
cmd.distance("StrongHBond", "resi 117 & chain C & name O", "resi 308 & chain C & name N")
cmd.distance("StrongHBond", "resi 117 & chain C & name N", "resi 308 & chain C & name O")
cmd.distance("StrongHBond", "resi 119 & chain C & name O", "resi 306 & chain C & name N")
cmd.distance("StrongHBond", "resi 119 & chain C & name N", "resi 306 & chain C & name O")
cmd.distance("StrongHBond", "resi 121 & chain C & name O", "resi 304 & chain C & name N")
cmd.distance("StrongHBond", "resi 121 & chain C & name N", "resi 304 & chain C & name O")
cmd.distance("StrongHBond", "resi 124 & chain C & name O", "resi 302 & chain C & name N")
cmd.distance("StrongHBond", "resi 124 & chain C & name N", "resi 302 & chain C & name O")
cmd.distance("StrongHBond", "resi 299 & chain C & name O", "resi 331 & chain C & name N")
cmd.distance("StrongHBond", "resi 299 & chain C & name N", "resi 331 & chain C & name O")
cmd.distance("StrongHBond", "resi 301 & chain C & name O", "resi 329 & chain C & name N")
cmd.distance("StrongHBond", "resi 301 & chain C & name N", "resi 329 & chain C & name O")
cmd.distance("StrongHBond", "resi 303 & chain C & name O", "resi 327 & chain C & name N")
cmd.distance("StrongHBond", "resi 303 & chain C & name N", "resi 327 & chain C & name O")
cmd.distance("StrongHBond", "resi 305 & chain C & name O", "resi 325 & chain C & name N")
cmd.distance("StrongHBond", "resi 305 & chain C & name N", "resi 325 & chain C & name O")
cmd.distance("StrongHBond", "resi 307 & chain C & name O", "resi 323 & chain C & name N")
cmd.distance("StrongHBond", "resi 307 & chain C & name N", "resi 323 & chain C & name O")
cmd.distance("StrongHBond", "resi 324 & chain C & name O", "resi 98 & chain B & name N")
cmd.distance("StrongHBond", "resi 324 & chain C & name N", "resi 98 & chain B & name O")
cmd.distance("StrongHBond", "resi 326 & chain C & name O", "resi 96 & chain B & name N")
cmd.distance("StrongHBond", "resi 326 & chain C & name N", "resi 96 & chain B & name O")
cmd.distance("StrongHBond", "resi 330 & chain C & name O", "resi 92 & chain B & name N")
cmd.distance("StrongHBond", "resi 330 & chain C & name N", "resi 92 & chain B & name O")
cmd.distance("StrongHBond", "resi 332 & chain C & name O", "resi 90 & chain B & name N")
cmd.distance("StrongHBond", "resi 332 & chain C & name N", "resi 90 & chain B & name O")
cmd.distance("StrongHBond", "resi 335 & chain C & name O", "resi 88 & chain B & name N")
cmd.distance("StrongHBond", "resi 335 & chain C & name N", "resi 88 & chain B & name O")
cmd.distance("StrongHBond", "resi 89 & chain B & name O", "resi 120 & chain B & name N")
cmd.distance("StrongHBond", "resi 89 & chain B & name N", "resi 120 & chain B & name O")
cmd.distance("StrongHBond", "resi 91 & chain B & name O", "resi 118 & chain B & name N")
cmd.distance("StrongHBond", "resi 91 & chain B & name N", "resi 118 & chain B & name O")
cmd.distance("StrongHBond", "resi 93 & chain B & name O", "resi 116 & chain B & name N")
cmd.distance("StrongHBond", "resi 93 & chain B & name N", "resi 116 & chain B & name O")
cmd.distance("StrongHBond", "resi 95 & chain B & name O", "resi 114 & chain B & name N")
cmd.distance("StrongHBond", "resi 95 & chain B & name N", "resi 114 & chain B & name O")
cmd.distance("StrongHBond", "resi 97 & chain B & name O", "resi 112 & chain B & name N")
cmd.distance("StrongHBond", "resi 97 & chain B & name N", "resi 112 & chain B & name O")
cmd.distance("StrongHBond", "resi 99 & chain B & name O", "resi 110 & chain B & name N")
cmd.distance("StrongHBond", "resi 99 & chain B & name N", "resi 110 & chain B & name O")
cmd.distance("StrongHBond", "resi 115 & chain B & name O", "resi 310 & chain B & name N")
cmd.distance("StrongHBond", "resi 115 & chain B & name N", "resi 310 & chain B & name O")
cmd.distance("StrongHBond", "resi 117 & chain B & name O", "resi 308 & chain B & name N")
cmd.distance("StrongHBond", "resi 117 & chain B & name N", "resi 308 & chain B & name O")
cmd.distance("StrongHBond", "resi 119 & chain B & name O", "resi 306 & chain B & name N")
cmd.distance("StrongHBond", "resi 119 & chain B & name N", "resi 306 & chain B & name O")
cmd.distance("StrongHBond", "resi 121 & chain B & name O", "resi 304 & chain B & name N")
cmd.distance("StrongHBond", "resi 121 & chain B & name N", "resi 304 & chain B & name O")
cmd.distance("StrongHBond", "resi 124 & chain B & name O", "resi 302 & chain B & name N")
cmd.distance("StrongHBond", "resi 124 & chain B & name N", "resi 302 & chain B & name O")
cmd.distance("StrongHBond", "resi 299 & chain B & name O", "resi 331 & chain B & name N")
cmd.distance("StrongHBond", "resi 299 & chain B & name N", "resi 331 & chain B & name O")
cmd.distance("StrongHBond", "resi 301 & chain B & name O", "resi 329 & chain B & name N")
cmd.distance("StrongHBond", "resi 301 & chain B & name N", "resi 329 & chain B & name O")
cmd.distance("StrongHBond", "resi 303 & chain B & name O", "resi 327 & chain B & name N")
cmd.distance("StrongHBond", "resi 303 & chain B & name N", "resi 327 & chain B & name O")
cmd.distance("StrongHBond", "resi 305 & chain B & name O", "resi 325 & chain B & name N")
cmd.distance("StrongHBond", "resi 305 & chain B & name N", "resi 325 & chain B & name O")
cmd.distance("StrongHBond", "resi 307 & chain B & name O", "resi 323 & chain B & name N")
cmd.distance("StrongHBond", "resi 307 & chain B & name N", "resi 323 & chain B & name O")
cmd.distance("StrongHBond", "resi 326 & chain B & name O", "resi 96 & chain A & name N")
cmd.distance("StrongHBond", "resi 326 & chain B & name N", "resi 96 & chain A & name O")
cmd.distance("StrongHBond", "resi 330 & chain B & name O", "resi 92 & chain A & name N")
cmd.distance("StrongHBond", "resi 330 & chain B & name N", "resi 92 & chain A & name O")
cmd.distance("StrongHBond", "resi 332 & chain B & name O", "resi 90 & chain A & name N")
cmd.distance("StrongHBond", "resi 332 & chain B & name N", "resi 90 & chain A & name O")
cmd.distance("StrongHBond", "resi 335 & chain B & name O", "resi 88 & chain A & name N")
cmd.distance("StrongHBond", "resi 335 & chain B & name N", "resi 88 & chain A & name O")
cmd.distance("WeakHBond", "resi 120 & chain A & name O", "PseudoH88A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 95 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 112 & chain A & name O", "PseudoH96A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH111A")
cmd.distance("WeakHBond", "resi 110 & chain A & name O", "PseudoH98A")
cmd.distance("WeakHBond", "resi 310 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH309A")
cmd.distance("WeakHBond", "resi 308 & chain A & name O", "PseudoH116A")
cmd.distance("WeakHBond", "resi 306 & chain A & name O", "PseudoH118A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH305A")
cmd.distance("WeakHBond", "resi 121 & chain A & name O", "PseudoH303A")
cmd.distance("WeakHBond", "resi 124 & chain A & name O", "PseudoH301A")
cmd.distance("WeakHBond", "resi 300 & chain A & name O", "PseudoH125A")
cmd.distance("WeakHBond", "resi 299 & chain A & name O", "PseudoH330A")
cmd.distance("WeakHBond", "resi 329 & chain A & name O", "PseudoH300A")
cmd.distance("WeakHBond", "resi 301 & chain A & name O", "PseudoH328A")
cmd.distance("WeakHBond", "resi 327 & chain A & name O", "PseudoH302A")
cmd.distance("WeakHBond", "resi 303 & chain A & name O", "PseudoH326A")
cmd.distance("WeakHBond", "resi 325 & chain A & name O", "PseudoH304A")
cmd.distance("WeakHBond", "resi 305 & chain A & name O", "PseudoH324A")
cmd.distance("WeakHBond", "resi 323 & chain A & name O", "PseudoH306A")
cmd.distance("WeakHBond", "resi 307 & chain A & name O", "PseudoH322A")
cmd.distance("WeakHBond", "resi 98 & chain C & name O", "PseudoH323A")
cmd.distance("WeakHBond", "resi 324 & chain A & name O", "PseudoH97C")
cmd.distance("WeakHBond", "resi 96 & chain C & name O", "PseudoH325A")
cmd.distance("WeakHBond", "resi 326 & chain A & name O", "PseudoH95C")
cmd.distance("WeakHBond", "resi 94 & chain C & name O", "PseudoH327A")
cmd.distance("WeakHBond", "resi 328 & chain A & name O", "PseudoH93C")
cmd.distance("WeakHBond", "resi 92 & chain C & name O", "PseudoH329A")
cmd.distance("WeakHBond", "resi 330 & chain A & name O", "PseudoH91C")
cmd.distance("WeakHBond", "resi 90 & chain C & name O", "PseudoH331A")
cmd.distance("WeakHBond", "resi 332 & chain A & name O", "PseudoH89C")
cmd.distance("WeakHBond", "resi 120 & chain C & name O", "PseudoH88C")
cmd.distance("WeakHBond", "resi 89 & chain C & name O", "PseudoH119C")
cmd.distance("WeakHBond", "resi 118 & chain C & name O", "PseudoH90C")
cmd.distance("WeakHBond", "resi 91 & chain C & name O", "PseudoH117C")
cmd.distance("WeakHBond", "resi 116 & chain C & name O", "PseudoH92C")
cmd.distance("WeakHBond", "resi 93 & chain C & name O", "PseudoH115C")
cmd.distance("WeakHBond", "resi 114 & chain C & name O", "PseudoH94C")
cmd.distance("WeakHBond", "resi 95 & chain C & name O", "PseudoH113C")
cmd.distance("WeakHBond", "resi 112 & chain C & name O", "PseudoH96C")
cmd.distance("WeakHBond", "resi 97 & chain C & name O", "PseudoH111C")
cmd.distance("WeakHBond", "resi 110 & chain C & name O", "PseudoH98C")
cmd.distance("WeakHBond", "resi 310 & chain C & name O", "PseudoH114C")
cmd.distance("WeakHBond", "resi 115 & chain C & name O", "PseudoH309C")
cmd.distance("WeakHBond", "resi 308 & chain C & name O", "PseudoH116C")
cmd.distance("WeakHBond", "resi 306 & chain C & name O", "PseudoH118C")
cmd.distance("WeakHBond", "resi 119 & chain C & name O", "PseudoH305C")
cmd.distance("WeakHBond", "resi 121 & chain C & name O", "PseudoH303C")
cmd.distance("WeakHBond", "resi 124 & chain C & name O", "PseudoH301C")
cmd.distance("WeakHBond", "resi 300 & chain C & name O", "PseudoH125C")
cmd.distance("WeakHBond", "resi 299 & chain C & name O", "PseudoH330C")
cmd.distance("WeakHBond", "resi 329 & chain C & name O", "PseudoH300C")
cmd.distance("WeakHBond", "resi 301 & chain C & name O", "PseudoH328C")
cmd.distance("WeakHBond", "resi 327 & chain C & name O", "PseudoH302C")
cmd.distance("WeakHBond", "resi 303 & chain C & name O", "PseudoH326C")
cmd.distance("WeakHBond", "resi 325 & chain C & name O", "PseudoH304C")
cmd.distance("WeakHBond", "resi 305 & chain C & name O", "PseudoH324C")
cmd.distance("WeakHBond", "resi 323 & chain C & name O", "PseudoH306C")
cmd.distance("WeakHBond", "resi 307 & chain C & name O", "PseudoH322C")
cmd.distance("WeakHBond", "resi 98 & chain B & name O", "PseudoH323C")
cmd.distance("WeakHBond", "resi 324 & chain C & name O", "PseudoH97B")
cmd.distance("WeakHBond", "resi 96 & chain B & name O", "PseudoH325C")
cmd.distance("WeakHBond", "resi 326 & chain C & name O", "PseudoH95B")
cmd.distance("WeakHBond", "resi 94 & chain B & name O", "PseudoH327C")
cmd.distance("WeakHBond", "resi 328 & chain C & name O", "PseudoH93B")
cmd.distance("WeakHBond", "resi 92 & chain B & name O", "PseudoH329C")
cmd.distance("WeakHBond", "resi 330 & chain C & name O", "PseudoH91B")
cmd.distance("WeakHBond", "resi 90 & chain B & name O", "PseudoH331C")
cmd.distance("WeakHBond", "resi 332 & chain C & name O", "PseudoH89B")
cmd.distance("WeakHBond", "resi 120 & chain B & name O", "PseudoH88B")
cmd.distance("WeakHBond", "resi 89 & chain B & name O", "PseudoH119B")
cmd.distance("WeakHBond", "resi 118 & chain B & name O", "PseudoH90B")
cmd.distance("WeakHBond", "resi 91 & chain B & name O", "PseudoH117B")
cmd.distance("WeakHBond", "resi 116 & chain B & name O", "PseudoH92B")
cmd.distance("WeakHBond", "resi 93 & chain B & name O", "PseudoH115B")
cmd.distance("WeakHBond", "resi 114 & chain B & name O", "PseudoH94B")
cmd.distance("WeakHBond", "resi 95 & chain B & name O", "PseudoH113B")
cmd.distance("WeakHBond", "resi 112 & chain B & name O", "PseudoH96B")
cmd.distance("WeakHBond", "resi 97 & chain B & name O", "PseudoH111B")
cmd.distance("WeakHBond", "resi 110 & chain B & name O", "PseudoH98B")
cmd.distance("WeakHBond", "resi 310 & chain B & name O", "PseudoH114B")
cmd.distance("WeakHBond", "resi 115 & chain B & name O", "PseudoH309B")
cmd.distance("WeakHBond", "resi 308 & chain B & name O", "PseudoH116B")
cmd.distance("WeakHBond", "resi 306 & chain B & name O", "PseudoH118B")
cmd.distance("WeakHBond", "resi 119 & chain B & name O", "PseudoH305B")
cmd.distance("WeakHBond", "resi 121 & chain B & name O", "PseudoH303B")
cmd.distance("WeakHBond", "resi 124 & chain B & name O", "PseudoH301B")
cmd.distance("WeakHBond", "resi 300 & chain B & name O", "PseudoH125B")
cmd.distance("WeakHBond", "resi 299 & chain B & name O", "PseudoH330B")
cmd.distance("WeakHBond", "resi 329 & chain B & name O", "PseudoH300B")
cmd.distance("WeakHBond", "resi 301 & chain B & name O", "PseudoH328B")
cmd.distance("WeakHBond", "resi 327 & chain B & name O", "PseudoH302B")
cmd.distance("WeakHBond", "resi 303 & chain B & name O", "PseudoH326B")
cmd.distance("WeakHBond", "resi 325 & chain B & name O", "PseudoH304B")
cmd.distance("WeakHBond", "resi 305 & chain B & name O", "PseudoH324B")
cmd.distance("WeakHBond", "resi 323 & chain B & name O", "PseudoH306B")
cmd.distance("WeakHBond", "resi 307 & chain B & name O", "PseudoH322B")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH323B")
cmd.distance("WeakHBond", "resi 324 & chain B & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH325B")
cmd.distance("WeakHBond", "resi 326 & chain B & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH327B")
cmd.distance("WeakHBond", "resi 328 & chain B & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH329B")
cmd.distance("WeakHBond", "resi 330 & chain B & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH331B")
cmd.distance("WeakHBond", "resi 332 & chain B & name O", "PseudoH89A")
cmd.distance("NonHBond", "resi 90 & chain A & name CB", "resi 119 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR92A", "resi 117 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR94A", "resi 115 & chain A & name CB")
cmd.distance("NonHBond", "resi 96 & chain A & name CB", "resi 113 & chain A & name CB")
cmd.distance("NonHBond", "resi 98 & chain A & name CB", "resi 111 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR116A", "resi 309 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR120A", "resi 305 & chain A & name CB")
cmd.distance("NonHBond", "resi 122 & chain A & name CB", "resi 303 & chain A & name CB")
cmd.distance("NonHBond", "resi 125 & chain A & name CB", "resi 301 & chain A & name CB")
cmd.distance("NonHBond", "resi 300 & chain A & name CB", "resi 330 & chain A & name CB")
cmd.distance("NonHBond", "resi 302 & chain A & name CB", "resi 328 & chain A & name CB")
cmd.distance("NonHBond", "resi 304 & chain A & name CB", "resi 326 & chain A & name CB")
cmd.distance("NonHBond", "resi 306 & chain A & name CB", "resi 324 & chain A & name CB")
cmd.distance("NonHBond", "resi 308 & chain A & name CB", "PseudoR322A")
cmd.distance("NonHBond", "resi 325 & chain A & name CB", "resi 97 & chain C & name CB")
cmd.distance("NonHBond", "resi 327 & chain A & name CB", "resi 95 & chain C & name CB")
cmd.distance("NonHBond", "resi 329 & chain A & name CB", "resi 93 & chain C & name CB")
cmd.distance("NonHBond", "resi 331 & chain A & name CB", "resi 91 & chain C & name CB")
cmd.distance("NonHBond", "resi 333 & chain A & name CB", "PseudoR89C")
cmd.distance("NonHBond", "resi 88 & chain C & name CB", "resi 121 & chain C & name CB")
cmd.distance("NonHBond", "resi 90 & chain C & name CB", "resi 119 & chain C & name CB")
cmd.distance("NonHBond", "PseudoR92C", "resi 117 & chain C & name CB")
cmd.distance("NonHBond", "PseudoR94C", "resi 115 & chain C & name CB")
cmd.distance("NonHBond", "resi 96 & chain C & name CB", "resi 113 & chain C & name CB")
cmd.distance("NonHBond", "resi 98 & chain C & name CB", "resi 111 & chain C & name CB")
cmd.distance("NonHBond", "PseudoR116C", "resi 309 & chain C & name CB")
cmd.distance("NonHBond", "PseudoR120C", "resi 305 & chain C & name CB")
cmd.distance("NonHBond", "resi 122 & chain C & name CB", "resi 303 & chain C & name CB")
cmd.distance("NonHBond", "resi 125 & chain C & name CB", "resi 301 & chain C & name CB")
cmd.distance("NonHBond", "resi 300 & chain C & name CB", "resi 330 & chain C & name CB")
cmd.distance("NonHBond", "resi 302 & chain C & name CB", "resi 328 & chain C & name CB")
cmd.distance("NonHBond", "resi 304 & chain C & name CB", "resi 326 & chain C & name CB")
cmd.distance("NonHBond", "resi 306 & chain C & name CB", "resi 324 & chain C & name CB")
cmd.distance("NonHBond", "resi 308 & chain C & name CB", "PseudoR322C")
cmd.distance("NonHBond", "resi 325 & chain C & name CB", "resi 97 & chain B & name CB")
cmd.distance("NonHBond", "resi 327 & chain C & name CB", "resi 95 & chain B & name CB")
cmd.distance("NonHBond", "resi 329 & chain C & name CB", "resi 93 & chain B & name CB")
cmd.distance("NonHBond", "resi 331 & chain C & name CB", "resi 91 & chain B & name CB")
cmd.distance("NonHBond", "resi 333 & chain C & name CB", "PseudoR89B")
cmd.distance("NonHBond", "resi 88 & chain B & name CB", "resi 121 & chain B & name CB")
cmd.distance("NonHBond", "resi 90 & chain B & name CB", "resi 119 & chain B & name CB")
cmd.distance("NonHBond", "PseudoR92B", "resi 117 & chain B & name CB")
cmd.distance("NonHBond", "PseudoR94B", "resi 115 & chain B & name CB")
cmd.distance("NonHBond", "resi 96 & chain B & name CB", "resi 113 & chain B & name CB")
cmd.distance("NonHBond", "resi 98 & chain B & name CB", "resi 111 & chain B & name CB")
cmd.distance("NonHBond", "PseudoR116B", "resi 309 & chain B & name CB")
cmd.distance("NonHBond", "resi 122 & chain B & name CB", "resi 303 & chain B & name CB")
cmd.distance("NonHBond", "resi 125 & chain B & name CB", "resi 301 & chain B & name CB")
cmd.distance("NonHBond", "resi 300 & chain B & name CB", "resi 330 & chain B & name CB")
cmd.distance("NonHBond", "resi 302 & chain B & name CB", "resi 328 & chain B & name CB")
cmd.distance("NonHBond", "resi 304 & chain B & name CB", "resi 326 & chain B & name CB")
cmd.distance("NonHBond", "resi 306 & chain B & name CB", "resi 324 & chain B & name CB")
cmd.distance("NonHBond", "resi 308 & chain B & name CB", "PseudoR322B")
cmd.distance("NonHBond", "resi 325 & chain B & name CB", "resi 97 & chain A & name CB")
cmd.distance("NonHBond", "resi 327 & chain B & name CB", "resi 95 & chain A & name CB")
cmd.distance("NonHBond", "resi 329 & chain B & name CB", "resi 93 & chain A & name CB")
cmd.distance("NonHBond", "resi 331 & chain B & name CB", "resi 91 & chain A & name CB")
cmd.distance("NonHBond", "resi 333 & chain B & name CB", "PseudoR89A")
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
