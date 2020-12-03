from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+17+18+19+20+21+22+23+24 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 29+30+31+32+163+33+162+164+165+34+166+35+167+168+169+170+171+172+173 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 99+100+101+102+103+104+105+106+107+108+109 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 86+87+88+89+90+91+92+93+94+95+96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 50+51+52+53+54+55+56+57+58 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 134+135+136+137+138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
