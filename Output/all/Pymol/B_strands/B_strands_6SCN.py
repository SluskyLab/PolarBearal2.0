from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("astrand0", "resi 276+277+278 & chain a ")
cmd.color ("red", "astrand0")


cmd.select("astrand1", "resi 374+375+376 & chain a ")
cmd.color ("green", "astrand1")


cmd.select("bstrand2", "resi 276+277+278 & chain b ")
cmd.color ("orange", "bstrand2")


cmd.select("bstrand3", "resi 374+375+376 & chain b ")
cmd.color ("teal", "bstrand3")


cmd.select("cstrand4", "resi 276+277+278 & chain c ")
cmd.color ("yellow", "cstrand4")


cmd.select("cstrand5", "resi 374+375+376 & chain c ")
cmd.color ("blue", "cstrand5")


cmd.select("dstrand6", "resi 276+277+278 & chain d ")
cmd.color ("red", "dstrand6")


cmd.select("dstrand7", "resi 374+375+376 & chain d ")
cmd.color ("green", "dstrand7")


cmd.select("estrand8", "resi 276+277+278 & chain e ")
cmd.color ("orange", "estrand8")


cmd.select("estrand9", "resi 374+375+376 & chain e ")
cmd.color ("teal", "estrand9")


cmd.select("fstrand10", "resi 276+277+278 & chain f ")
cmd.color ("yellow", "fstrand10")


cmd.select("fstrand11", "resi 374+375+376 & chain f ")
cmd.color ("blue", "fstrand11")


cmd.select("gstrand12", "resi 276+277+278 & chain g ")
cmd.color ("red", "gstrand12")


cmd.select("gstrand13", "resi 374+375+376 & chain g ")
cmd.color ("green", "gstrand13")


cmd.select("Astrand14", "resi 276+277+278 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 374+375+376 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Bstrand16", "resi 276+277+278 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 374+375+376 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Cstrand18", "resi 276+277+278 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 374+375+376 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Dstrand20", "resi 276+277+278 & chain D ")
cmd.color ("orange", "Dstrand20")


cmd.select("Dstrand21", "resi 374+375+376 & chain D ")
cmd.color ("teal", "Dstrand21")


cmd.select("Estrand22", "resi 276+277+278 & chain E ")
cmd.color ("yellow", "Estrand22")


cmd.select("Estrand23", "resi 374+375+376 & chain E ")
cmd.color ("blue", "Estrand23")


cmd.select("Fstrand24", "resi 276+277+278 & chain F ")
cmd.color ("red", "Fstrand24")


cmd.select("Fstrand25", "resi 374+375+376 & chain F ")
cmd.color ("green", "Fstrand25")


cmd.select("Gstrand26", "resi 276+277+278 & chain G ")
cmd.color ("orange", "Gstrand26")


cmd.select("Gstrand27", "resi 374+375+376 & chain G ")
cmd.color ("teal", "Gstrand27")


cmd.select("Hstrand28", "resi 276+277+278 & chain H ")
cmd.color ("yellow", "Hstrand28")


cmd.select("Hstrand29", "resi 374+375+376 & chain H ")
cmd.color ("blue", "Hstrand29")


cmd.select("Istrand30", "resi 276+277+278 & chain I ")
cmd.color ("red", "Istrand30")


cmd.select("Istrand31", "resi 374+375+376 & chain I ")
cmd.color ("green", "Istrand31")


cmd.select("Jstrand32", "resi 276+277+278 & chain J ")
cmd.color ("orange", "Jstrand32")


cmd.select("Jstrand33", "resi 374+375+376 & chain J ")
cmd.color ("teal", "Jstrand33")


cmd.select("Kstrand34", "resi 276+277+278 & chain K ")
cmd.color ("yellow", "Kstrand34")


cmd.select("Kstrand35", "resi 374+375+376 & chain K ")
cmd.color ("blue", "Kstrand35")


cmd.select("Lstrand36", "resi 276+277+278 & chain L ")
cmd.color ("red", "Lstrand36")


