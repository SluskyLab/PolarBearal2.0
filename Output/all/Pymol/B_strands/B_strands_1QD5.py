from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QD5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 39+40+41+42+43+44+45 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 236+237+238+239+240+241+242+243+244+245 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 221+222+223+224+225+226+227+228+229+230 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 206+207+208+209+210+211+212+213+214 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 169+170+171+172+173 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 154+155+156+157+158+159+160+161+162+163+164+165+166 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 131+132+133+134+135+136+137+138+139+140+141+142+143+144 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 86+87+88+89+90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 197+198+199+200+201+202+203 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 65+66+67+68+69+70+71+72+73+74+75+76+77+78+79 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
