from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 147+147+148+149+150+151+152+153+154+155+156+157+158+165+166+167+168+169+170+171+172+173+174+175+176+181+182+183+184+185+186+187+188+191+192+193+194+201+202+203+204+207+208+209+210+211+212+213+214+215+216+217+222+223+224+225+226+227+228+229+230+240+241+242+243+244+245+246+247+248+336+337+338+339+340+341+342+343+344+356+357+358+359+360+361+362+363+364+365+370+371+372+373+374+375+376+377+378+379+382+383+384+385+386+387+388+389+390+391+392+398+399+400+401+402+403+404+405+406+407+408+409+415+416+417+418+419+420+421+422+423+424+425+437+438+439+440+441+442+443+444+467+468+469+470+471+472+473+474+475+476+477+478+485+486+487+488+489+490+491+492+493+494+495+501+502+503+504+505+506+507+508+509+510+521+522+523+524+525+526+527+538+539+540+541+542+543+544+545+552+553+554+555+556+557+563+564+565+566+567+568+569+570+571+572+579+580+581+582+583+584+585+586+587+588+594+595+596+597+598+599+600+601+602+603+604+605+609+610+611+612+613+614+615+616+617+618+623+624+625+626+627+628+629+630+631+632+633+634 & chain A or resi 202+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216+181+182+183+184+185+186+187+188+189+190+191+192+193+222+223+224+225+226+227+228+229+230+231+239+240+241+242+243+244+245+246+247+248+336+337+338+339+340+341+342+343+344+356+357+358+359+360+361+362+363+364+365+370+371+372+373+375+376+377+378+379+382+383+384+385+386+387+388+389+390+391+399+400+401+402+403+404+405+406+407+408+409+415+416+417+418+419+420+421+422+439+440+441+442+443+444+467+468+469+470+471+472+473+489+490+491+492+493+494+495+501+502+503+504+505+506+507+508+522+523+524+525+526+527+528+537+538+539+540+541+542+555+556+557+564+565+566 & chain B")
cmd.load_cgo( [9.0, 24.073162,86.93202,50.513596, 28.79647, -21.426956, 49.532692, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