cmd.select("Lstrand37", "resi 374+375+376 & chain L ")
cmd.color ("green", "Lstrand37")


cmd.select("Mstrand38", "resi 276+277+278 & chain M ")
cmd.color ("orange", "Mstrand38")


cmd.select("Mstrand39", "resi 374+375+376 & chain M ")
cmd.color ("teal", "Mstrand39")


cmd.select("Nstrand40", "resi 276+277+278 & chain N ")
cmd.color ("yellow", "Nstrand40")


cmd.select("Nstrand41", "resi 374+375+376 & chain N ")
cmd.color ("blue", "Nstrand41")


cmd.select("Ostrand42", "resi 276+277+278 & chain O ")
cmd.color ("red", "Ostrand42")


cmd.select("Ostrand43", "resi 374+375+376 & chain O ")
cmd.color ("green", "Ostrand43")


cmd.select("Pstrand44", "resi 276+277+278 & chain P ")
cmd.color ("orange", "Pstrand44")


cmd.select("Pstrand45", "resi 374+375+376 & chain P ")
cmd.color ("teal", "Pstrand45")


cmd.select("Qstrand46", "resi 276+277+278 & chain Q ")
cmd.color ("yellow", "Qstrand46")


cmd.select("Qstrand47", "resi 374+375+376 & chain Q ")
cmd.color ("blue", "Qstrand47")


cmd.select("Rstrand48", "resi 276+277+278 & chain R ")
cmd.color ("red", "Rstrand48")


cmd.select("Rstrand49", "resi 374+375+376 & chain R ")
cmd.color ("green", "Rstrand49")


cmd.select("Sstrand50", "resi 276+277+278 & chain S ")
cmd.color ("orange", "Sstrand50")


cmd.select("Sstrand51", "resi 374+375+376 & chain S ")
cmd.color ("teal", "Sstrand51")


cmd.select("Tstrand52", "resi 276+277+278 & chain T ")
cmd.color ("yellow", "Tstrand52")


cmd.select("Tstrand53", "resi 374+375+376 & chain T ")
cmd.color ("blue", "Tstrand53")


cmd.select("Ustrand54", "resi 276+277+278 & chain U ")
cmd.color ("red", "Ustrand54")


cmd.select("Ustrand55", "resi 374+375+376 & chain U ")
cmd.color ("green", "Ustrand55")


cmd.select("Vstrand56", "resi 276+277+278 & chain V ")
cmd.color ("orange", "Vstrand56")


cmd.select("Vstrand57", "resi 374+375+376 & chain V ")
cmd.color ("teal", "Vstrand57")


cmd.select("Wstrand58", "resi 276+277+278 & chain W ")
cmd.color ("yellow", "Wstrand58")


cmd.select("Wstrand59", "resi 374+375+376 & chain W ")
cmd.color ("blue", "Wstrand59")


cmd.select("Xstrand60", "resi 276+277+278 & chain X ")
cmd.color ("red", "Xstrand60")


cmd.select("Xstrand61", "resi 374+375+376 & chain X ")
cmd.color ("green", "Xstrand61")


cmd.select("Ystrand62", "resi 276+277+278 & chain Y ")
cmd.color ("orange", "Ystrand62")


cmd.select("Ystrand63", "resi 374+375+376 & chain Y ")
cmd.color ("teal", "Ystrand63")


cmd.select("Zstrand64", "resi 276+277+278 & chain Z ")
cmd.color ("yellow", "Zstrand64")


cmd.select("Zstrand65", "resi 374+375+376 & chain Z ")
cmd.color ("blue", "Zstrand65")


cmd.select("barrel", "astrand* or bstrand* or cstrand* or dstrand* or estrand* or fstrand* or gstrand* or Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand* or Qstrand* or Rstrand* or Sstrand* or Tstrand* or Ustrand* or Vstrand* or Wstrand* or Xstrand* or Ystrand* or Zstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
