from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6R2Q.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 680+681+682+683+684+685+686+687+688+689+690+691+692+693+694 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 644+645+646+647+648+649+650+651+652+653+654+655+656+657+658+659 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 625+626+627+628+629+630+631+632+633+634+635+636+637+638 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 572+573+574+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+590 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 598+599+600+601+602+603+604+605+606+607+608+609+610+611+612+613+614+615+616+617+618+619+620+621 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562+563 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 506+507+508+509+510+511+512+513+514+515+516+517+518 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 525+526+527+528+529+530+531+532+533+534+535+536+537+538+539+540 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 489+490+491+492+493+494+495+496+497+498+499+500 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 452+453+454+455+456+457+458+459+460+461+462+463+464 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 396+397+398+399+400+401+402+403+404+405+406+407 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 433+434+435+436+437+438+439+440+441+442+443+444+445 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 356+357+358+359+360+361+362+363+364+365+366+367+368+369 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 288+289+290+291+292+293+294+295+296+297+298+299 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 246+247+248+249+250+251+252+253+254+255+256+257+258+259 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+242 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 196+197+198+199+200+201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 173+174+175+176+177+178+179+180+181+182+183+184+185+186+187+188+189+190+191 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 121+122+123+124+125+126+127+128+129+130+131+132+133+134+135 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 110+111+112+113 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 85+86+87+88 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 99+100+101+102 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
