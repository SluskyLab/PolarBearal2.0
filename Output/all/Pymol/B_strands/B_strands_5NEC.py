from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NEC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 157+158+159+160+161+162+163+164+165 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 170+171+172+173+174+175+176+177+178+179+180 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 651+652+653+654+655+656+657+658+659+660 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 637+638+639+640+641+642+643+644+645+646+647+648 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 594+595+596+597+598+599+600+601+602+603+604+605+606+607 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 577+578+579+580+581+582+583+584+585+586+587+588+589 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 548+549+550+551+552+553+554+555+556+557+558+559 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 532+533+534+535+536+537+538+539+540+541+542+543 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 492+493+494+495+496+497+498+499+500+501 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 469+470+471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 355+356+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+372+373+374+375+376+377 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 294+295+296+297+298+299+300+301+302+303+304+305+306+307+308+309+310+311+312+313+314 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 274+275+276+277+278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 223+224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 676+677+678+679+680+681+682+683+684+685+686 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216+217 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 691+692+693+694+695+696+697+698 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 185+186+187+188+189+190+191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 722+723+724+725+726+727+728+729+730+731 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
