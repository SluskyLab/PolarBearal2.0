from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/7AHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Bstrand1", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Cstrand3", "resi 135+136+137+138+139+140+141+142+143+144+145+146+147 & chain C ")
cmd.color ("teal", "Cstrand3")


cmd.select("Cstrand4", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Dstrand5", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain D ")
cmd.color ("blue", "Dstrand5")


cmd.select("Dstrand6", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain D ")
cmd.color ("red", "Dstrand6")


cmd.select("Estrand7", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain E ")
cmd.color ("green", "Estrand7")


cmd.select("Estrand8", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain E ")
cmd.color ("orange", "Estrand8")


cmd.select("Fstrand9", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain F ")
cmd.color ("teal", "Fstrand9")


cmd.select("Fstrand10", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain F ")
cmd.color ("yellow", "Fstrand10")


cmd.select("Gstrand11", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain G ")
cmd.color ("blue", "Gstrand11")


cmd.select("Gstrand12", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain G ")
cmd.color ("red", "Gstrand12")


cmd.select("Astrand13", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
