from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4QKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 212+213+214+215+216+217+218 & chain A ")


cmd.select("Astrand1", "resi 227+228+229+230+231+232+233+234+235+236+237+238+239 & chain A ")


cmd.select("Astrand2", "resi 546+547+548+549+550+551+552+553 & chain A ")


cmd.select("Astrand3", "resi 522+523+524+525+526+527+528+529+530+531 & chain A ")


cmd.select("Astrand4", "resi 504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519 & chain A ")


cmd.select("Astrand5", "resi 418+419+420+421+422+423+424+425+426+427+428+429+430 & chain A ")


cmd.select("Astrand6", "resi 488+489+490+491+492+493+494+495+496+497+498 & chain A ")


cmd.select("Astrand7", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")


cmd.select("Astrand8", "resi 458+459+460+461+462+463+464+465+466+467+468+469+470+471 & chain A ")


cmd.select("Astrand9", "resi 369+370+371+372+373+374+375+376+377+378+379 & chain A ")


cmd.select("Astrand10", "resi 355+356+357+358+359+360+361+362+363+364+365 & chain A ")


cmd.select("Astrand11", "resi 324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")


cmd.select("Astrand12", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320 & chain A ")


cmd.select("Astrand13", "resi 279+280+281+282+283+284+285+286+287+288+289+290+291+292 & chain A ")


cmd.select("Astrand14", "resi 264+265+266+267+268+269+270+271+272+273+274+275+276 & chain A ")


cmd.select("Astrand15", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH236A", pos=[16.117603,30.376263,-18.41988])
cmd.pseudoatom ("PseudoH213A", pos=[14.696957,32.49143,-18.33726])
cmd.pseudoatom ("PseudoH234A", pos=[19.650333,36.56965,-20.227156])
cmd.pseudoatom ("PseudoH215A", pos=[17.983221,38.431488,-19.95924])
cmd.pseudoatom ("PseudoH232A", pos=[23.303713,42.268047,-21.31107])
cmd.pseudoatom ("PseudoH217A", pos=[23.049694,43.983074,-19.403791])
cmd.pseudoatom ("PseudoH230A", pos=[27.389784,47.456497,-20.689257])
cmd.pseudoatom ("PseudoH546A", pos=[28.581654,54.102894,-10.082967])
cmd.pseudoatom ("PseudoH526A", pos=[23.48906,51.230507,-9.537564])
cmd.pseudoatom ("PseudoH548A", pos=[23.73529,50.27334,-12.156164])
cmd.pseudoatom ("PseudoH524A", pos=[18.307886,46.366756,-11.507816])
cmd.pseudoatom ("PseudoH522A", pos=[12.977436,42.587654,-13.443891])
cmd.pseudoatom ("PseudoH523A", pos=[14.607948,44.58274,-9.674167])
cmd.pseudoatom ("PseudoH516A", pos=[19.06584,48.277122,-6.062091])
cmd.pseudoatom ("PseudoH525A", pos=[20.199791,48.500446,-7.867307])
cmd.pseudoatom ("PseudoH527A", pos=[26.156582,51.62722,-5.971842])
cmd.pseudoatom ("PseudoH512A", pos=[30.471003,52.716385,-2.9973834])
cmd.pseudoatom ("PseudoH529A", pos=[31.58716,53.564034,-4.9022255])
cmd.pseudoatom ("PseudoH510A", pos=[37.359703,52.78938,-1.6279756])
cmd.pseudoatom ("PseudoH531A", pos=[38.422955,53.156113,-4.296237])
cmd.pseudoatom ("PseudoH365A", pos=[23.013186,31.272295,11.533872])
cmd.pseudoatom ("PseudoH370A", pos=[24.645155,32.80028,10.686627])
cmd.pseudoatom ("PseudoH363A", pos=[28.404037,28.072737,7.970673])
cmd.pseudoatom ("PseudoH372A", pos=[29.58565,29.630676,6.713835])
cmd.pseudoatom ("PseudoH361A", pos=[33.171265,24.903208,3.9756641])
cmd.pseudoatom ("PseudoH374A", pos=[34.62379,26.543652,3.0407069])
cmd.pseudoatom ("PseudoH359A", pos=[38.718353,21.511587,0.48653242])
cmd.pseudoatom ("PseudoH376A", pos=[39.772743,23.385828,0.021833152])
cmd.pseudoatom ("PseudoH357A", pos=[41.121914,21.10865,-5.6447086])
cmd.pseudoatom ("PseudoH378A", pos=[43.113667,22.580566,-5.9099693])
cmd.pseudoatom ("PseudoH355A", pos=[43.98723,20.984251,-11.821072])
cmd.pseudoatom ("PseudoH332A", pos=[39.03202,18.696901,-11.08279])
cmd.pseudoatom ("PseudoH356A", pos=[40.68579,18.898766,-9.43115])
cmd.pseudoatom ("PseudoH330A", pos=[36.84644,17.767807,-4.2935762])
cmd.pseudoatom ("PseudoH358A", pos=[38.46806,18.755363,-2.7905562])
cmd.pseudoatom ("PseudoH328A", pos=[34.10318,18.911798,2.2705722])
cmd.pseudoatom ("PseudoH360A", pos=[34.75817,20.818354,2.8571146])
cmd.pseudoatom ("PseudoH326A", pos=[29.865854,21.62402,7.283786])
cmd.pseudoatom ("PseudoH362A", pos=[30.30941,23.976282,7.294176])
cmd.pseudoatom ("PseudoH324A", pos=[25.482897,24.834572,11.554417])
cmd.pseudoatom ("PseudoH320A", pos=[24.778105,19.48995,10.11472])
cmd.pseudoatom ("PseudoH325A", pos=[25.738611,21.07237,8.758689])
cmd.pseudoatom ("PseudoH317A", pos=[27.7675,17.610764,3.8769634])
cmd.pseudoatom ("PseudoH327A", pos=[30.05045,18.334497,4.351584])
cmd.pseudoatom ("PseudoH315A", pos=[30.766441,17.508844,-2.0771785])
cmd.pseudoatom ("PseudoH329A", pos=[33.082066,17.484896,-1.8399398])
cmd.pseudoatom ("PseudoH313A", pos=[33.12007,18.293945,-8.1378565])
cmd.pseudoatom ("PseudoH331A", pos=[35.288094,18.418753,-8.285119])
cmd.pseudoatom ("PseudoH311A", pos=[35.16805,20.332298,-14.52572])
cmd.pseudoatom ("PseudoH333A", pos=[37.20311,21.1497,-14.19206])
cmd.pseudoatom ("PseudoH309A", pos=[36.859238,24.027405,-19.897326])
cmd.pseudoatom ("PseudoH335A", pos=[39.20026,24.253757,-19.889635])
cmd.pseudoatom ("PseudoH307A", pos=[39.108826,28.533907,-24.138998])
cmd.pseudoatom ("PseudoH337A", pos=[41.52771,28.27994,-24.830347])
cmd.pseudoatom ("PseudoH305A", pos=[41.275875,32.835243,-29.615953])
cmd.pseudoatom ("PseudoH339A", pos=[43.64548,32.8849,-29.378944])
cmd.pseudoatom ("PseudoH303A", pos=[44.36084,38.48954,-32.435413])
cmd.pseudoatom ("PseudoH291A", pos=[38.628677,39.00362,-31.6206])
cmd.pseudoatom ("PseudoH304A", pos=[40.254517,36.90831,-31.259916])
cmd.pseudoatom ("PseudoH289A", pos=[36.190983,33.305332,-27.435537])
cmd.pseudoatom ("PseudoH306A", pos=[37.680294,31.668541,-27.11453])
cmd.pseudoatom ("PseudoH287A", pos=[33.531197,27.949806,-24.120846])
cmd.pseudoatom ("PseudoH308A", pos=[35.43536,26.046963,-23.52842])
cmd.pseudoatom ("PseudoH285A", pos=[31.943388,23.373907,-19.283096])
cmd.pseudoatom ("PseudoH310A", pos=[33.334076,21.566639,-18.281225])
cmd.pseudoatom ("PseudoH283A", pos=[29.403175,19.165007,-13.870059])
cmd.pseudoatom ("PseudoH312A", pos=[31.734205,18.220161,-12.426564])
cmd.pseudoatom ("PseudoH281A", pos=[27.801554,16.172167,-8.0375395])
cmd.pseudoatom ("PseudoH314A", pos=[29.803524,15.936179,-6.126605])
cmd.pseudoatom ("PseudoH279A", pos=[26.319916,14.605259,-1.6949184])
cmd.pseudoatom ("PseudoH275A", pos=[22.08487,16.488144,-5.2219033])
cmd.pseudoatom ("PseudoH280A", pos=[24.330168,16.349045,-5.1898193])
cmd.pseudoatom ("PseudoH273A", pos=[24.066204,19.689892,-10.435397])
cmd.pseudoatom ("PseudoH282A", pos=[26.489271,19.596502,-10.523572])
cmd.pseudoatom ("PseudoH271A", pos=[26.41091,23.849504,-15.241355])
cmd.pseudoatom ("PseudoH284A", pos=[28.583023,22.937166,-16.219664])
cmd.pseudoatom ("PseudoH286A", pos=[30.138971,26.738098,-21.265995])
cmd.pseudoatom ("PseudoH267A", pos=[31.04333,32.882248,-24.017439])
cmd.pseudoatom ("PseudoH288A", pos=[32.86622,32.271927,-24.608068])
cmd.pseudoatom ("PseudoH265A", pos=[33.86743,38.439873,-26.888422])
cmd.pseudoatom ("PseudoH290A", pos=[35.645626,37.771423,-28.228539])
cmd.pseudoatom ("PseudoH254A", pos=[28.453281,38.645687,-25.206959])
cmd.pseudoatom ("PseudoH266A", pos=[29.771664,36.86589,-25.765451])
cmd.pseudoatom ("PseudoH252A", pos=[25.250317,32.87335,-23.083593])
cmd.pseudoatom ("PseudoH268A", pos=[27.11841,30.978912,-23.023407])
cmd.pseudoatom ("PseudoH250A", pos=[22.803936,27.71998,-19.622879])
cmd.pseudoatom ("PseudoH270A", pos=[24.825504,25.732714,-18.928741])
cmd.pseudoatom ("PseudoH248A", pos=[20.950424,22.98187,-15.134959])
cmd.pseudoatom ("PseudoH272A", pos=[22.737854,21.495436,-14.308966])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR510A", pos=[36.54267,51.515957,-2.4484475])
cmd.pseudoatom ("PseudoR359A", pos=[37.336174,22.211277,-0.26609394])
cmd.pseudoatom ("PseudoR330A", pos=[36.168064,16.18749,-4.6468782])
cmd.pseudoatom ("PseudoR331A", pos=[36.084106,19.941906,-8.161115])
cmd.pseudoatom ("PseudoR311A", pos=[34.08738,21.628252,-14.053946])
cmd.pseudoatom ("PseudoR305A", pos=[41.25036,33.85331,-28.219072])
cmd.pseudoatom ("PseudoR286A", pos=[31.452293,27.46685,-20.368824])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 212 & chain A & name O", "resi 237 & chain A & name N")
cmd.distance("StrongHBond", "resi 212 & chain A & name N", "resi 237 & chain A & name O")
cmd.distance("StrongHBond", "resi 214 & chain A & name O", "resi 235 & chain A & name N")
cmd.distance("StrongHBond", "resi 214 & chain A & name N", "resi 235 & chain A & name O")
cmd.distance("StrongHBond", "resi 216 & chain A & name O", "resi 233 & chain A & name N")
cmd.distance("StrongHBond", "resi 216 & chain A & name N", "resi 233 & chain A & name O")
cmd.distance("StrongHBond", "resi 218 & chain A & name O", "resi 231 & chain A & name N")
cmd.distance("StrongHBond", "resi 218 & chain A & name N", "resi 231 & chain A & name O")
cmd.distance("StrongHBond", "resi 547 & chain A & name O", "resi 527 & chain A & name N")
cmd.distance("StrongHBond", "resi 547 & chain A & name N", "resi 527 & chain A & name O")
cmd.distance("StrongHBond", "resi 549 & chain A & name O", "resi 525 & chain A & name N")
cmd.distance("StrongHBond", "resi 549 & chain A & name N", "resi 525 & chain A & name O")
cmd.distance("StrongHBond", "resi 551 & chain A & name O", "resi 523 & chain A & name N")
cmd.distance("StrongHBond", "resi 551 & chain A & name N", "resi 523 & chain A & name O")
cmd.distance("StrongHBond", "resi 522 & chain A & name O", "resi 519 & chain A & name N")
cmd.distance("StrongHBond", "resi 522 & chain A & name N", "resi 519 & chain A & name O")
cmd.distance("StrongHBond", "resi 524 & chain A & name O", "resi 517 & chain A & name N")
cmd.distance("StrongHBond", "resi 524 & chain A & name N", "resi 517 & chain A & name O")
cmd.distance("StrongHBond", "resi 526 & chain A & name O", "resi 515 & chain A & name N")
cmd.distance("StrongHBond", "resi 526 & chain A & name N", "resi 515 & chain A & name O")
cmd.distance("StrongHBond", "resi 528 & chain A & name O", "resi 513 & chain A & name N")
cmd.distance("StrongHBond", "resi 528 & chain A & name N", "resi 513 & chain A & name O")
cmd.distance("StrongHBond", "resi 530 & chain A & name O", "resi 511 & chain A & name N")
cmd.distance("StrongHBond", "resi 530 & chain A & name N", "resi 511 & chain A & name O")
cmd.distance("StrongHBond", "resi 371 & chain A & name O", "resi 364 & chain A & name N")
cmd.distance("StrongHBond", "resi 371 & chain A & name N", "resi 364 & chain A & name O")
cmd.distance("StrongHBond", "resi 373 & chain A & name O", "resi 362 & chain A & name N")
cmd.distance("StrongHBond", "resi 373 & chain A & name N", "resi 362 & chain A & name O")
cmd.distance("StrongHBond", "resi 375 & chain A & name O", "resi 360 & chain A & name N")
cmd.distance("StrongHBond", "resi 375 & chain A & name N", "resi 360 & chain A & name O")
cmd.distance("StrongHBond", "resi 377 & chain A & name O", "resi 358 & chain A & name N")
cmd.distance("StrongHBond", "resi 377 & chain A & name N", "resi 358 & chain A & name O")
cmd.distance("StrongHBond", "resi 379 & chain A & name O", "resi 356 & chain A & name N")
cmd.distance("StrongHBond", "resi 379 & chain A & name N", "resi 356 & chain A & name O")
cmd.distance("StrongHBond", "resi 355 & chain A & name O", "resi 333 & chain A & name N")
cmd.distance("StrongHBond", "resi 355 & chain A & name N", "resi 333 & chain A & name O")
cmd.distance("StrongHBond", "resi 357 & chain A & name O", "resi 331 & chain A & name N")
cmd.distance("StrongHBond", "resi 357 & chain A & name N", "resi 331 & chain A & name O")
cmd.distance("StrongHBond", "resi 359 & chain A & name O", "resi 329 & chain A & name N")
cmd.distance("StrongHBond", "resi 359 & chain A & name N", "resi 329 & chain A & name O")
cmd.distance("StrongHBond", "resi 361 & chain A & name O", "resi 327 & chain A & name N")
cmd.distance("StrongHBond", "resi 361 & chain A & name N", "resi 327 & chain A & name O")
cmd.distance("StrongHBond", "resi 363 & chain A & name O", "resi 325 & chain A & name N")
cmd.distance("StrongHBond", "resi 363 & chain A & name N", "resi 325 & chain A & name O")
cmd.distance("StrongHBond", "resi 326 & chain A & name O", "resi 319 & chain A & name N")
cmd.distance("StrongHBond", "resi 326 & chain A & name N", "resi 319 & chain A & name O")
cmd.distance("StrongHBond", "resi 328 & chain A & name O", "resi 316 & chain A & name N")
cmd.distance("StrongHBond", "resi 328 & chain A & name N", "resi 316 & chain A & name O")
cmd.distance("StrongHBond", "resi 330 & chain A & name O", "resi 314 & chain A & name N")
cmd.distance("StrongHBond", "resi 330 & chain A & name N", "resi 314 & chain A & name O")
cmd.distance("StrongHBond", "resi 332 & chain A & name O", "resi 312 & chain A & name N")
cmd.distance("StrongHBond", "resi 332 & chain A & name N", "resi 312 & chain A & name O")
cmd.distance("StrongHBond", "resi 334 & chain A & name O", "resi 310 & chain A & name N")
cmd.distance("StrongHBond", "resi 334 & chain A & name N", "resi 310 & chain A & name O")
cmd.distance("StrongHBond", "resi 336 & chain A & name O", "resi 308 & chain A & name N")
cmd.distance("StrongHBond", "resi 336 & chain A & name N", "resi 308 & chain A & name O")
cmd.distance("StrongHBond", "resi 338 & chain A & name O", "resi 306 & chain A & name N")
cmd.distance("StrongHBond", "resi 338 & chain A & name N", "resi 306 & chain A & name O")
cmd.distance("StrongHBond", "resi 340 & chain A & name O", "resi 304 & chain A & name N")
cmd.distance("StrongHBond", "resi 340 & chain A & name N", "resi 304 & chain A & name O")
cmd.distance("StrongHBond", "resi 303 & chain A & name O", "resi 292 & chain A & name N")
cmd.distance("StrongHBond", "resi 303 & chain A & name N", "resi 292 & chain A & name O")
cmd.distance("StrongHBond", "resi 305 & chain A & name O", "resi 290 & chain A & name N")
cmd.distance("StrongHBond", "resi 305 & chain A & name N", "resi 290 & chain A & name O")
cmd.distance("StrongHBond", "resi 307 & chain A & name O", "resi 288 & chain A & name N")
cmd.distance("StrongHBond", "resi 307 & chain A & name N", "resi 288 & chain A & name O")
cmd.distance("StrongHBond", "resi 309 & chain A & name O", "resi 286 & chain A & name N")
cmd.distance("StrongHBond", "resi 309 & chain A & name N", "resi 286 & chain A & name O")
cmd.distance("StrongHBond", "resi 311 & chain A & name O", "resi 284 & chain A & name N")
cmd.distance("StrongHBond", "resi 311 & chain A & name N", "resi 284 & chain A & name O")
cmd.distance("StrongHBond", "resi 313 & chain A & name O", "resi 282 & chain A & name N")
cmd.distance("StrongHBond", "resi 313 & chain A & name N", "resi 282 & chain A & name O")
cmd.distance("StrongHBond", "resi 315 & chain A & name O", "resi 280 & chain A & name N")
cmd.distance("StrongHBond", "resi 315 & chain A & name N", "resi 280 & chain A & name O")
cmd.distance("StrongHBond", "resi 279 & chain A & name O", "resi 276 & chain A & name N")
cmd.distance("StrongHBond", "resi 279 & chain A & name N", "resi 276 & chain A & name O")
cmd.distance("StrongHBond", "resi 281 & chain A & name O", "resi 274 & chain A & name N")
cmd.distance("StrongHBond", "resi 281 & chain A & name N", "resi 274 & chain A & name O")
cmd.distance("StrongHBond", "resi 283 & chain A & name O", "resi 272 & chain A & name N")
cmd.distance("StrongHBond", "resi 283 & chain A & name N", "resi 272 & chain A & name O")
cmd.distance("StrongHBond", "resi 285 & chain A & name O", "resi 270 & chain A & name N")
cmd.distance("StrongHBond", "resi 285 & chain A & name N", "resi 270 & chain A & name O")
cmd.distance("StrongHBond", "resi 287 & chain A & name O", "resi 268 & chain A & name N")
cmd.distance("StrongHBond", "resi 287 & chain A & name N", "resi 268 & chain A & name O")
cmd.distance("StrongHBond", "resi 289 & chain A & name O", "resi 266 & chain A & name N")
cmd.distance("StrongHBond", "resi 289 & chain A & name N", "resi 266 & chain A & name O")
cmd.distance("StrongHBond", "resi 291 & chain A & name O", "resi 264 & chain A & name N")
cmd.distance("StrongHBond", "resi 291 & chain A & name N", "resi 264 & chain A & name O")
cmd.distance("StrongHBond", "resi 267 & chain A & name O", "resi 253 & chain A & name N")
cmd.distance("StrongHBond", "resi 267 & chain A & name N", "resi 253 & chain A & name O")
cmd.distance("StrongHBond", "resi 269 & chain A & name O", "resi 251 & chain A & name N")
cmd.distance("StrongHBond", "resi 269 & chain A & name N", "resi 251 & chain A & name O")
cmd.distance("StrongHBond", "resi 271 & chain A & name O", "resi 249 & chain A & name N")
cmd.distance("StrongHBond", "resi 271 & chain A & name N", "resi 249 & chain A & name O")
cmd.distance("StrongHBond", "resi 273 & chain A & name O", "resi 247 & chain A & name N")
cmd.distance("StrongHBond", "resi 273 & chain A & name N", "resi 247 & chain A & name O")
cmd.distance("WeakHBond", "resi 212 & chain A & name O", "PseudoH236A")
cmd.distance("WeakHBond", "resi 235 & chain A & name O", "PseudoH213A")
cmd.distance("WeakHBond", "resi 214 & chain A & name O", "PseudoH234A")
cmd.distance("WeakHBond", "resi 233 & chain A & name O", "PseudoH215A")
cmd.distance("WeakHBond", "resi 216 & chain A & name O", "PseudoH232A")
cmd.distance("WeakHBond", "resi 231 & chain A & name O", "PseudoH217A")
cmd.distance("WeakHBond", "resi 218 & chain A & name O", "PseudoH230A")
cmd.distance("WeakHBond", "resi 527 & chain A & name O", "PseudoH546A")
cmd.distance("WeakHBond", "resi 547 & chain A & name O", "PseudoH526A")
cmd.distance("WeakHBond", "resi 525 & chain A & name O", "PseudoH548A")
cmd.distance("WeakHBond", "resi 549 & chain A & name O", "PseudoH524A")
cmd.distance("WeakHBond", "resi 551 & chain A & name O", "PseudoH522A")
cmd.distance("WeakHBond", "resi 517 & chain A & name O", "PseudoH523A")
cmd.distance("WeakHBond", "resi 524 & chain A & name O", "PseudoH516A")
cmd.distance("WeakHBond", "resi 515 & chain A & name O", "PseudoH525A")
cmd.distance("WeakHBond", "resi 513 & chain A & name O", "PseudoH527A")
cmd.distance("WeakHBond", "resi 528 & chain A & name O", "PseudoH512A")
cmd.distance("WeakHBond", "resi 511 & chain A & name O", "PseudoH529A")
cmd.distance("WeakHBond", "resi 530 & chain A & name O", "PseudoH510A")
cmd.distance("WeakHBond", "resi 509 & chain A & name O", "PseudoH531A")
cmd.distance("WeakHBond", "resi 369 & chain A & name O", "PseudoH365A")
cmd.distance("WeakHBond", "resi 364 & chain A & name O", "PseudoH370A")
cmd.distance("WeakHBond", "resi 371 & chain A & name O", "PseudoH363A")
cmd.distance("WeakHBond", "resi 362 & chain A & name O", "PseudoH372A")
cmd.distance("WeakHBond", "resi 373 & chain A & name O", "PseudoH361A")
cmd.distance("WeakHBond", "resi 360 & chain A & name O", "PseudoH374A")
cmd.distance("WeakHBond", "resi 375 & chain A & name O", "PseudoH359A")
cmd.distance("WeakHBond", "resi 358 & chain A & name O", "PseudoH376A")
cmd.distance("WeakHBond", "resi 377 & chain A & name O", "PseudoH357A")
cmd.distance("WeakHBond", "resi 356 & chain A & name O", "PseudoH378A")
cmd.distance("WeakHBond", "resi 379 & chain A & name O", "PseudoH355A")
cmd.distance("WeakHBond", "resi 355 & chain A & name O", "PseudoH332A")
cmd.distance("WeakHBond", "resi 331 & chain A & name O", "PseudoH356A")
cmd.distance("WeakHBond", "resi 357 & chain A & name O", "PseudoH330A")
cmd.distance("WeakHBond", "resi 329 & chain A & name O", "PseudoH358A")
cmd.distance("WeakHBond", "resi 359 & chain A & name O", "PseudoH328A")
cmd.distance("WeakHBond", "resi 327 & chain A & name O", "PseudoH360A")
cmd.distance("WeakHBond", "resi 361 & chain A & name O", "PseudoH326A")
cmd.distance("WeakHBond", "resi 325 & chain A & name O", "PseudoH362A")
cmd.distance("WeakHBond", "resi 363 & chain A & name O", "PseudoH324A")
cmd.distance("WeakHBond", "resi 324 & chain A & name O", "PseudoH320A")
cmd.distance("WeakHBond", "resi 319 & chain A & name O", "PseudoH325A")
cmd.distance("WeakHBond", "resi 326 & chain A & name O", "PseudoH317A")
cmd.distance("WeakHBond", "resi 316 & chain A & name O", "PseudoH327A")
cmd.distance("WeakHBond", "resi 328 & chain A & name O", "PseudoH315A")
cmd.distance("WeakHBond", "resi 314 & chain A & name O", "PseudoH329A")
cmd.distance("WeakHBond", "resi 330 & chain A & name O", "PseudoH313A")
cmd.distance("WeakHBond", "resi 312 & chain A & name O", "PseudoH331A")
cmd.distance("WeakHBond", "resi 332 & chain A & name O", "PseudoH311A")
cmd.distance("WeakHBond", "resi 310 & chain A & name O", "PseudoH333A")
cmd.distance("WeakHBond", "resi 334 & chain A & name O", "PseudoH309A")
cmd.distance("WeakHBond", "resi 308 & chain A & name O", "PseudoH335A")
cmd.distance("WeakHBond", "resi 336 & chain A & name O", "PseudoH307A")
cmd.distance("WeakHBond", "resi 306 & chain A & name O", "PseudoH337A")
cmd.distance("WeakHBond", "resi 338 & chain A & name O", "PseudoH305A")
cmd.distance("WeakHBond", "resi 304 & chain A & name O", "PseudoH339A")
cmd.distance("WeakHBond", "resi 340 & chain A & name O", "PseudoH303A")
cmd.distance("WeakHBond", "resi 303 & chain A & name O", "PseudoH291A")
cmd.distance("WeakHBond", "resi 290 & chain A & name O", "PseudoH304A")
cmd.distance("WeakHBond", "resi 305 & chain A & name O", "PseudoH289A")
cmd.distance("WeakHBond", "resi 288 & chain A & name O", "PseudoH306A")
cmd.distance("WeakHBond", "resi 307 & chain A & name O", "PseudoH287A")
cmd.distance("WeakHBond", "resi 286 & chain A & name O", "PseudoH308A")
cmd.distance("WeakHBond", "resi 309 & chain A & name O", "PseudoH285A")
cmd.distance("WeakHBond", "resi 284 & chain A & name O", "PseudoH310A")
cmd.distance("WeakHBond", "resi 311 & chain A & name O", "PseudoH283A")
cmd.distance("WeakHBond", "resi 282 & chain A & name O", "PseudoH312A")
cmd.distance("WeakHBond", "resi 313 & chain A & name O", "PseudoH281A")
cmd.distance("WeakHBond", "resi 280 & chain A & name O", "PseudoH314A")
cmd.distance("WeakHBond", "resi 315 & chain A & name O", "PseudoH279A")
cmd.distance("WeakHBond", "resi 279 & chain A & name O", "PseudoH275A")
cmd.distance("WeakHBond", "resi 274 & chain A & name O", "PseudoH280A")
cmd.distance("WeakHBond", "resi 281 & chain A & name O", "PseudoH273A")
cmd.distance("WeakHBond", "resi 272 & chain A & name O", "PseudoH282A")
cmd.distance("WeakHBond", "resi 283 & chain A & name O", "PseudoH271A")
cmd.distance("WeakHBond", "resi 270 & chain A & name O", "PseudoH284A")
cmd.distance("WeakHBond", "resi 268 & chain A & name O", "PseudoH286A")
cmd.distance("WeakHBond", "resi 287 & chain A & name O", "PseudoH267A")
cmd.distance("WeakHBond", "resi 266 & chain A & name O", "PseudoH288A")
cmd.distance("WeakHBond", "resi 289 & chain A & name O", "PseudoH265A")
cmd.distance("WeakHBond", "resi 264 & chain A & name O", "PseudoH290A")
cmd.distance("WeakHBond", "resi 265 & chain A & name O", "PseudoH254A")
cmd.distance("WeakHBond", "resi 253 & chain A & name O", "PseudoH266A")
cmd.distance("WeakHBond", "resi 267 & chain A & name O", "PseudoH252A")
cmd.distance("WeakHBond", "resi 251 & chain A & name O", "PseudoH268A")
cmd.distance("WeakHBond", "resi 269 & chain A & name O", "PseudoH250A")
cmd.distance("WeakHBond", "resi 249 & chain A & name O", "PseudoH270A")
cmd.distance("WeakHBond", "resi 271 & chain A & name O", "PseudoH248A")
cmd.distance("WeakHBond", "resi 247 & chain A & name O", "PseudoH272A")
cmd.distance("NonHBond", "resi 213 & chain A & name CB", "resi 236 & chain A & name CB")
cmd.distance("NonHBond", "resi 215 & chain A & name CB", "resi 234 & chain A & name CB")
cmd.distance("NonHBond", "resi 217 & chain A & name CB", "resi 232 & chain A & name CB")
cmd.distance("NonHBond", "resi 546 & chain A & name CB", "resi 528 & chain A & name CB")
cmd.distance("NonHBond", "resi 548 & chain A & name CB", "resi 526 & chain A & name CB")
cmd.distance("NonHBond", "resi 550 & chain A & name CB", "resi 524 & chain A & name CB")
cmd.distance("NonHBond", "resi 552 & chain A & name CB", "resi 522 & chain A & name CB")
cmd.distance("NonHBond", "resi 523 & chain A & name CB", "resi 518 & chain A & name CB")
cmd.distance("NonHBond", "resi 525 & chain A & name CB", "resi 516 & chain A & name CB")
cmd.distance("NonHBond", "resi 529 & chain A & name CB", "resi 512 & chain A & name CB")
cmd.distance("NonHBond", "resi 531 & chain A & name CB", "PseudoR510A")
cmd.distance("NonHBond", "resi 370 & chain A & name CB", "resi 365 & chain A & name CB")
cmd.distance("NonHBond", "resi 372 & chain A & name CB", "resi 363 & chain A & name CB")
cmd.distance("NonHBond", "resi 374 & chain A & name CB", "resi 361 & chain A & name CB")
cmd.distance("NonHBond", "resi 376 & chain A & name CB", "PseudoR359A")
cmd.distance("NonHBond", "resi 378 & chain A & name CB", "resi 357 & chain A & name CB")
cmd.distance("NonHBond", "resi 356 & chain A & name CB", "resi 332 & chain A & name CB")
cmd.distance("NonHBond", "resi 358 & chain A & name CB", "PseudoR330A")
cmd.distance("NonHBond", "resi 360 & chain A & name CB", "resi 328 & chain A & name CB")
cmd.distance("NonHBond", "resi 362 & chain A & name CB", "resi 326 & chain A & name CB")
cmd.distance("NonHBond", "resi 364 & chain A & name CB", "resi 324 & chain A & name CB")
cmd.distance("NonHBond", "resi 325 & chain A & name CB", "resi 320 & chain A & name CB")
cmd.distance("NonHBond", "resi 327 & chain A & name CB", "resi 317 & chain A & name CB")
cmd.distance("NonHBond", "resi 329 & chain A & name CB", "resi 315 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR331A", "resi 313 & chain A & name CB")
cmd.distance("NonHBond", "resi 333 & chain A & name CB", "PseudoR311A")
cmd.distance("NonHBond", "resi 335 & chain A & name CB", "resi 309 & chain A & name CB")
cmd.distance("NonHBond", "resi 337 & chain A & name CB", "resi 307 & chain A & name CB")
cmd.distance("NonHBond", "resi 339 & chain A & name CB", "PseudoR305A")
cmd.distance("NonHBond", "resi 304 & chain A & name CB", "resi 291 & chain A & name CB")
cmd.distance("NonHBond", "resi 306 & chain A & name CB", "resi 289 & chain A & name CB")
cmd.distance("NonHBond", "resi 308 & chain A & name CB", "resi 287 & chain A & name CB")
cmd.distance("NonHBond", "resi 310 & chain A & name CB", "resi 285 & chain A & name CB")
cmd.distance("NonHBond", "resi 312 & chain A & name CB", "resi 283 & chain A & name CB")
cmd.distance("NonHBond", "resi 314 & chain A & name CB", "resi 281 & chain A & name CB")
cmd.distance("NonHBond", "resi 316 & chain A & name CB", "resi 279 & chain A & name CB")
cmd.distance("NonHBond", "resi 280 & chain A & name CB", "resi 275 & chain A & name CB")
cmd.distance("NonHBond", "resi 282 & chain A & name CB", "resi 273 & chain A & name CB")
cmd.distance("NonHBond", "resi 284 & chain A & name CB", "resi 271 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR286A", "resi 269 & chain A & name CB")
cmd.distance("NonHBond", "resi 288 & chain A & name CB", "resi 267 & chain A & name CB")
cmd.distance("NonHBond", "resi 290 & chain A & name CB", "resi 265 & chain A & name CB")
cmd.distance("NonHBond", "resi 266 & chain A & name CB", "resi 254 & chain A & name CB")
cmd.distance("NonHBond", "resi 268 & chain A & name CB", "resi 252 & chain A & name CB")
cmd.distance("NonHBond", "resi 270 & chain A & name CB", "resi 250 & chain A & name CB")
cmd.distance("NonHBond", "resi 272 & chain A & name CB", "resi 248 & chain A & name CB")
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
