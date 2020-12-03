from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6E4V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 191+192+193+194+195+196+197+198+199 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 720+721+722+723+724+725+726+727+728 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 691+692+693+694+695+696+697+698 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 676+677+678+679+680+681+682+683+684+685+686 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 646+647+648+649+650+651+652+653+654+655 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 630+631+632+633+634+635+636+637+638+639 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 604+605+606+607+608+609+610+611+612+613+614+615+616 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 588+589+590+591+592+593+594+595+596+597+598+599+600+601 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 506+507+508+552+551+553+509+554+550+555+510+556+511+557+512+513+558+559+514+560+515+561+516+562+517+563+564+565+566+567+568+569+570+571 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 467+468+469+470+471+472+473+474+475+476+477+478+479+480+481 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 579+580+581+582+583+584+487+486+532+488+489+533+490+534+491+535+492+493+536+494+537+495+538+496+497+539+540+498+499+541+542+500+543+501+544+545 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 443+444+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 395+396+397+398+399+400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 368+369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+384+385+386+387+388+389+390+391+392 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 257+258+259+260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 239+240+241+242+243+244+245+246+247+248+249+250+251+252+253 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 220+221+222+223+224+225+226+227+228+229+230+231+232 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 203+204+205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
