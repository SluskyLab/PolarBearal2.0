from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5M9B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 156+157+158+159+160+672+673+161+674+162+675+622+623+163+676+624+164+677+625+582+678+581+165+626+679+584+627+583+166+585+518+519+586+628+629+520+521+587+588+630+523+522+631+525+589+524+590+527+526+529+593+532+528+591+533+592+530+531+534+594+595+535+494+493+492+491 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 174+175+176+177+178+179+180+181+182+183+184+185+186 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 189+190+191+192+193+194+195+196+197+198+199+200 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 229+230+231+232+233+234+235+236+237+238+239+240+241+242 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 247+248+249+250+251+252+253+254+255+256+257+258+259+260+261 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 284+285+286+287+288+289+290+291+292+293+294+295+296+297+298 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 361+362+363+364+365+366+367+368+369+370+371+372+373+374+375 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 421+422+423+424+425+426+427+428+429+430+431+432 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 436+437+438+439+440+441+442+443+444+445+446+447+448+449+450 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 453+454+455+456+457+458+459+460+461+462+463+464 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 554+555+556+478+479+557+477+476+558+559+560+561+562+563+502+564+503+565+504+566+505+567+506+568+507+608+609+508+569+657+570+509+610+658+659+611+571+510+712+572+660+612+511+661+713+613+512+714+573+662+574+715+716+663+513+614+514+615+717+718+664+575+665+515+719+616+720+576+666+667+668+669 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
