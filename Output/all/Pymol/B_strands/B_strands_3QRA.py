from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QRA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30+31+32+33+34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 169+170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 155+156+157+158+159+160+161+162+163+164+165+166 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 53+54+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 67+68+69+70+71+72+73+74+75+76+77+78 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
