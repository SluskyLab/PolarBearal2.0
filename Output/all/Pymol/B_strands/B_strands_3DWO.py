from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DWO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 423+424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 324+325+326+327+328+329+330+336+337+338+339+340+341+342+343+344+345+346 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 226+227+228+229+230+231+232+233+239+240+241+242+243+244+245+246+247+248 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 300+301+302+303+304+305+306+307+308+309+316+317+318+319+320+321 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216+217+218+219+220 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 158+159+160+161+162+163+164+165+166+167+168+169+170+171+172+173+174+175+176+177 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 275+276+277+278+279+280+281+287+288+289+290+291+292+293+294+295 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 93+94+95+96+97+98+99+100+101+102+103+104+105 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 351+352+353+354+355+356+357+358+359+360 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 378+379+380+381+382+383+384+385+386+387+388 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 395+396+397+398+399+400+401+402+403+404+405+406 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
