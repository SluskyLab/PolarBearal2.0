from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6BPM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 182+183+184+185+186+187+188+189+190 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 751+752+753+754+755+756+757+758+759 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 719+720+721+722+723+724+725+726 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 704+705+706+707+708+709+710+711+712+713+714 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 675+676+677+678+679+680+681+682+683+684 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 661+662+663+664+665+666+667+668+669 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 628+629+630+631+632+633+634+635+636+637+638+639+640+641+642+643 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 605+606+607+608+609+610+611+612+613+614+615+616+617+618+619+620+621+622+623+624+625 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 527+528+529+530+531+532+533+534+535+536+537+538 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 582+583+584+585+586+587+588+589+590+591+592+593+594+595+596+597+598+599 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 500+501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520+521+522 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 460+461+462+463+464+465+466+467+468+469+470+471+472+473+474+475+476+477+478+479+480 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 434+435+436+437+438+439+440+441+442+443+444+445+446+447+448+449+450+451+452+453+454+455 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 391+392+393+394+395+396+397+398+399+400+401+402+403+404+405+406+407+408+409+410 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 360+361+362+363+364+365+366+367+368+369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+384+385+386 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 247+248+249+250+251+252+253+254+255+256+257+258+259+260 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 229+230+231+232+233+234+235+236+237+238+239+240+241 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 209+210+211+212+213+214+215+216+217+218+219+220+221 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 194+195+196+197+198+199+200+201+202+203+204 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
