from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6V81.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 164+165+166+167+168+169+170+171+172 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 688+689+690+691+692+693+694+695+696+697+698 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 651+652+653+654+655+656+657+658+659+660 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 635+636+637+638+639+640+641+642+643+644+645+646+647+648 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 611+612+613+614+615+616+617+618+619 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 596+597+598+599+600+601+602+603+604 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 562+563+564+565+566+567+568+569+570+571+572+573+574+575 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 545+546+547+548+549+550+551+552+553+554+555+556+557+558 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 500+501+502+503+504+505+506+507+508+509 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 512+513+514+515+516+517+518+519+520+521+522+523 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 461+462+463+464+465+466+467+468 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 440+441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427+428 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 386+387+388+389+390+391+392+393+394+395+396+397+398+399+400+401+402+403+404+405+406+407+408 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366+367+368 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 293+294+295+296+297+298+299+300+301+302+303+304+305+306+307+308+309 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 273+274+275+276+277+278+279+280+281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 234+235+236+237+238+239+240+241+242+243+244+245+246+247 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 176+177+178+179+180+181+182+183+184+185+186 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
