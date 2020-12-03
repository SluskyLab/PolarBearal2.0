from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("astrand3", "resi 276+277+278 & chain a ")


cmd.select("astrand6", "resi 374+375+376 & chain a ")


cmd.select("bstrand23", "resi 276+277+278 & chain b ")


cmd.select("bstrand26", "resi 374+375+376 & chain b ")


cmd.select("cstrand43", "resi 276+277+278 & chain c ")


cmd.select("cstrand46", "resi 374+375+376 & chain c ")


cmd.select("dstrand62", "resi 276+277+278 & chain d ")


cmd.select("dstrand65", "resi 374+375+376 & chain d ")


cmd.select("estrand82", "resi 276+277+278 & chain e ")


cmd.select("estrand85", "resi 374+375+376 & chain e ")


cmd.select("fstrand101", "resi 276+277+278 & chain f ")


cmd.select("fstrand104", "resi 374+375+376 & chain f ")


cmd.select("gstrand118", "resi 276+277+278 & chain g ")


cmd.select("gstrand121", "resi 374+375+376 & chain g ")


cmd.select("Astrand13", "resi 276+277+278 & chain A ")


cmd.select("Astrand16", "resi 374+375+376 & chain A ")


cmd.select("Bstrand33", "resi 276+277+278 & chain B ")


cmd.select("Bstrand36", "resi 374+375+376 & chain B ")


cmd.select("Cstrand53", "resi 276+277+278 & chain C ")


cmd.select("Cstrand56", "resi 374+375+376 & chain C ")


cmd.select("Dstrand72", "resi 276+277+278 & chain D ")


cmd.select("Dstrand75", "resi 374+375+376 & chain D ")


cmd.select("Estrand91", "resi 276+277+278 & chain E ")


cmd.select("Estrand94", "resi 374+375+376 & chain E ")


cmd.select("Fstrand111", "resi 276+277+278 & chain F ")


cmd.select("Fstrand114", "resi 374+375+376 & chain F ")


cmd.select("Gstrand128", "resi 276+277+278 & chain G ")


cmd.select("Gstrand131", "resi 374+375+376 & chain G ")


cmd.select("Hstrand137", "resi 276+277+278 & chain H ")


cmd.select("Hstrand140", "resi 374+375+376 & chain H ")


cmd.select("Istrand147", "resi 276+277+278 & chain I ")


cmd.select("Istrand150", "resi 374+375+376 & chain I ")


cmd.select("Jstrand157", "resi 276+277+278 & chain J ")


cmd.select("Jstrand160", "resi 374+375+376 & chain J ")


cmd.select("Kstrand164", "resi 276+277+278 & chain K ")


cmd.select("Kstrand167", "resi 374+375+376 & chain K ")


cmd.select("Lstrand174", "resi 276+277+278 & chain L ")


cmd.select("Lstrand177", "resi 374+375+376 & chain L ")


cmd.select("Mstrand183", "resi 276+277+278 & chain M ")


cmd.select("Mstrand186", "resi 374+375+376 & chain M ")


cmd.select("Nstrand193", "resi 276+277+278 & chain N ")


cmd.select("Nstrand196", "resi 374+375+376 & chain N ")


cmd.select("Ostrand203", "resi 276+277+278 & chain O ")


cmd.select("Ostrand206", "resi 374+375+376 & chain O ")


cmd.select("Pstrand212", "resi 276+277+278 & chain P ")


cmd.select("Pstrand215", "resi 374+375+376 & chain P ")


cmd.select("Qstrand222", "resi 276+277+278 & chain Q ")


cmd.select("Qstrand225", "resi 374+375+376 & chain Q ")


cmd.select("Rstrand232", "resi 276+277+278 & chain R ")


cmd.select("Rstrand235", "resi 374+375+376 & chain R ")


cmd.select("Sstrand241", "resi 276+277+278 & chain S ")


cmd.select("Sstrand244", "resi 374+375+376 & chain S ")


cmd.select("Tstrand251", "resi 276+277+278 & chain T ")


cmd.select("Tstrand254", "resi 374+375+376 & chain T ")


cmd.select("Ustrand261", "resi 276+277+278 & chain U ")


cmd.select("Ustrand264", "resi 374+375+376 & chain U ")


cmd.select("Vstrand268", "resi 276+277+278 & chain V ")


cmd.select("Vstrand271", "resi 374+375+376 & chain V ")


cmd.select("Wstrand278", "resi 276+277+278 & chain W ")


cmd.select("Wstrand281", "resi 374+375+376 & chain W ")


cmd.select("Xstrand287", "resi 276+277+278 & chain X ")


cmd.select("Xstrand290", "resi 374+375+376 & chain X ")


cmd.select("Ystrand297", "resi 276+277+278 & chain Y ")


cmd.select("Ystrand300", "resi 374+375+376 & chain Y ")


cmd.select("Zstrand307", "resi 276+277+278 & chain Z ")


cmd.select("Zstrand310", "resi 374+375+376 & chain Z ")


cmd.select("barrel", "astrand* or bstrand* or cstrand* or dstrand* or estrand* or fstrand* or gstrand* or Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand* or Qstrand* or Rstrand* or Sstrand* or Tstrand* or Ustrand* or Vstrand* or Wstrand* or Xstrand* or Ystrand* or Zstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 276 & chain a")

cmd.select ("Outward", "resi 276 & chain a", merge=1)

cmd.color ("blue", "resi 277 & chain a")

cmd.select ("Outward", "resi 277 & chain a", merge=1)

cmd.color ("blue", "resi 278 & chain a")

cmd.select ("Outward", "resi 278 & chain a", merge=1)

cmd.color ("blue", "resi 374 & chain a")

cmd.select ("Outward", "resi 374 & chain a", merge=1)

cmd.color ("blue", "resi 375 & chain a")

cmd.select ("Outward", "resi 375 & chain a", merge=1)

cmd.color ("blue", "resi 376 & chain a")

cmd.select ("Outward", "resi 376 & chain a", merge=1)

cmd.color ("blue", "resi 276 & chain b")

cmd.select ("Outward", "resi 276 & chain b", merge=1)

cmd.color ("blue", "resi 277 & chain b")

cmd.select ("Outward", "resi 277 & chain b", merge=1)

cmd.color ("blue", "resi 278 & chain b")

cmd.select ("Outward", "resi 278 & chain b", merge=1)

cmd.color ("blue", "resi 374 & chain b")

cmd.select ("Outward", "resi 374 & chain b", merge=1)

cmd.color ("blue", "resi 375 & chain b")

cmd.select ("Outward", "resi 375 & chain b", merge=1)

cmd.color ("blue", "resi 376 & chain b")

cmd.select ("Outward", "resi 376 & chain b", merge=1)

cmd.color ("blue", "resi 276 & chain c")

cmd.select ("Outward", "resi 276 & chain c", merge=1)

cmd.color ("blue", "resi 277 & chain c")

cmd.select ("Outward", "resi 277 & chain c", merge=1)

cmd.color ("blue", "resi 278 & chain c")

cmd.select ("Outward", "resi 278 & chain c", merge=1)

cmd.color ("blue", "resi 374 & chain c")

cmd.select ("Outward", "resi 374 & chain c", merge=1)

cmd.color ("blue", "resi 375 & chain c")

cmd.select ("Outward", "resi 375 & chain c", merge=1)

cmd.color ("blue", "resi 376 & chain c")

cmd.select ("Outward", "resi 376 & chain c", merge=1)

cmd.color ("blue", "resi 276 & chain d")

cmd.select ("Outward", "resi 276 & chain d", merge=1)

cmd.color ("blue", "resi 277 & chain d")

cmd.select ("Outward", "resi 277 & chain d", merge=1)

cmd.color ("blue", "resi 278 & chain d")

cmd.select ("Outward", "resi 278 & chain d", merge=1)

cmd.color ("blue", "resi 374 & chain d")

cmd.select ("Outward", "resi 374 & chain d", merge=1)

cmd.color ("blue", "resi 375 & chain d")

cmd.select ("Outward", "resi 375 & chain d", merge=1)

cmd.color ("blue", "resi 376 & chain d")

cmd.select ("Outward", "resi 376 & chain d", merge=1)

cmd.color ("blue", "resi 276 & chain e")

cmd.select ("Outward", "resi 276 & chain e", merge=1)

cmd.color ("blue", "resi 277 & chain e")

cmd.select ("Outward", "resi 277 & chain e", merge=1)

cmd.color ("blue", "resi 278 & chain e")

cmd.select ("Outward", "resi 278 & chain e", merge=1)

cmd.color ("blue", "resi 374 & chain e")

cmd.select ("Outward", "resi 374 & chain e", merge=1)

cmd.color ("blue", "resi 375 & chain e")

cmd.select ("Outward", "resi 375 & chain e", merge=1)

cmd.color ("blue", "resi 376 & chain e")

cmd.select ("Outward", "resi 376 & chain e", merge=1)

cmd.color ("blue", "resi 276 & chain f")

cmd.select ("Outward", "resi 276 & chain f", merge=1)

cmd.color ("blue", "resi 277 & chain f")

cmd.select ("Outward", "resi 277 & chain f", merge=1)

cmd.color ("blue", "resi 278 & chain f")

cmd.select ("Outward", "resi 278 & chain f", merge=1)

cmd.color ("blue", "resi 374 & chain f")

cmd.select ("Outward", "resi 374 & chain f", merge=1)

cmd.color ("blue", "resi 375 & chain f")

cmd.select ("Outward", "resi 375 & chain f", merge=1)

cmd.color ("blue", "resi 376 & chain f")

cmd.select ("Outward", "resi 376 & chain f", merge=1)

cmd.color ("blue", "resi 276 & chain g")

cmd.select ("Outward", "resi 276 & chain g", merge=1)

cmd.color ("blue", "resi 277 & chain g")

cmd.select ("Outward", "resi 277 & chain g", merge=1)

cmd.color ("blue", "resi 278 & chain g")

cmd.select ("Outward", "resi 278 & chain g", merge=1)

cmd.color ("blue", "resi 374 & chain g")

cmd.select ("Outward", "resi 374 & chain g", merge=1)

cmd.color ("blue", "resi 375 & chain g")

cmd.select ("Outward", "resi 375 & chain g", merge=1)

cmd.color ("blue", "resi 376 & chain g")

cmd.select ("Outward", "resi 376 & chain g", merge=1)

cmd.color ("blue", "resi 276 & chain A")

cmd.select ("Outward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 276 & chain B")

cmd.select ("Outward", "resi 276 & chain B", merge=1)

cmd.color ("blue", "resi 277 & chain B")

cmd.select ("Outward", "resi 277 & chain B", merge=1)

cmd.color ("blue", "resi 278 & chain B")

cmd.select ("Outward", "resi 278 & chain B", merge=1)

cmd.color ("blue", "resi 374 & chain B")

cmd.select ("Outward", "resi 374 & chain B", merge=1)

cmd.color ("blue", "resi 375 & chain B")

cmd.select ("Outward", "resi 375 & chain B", merge=1)

cmd.color ("blue", "resi 376 & chain B")

cmd.select ("Outward", "resi 376 & chain B", merge=1)

cmd.color ("blue", "resi 276 & chain C")

cmd.select ("Outward", "resi 276 & chain C", merge=1)

cmd.color ("blue", "resi 277 & chain C")

cmd.select ("Outward", "resi 277 & chain C", merge=1)

cmd.color ("blue", "resi 278 & chain C")

cmd.select ("Outward", "resi 278 & chain C", merge=1)

cmd.color ("blue", "resi 374 & chain C")

cmd.select ("Outward", "resi 374 & chain C", merge=1)

cmd.color ("blue", "resi 375 & chain C")

cmd.select ("Outward", "resi 375 & chain C", merge=1)

cmd.color ("blue", "resi 376 & chain C")

cmd.select ("Outward", "resi 376 & chain C", merge=1)

cmd.color ("blue", "resi 276 & chain D")

cmd.select ("Outward", "resi 276 & chain D", merge=1)

cmd.color ("blue", "resi 277 & chain D")

cmd.select ("Outward", "resi 277 & chain D", merge=1)

cmd.color ("blue", "resi 278 & chain D")

cmd.select ("Outward", "resi 278 & chain D", merge=1)

cmd.color ("blue", "resi 374 & chain D")

cmd.select ("Outward", "resi 374 & chain D", merge=1)

cmd.color ("blue", "resi 375 & chain D")

cmd.select ("Outward", "resi 375 & chain D", merge=1)

cmd.color ("blue", "resi 376 & chain D")

cmd.select ("Outward", "resi 376 & chain D", merge=1)

cmd.color ("blue", "resi 276 & chain E")

cmd.select ("Outward", "resi 276 & chain E", merge=1)

cmd.color ("blue", "resi 277 & chain E")

cmd.select ("Outward", "resi 277 & chain E", merge=1)

cmd.color ("blue", "resi 278 & chain E")

cmd.select ("Outward", "resi 278 & chain E", merge=1)

cmd.color ("blue", "resi 374 & chain E")

cmd.select ("Outward", "resi 374 & chain E", merge=1)

cmd.color ("blue", "resi 375 & chain E")

cmd.select ("Outward", "resi 375 & chain E", merge=1)

cmd.color ("blue", "resi 376 & chain E")

cmd.select ("Outward", "resi 376 & chain E", merge=1)

cmd.color ("blue", "resi 276 & chain F")

cmd.select ("Outward", "resi 276 & chain F", merge=1)

cmd.color ("blue", "resi 277 & chain F")

cmd.select ("Outward", "resi 277 & chain F", merge=1)

cmd.color ("blue", "resi 278 & chain F")

cmd.select ("Outward", "resi 278 & chain F", merge=1)

cmd.color ("blue", "resi 374 & chain F")

cmd.select ("Outward", "resi 374 & chain F", merge=1)

cmd.color ("blue", "resi 375 & chain F")

cmd.select ("Outward", "resi 375 & chain F", merge=1)

cmd.color ("blue", "resi 376 & chain F")

cmd.select ("Outward", "resi 376 & chain F", merge=1)

cmd.color ("blue", "resi 276 & chain G")

cmd.select ("Outward", "resi 276 & chain G", merge=1)

cmd.color ("blue", "resi 277 & chain G")

cmd.select ("Outward", "resi 277 & chain G", merge=1)

cmd.color ("blue", "resi 278 & chain G")

cmd.select ("Outward", "resi 278 & chain G", merge=1)

cmd.color ("blue", "resi 374 & chain G")

cmd.select ("Outward", "resi 374 & chain G", merge=1)

cmd.color ("blue", "resi 375 & chain G")

cmd.select ("Outward", "resi 375 & chain G", merge=1)

cmd.color ("blue", "resi 376 & chain G")

cmd.select ("Outward", "resi 376 & chain G", merge=1)

cmd.color ("blue", "resi 276 & chain H")

cmd.select ("Outward", "resi 276 & chain H", merge=1)

cmd.color ("blue", "resi 277 & chain H")

cmd.select ("Outward", "resi 277 & chain H", merge=1)

cmd.color ("blue", "resi 278 & chain H")

cmd.select ("Outward", "resi 278 & chain H", merge=1)

cmd.color ("blue", "resi 374 & chain H")

cmd.select ("Outward", "resi 374 & chain H", merge=1)

cmd.color ("blue", "resi 375 & chain H")

cmd.select ("Outward", "resi 375 & chain H", merge=1)

cmd.color ("blue", "resi 376 & chain H")

cmd.select ("Outward", "resi 376 & chain H", merge=1)

cmd.color ("blue", "resi 276 & chain I")

cmd.select ("Outward", "resi 276 & chain I", merge=1)

cmd.color ("blue", "resi 277 & chain I")

cmd.select ("Outward", "resi 277 & chain I", merge=1)

cmd.color ("blue", "resi 278 & chain I")

cmd.select ("Outward", "resi 278 & chain I", merge=1)

cmd.color ("blue", "resi 374 & chain I")

cmd.select ("Outward", "resi 374 & chain I", merge=1)

cmd.color ("blue", "resi 375 & chain I")

cmd.select ("Outward", "resi 375 & chain I", merge=1)

cmd.color ("blue", "resi 376 & chain I")

cmd.select ("Outward", "resi 376 & chain I", merge=1)

cmd.color ("blue", "resi 276 & chain J")

cmd.select ("Outward", "resi 276 & chain J", merge=1)

cmd.color ("blue", "resi 277 & chain J")

cmd.select ("Outward", "resi 277 & chain J", merge=1)

cmd.color ("blue", "resi 278 & chain J")

cmd.select ("Outward", "resi 278 & chain J", merge=1)

cmd.color ("blue", "resi 374 & chain J")

cmd.select ("Outward", "resi 374 & chain J", merge=1)

cmd.color ("blue", "resi 375 & chain J")

cmd.select ("Outward", "resi 375 & chain J", merge=1)

cmd.color ("blue", "resi 376 & chain J")

cmd.select ("Outward", "resi 376 & chain J", merge=1)

cmd.color ("blue", "resi 276 & chain K")

cmd.select ("Outward", "resi 276 & chain K", merge=1)

cmd.color ("blue", "resi 277 & chain K")

cmd.select ("Outward", "resi 277 & chain K", merge=1)

cmd.color ("blue", "resi 278 & chain K")

cmd.select ("Outward", "resi 278 & chain K", merge=1)

cmd.color ("blue", "resi 374 & chain K")

cmd.select ("Outward", "resi 374 & chain K", merge=1)

cmd.color ("blue", "resi 375 & chain K")

cmd.select ("Outward", "resi 375 & chain K", merge=1)

cmd.color ("blue", "resi 376 & chain K")

cmd.select ("Outward", "resi 376 & chain K", merge=1)

cmd.color ("blue", "resi 276 & chain L")

cmd.select ("Outward", "resi 276 & chain L", merge=1)

cmd.color ("blue", "resi 277 & chain L")

cmd.select ("Outward", "resi 277 & chain L", merge=1)

cmd.color ("blue", "resi 278 & chain L")

cmd.select ("Outward", "resi 278 & chain L", merge=1)

cmd.color ("blue", "resi 374 & chain L")

cmd.select ("Outward", "resi 374 & chain L", merge=1)

cmd.color ("blue", "resi 375 & chain L")

cmd.select ("Outward", "resi 375 & chain L", merge=1)

cmd.color ("blue", "resi 376 & chain L")

cmd.select ("Outward", "resi 376 & chain L", merge=1)

cmd.color ("blue", "resi 276 & chain M")

cmd.select ("Outward", "resi 276 & chain M", merge=1)

cmd.color ("blue", "resi 277 & chain M")

cmd.select ("Outward", "resi 277 & chain M", merge=1)

cmd.color ("blue", "resi 278 & chain M")

cmd.select ("Outward", "resi 278 & chain M", merge=1)

cmd.color ("blue", "resi 374 & chain M")

cmd.select ("Outward", "resi 374 & chain M", merge=1)

cmd.color ("blue", "resi 375 & chain M")

cmd.select ("Outward", "resi 375 & chain M", merge=1)

cmd.color ("blue", "resi 376 & chain M")

cmd.select ("Outward", "resi 376 & chain M", merge=1)

cmd.color ("blue", "resi 276 & chain N")

cmd.select ("Outward", "resi 276 & chain N", merge=1)

cmd.color ("blue", "resi 277 & chain N")

cmd.select ("Outward", "resi 277 & chain N", merge=1)

cmd.color ("blue", "resi 278 & chain N")

cmd.select ("Outward", "resi 278 & chain N", merge=1)

cmd.color ("blue", "resi 374 & chain N")

cmd.select ("Outward", "resi 374 & chain N", merge=1)

cmd.color ("blue", "resi 375 & chain N")

cmd.select ("Outward", "resi 375 & chain N", merge=1)

cmd.color ("blue", "resi 376 & chain N")

cmd.select ("Outward", "resi 376 & chain N", merge=1)

cmd.color ("blue", "resi 276 & chain O")

cmd.select ("Outward", "resi 276 & chain O", merge=1)

cmd.color ("blue", "resi 277 & chain O")

cmd.select ("Outward", "resi 277 & chain O", merge=1)

cmd.color ("blue", "resi 278 & chain O")

cmd.select ("Outward", "resi 278 & chain O", merge=1)

cmd.color ("blue", "resi 374 & chain O")

cmd.select ("Outward", "resi 374 & chain O", merge=1)

cmd.color ("blue", "resi 375 & chain O")

cmd.select ("Outward", "resi 375 & chain O", merge=1)

cmd.color ("blue", "resi 376 & chain O")

cmd.select ("Outward", "resi 376 & chain O", merge=1)

cmd.color ("blue", "resi 276 & chain P")

cmd.select ("Outward", "resi 276 & chain P", merge=1)

cmd.color ("blue", "resi 277 & chain P")

cmd.select ("Outward", "resi 277 & chain P", merge=1)

cmd.color ("blue", "resi 278 & chain P")

cmd.select ("Outward", "resi 278 & chain P", merge=1)

cmd.color ("blue", "resi 374 & chain P")

cmd.select ("Outward", "resi 374 & chain P", merge=1)

cmd.color ("blue", "resi 375 & chain P")

cmd.select ("Outward", "resi 375 & chain P", merge=1)

cmd.color ("blue", "resi 376 & chain P")

cmd.select ("Outward", "resi 376 & chain P", merge=1)

cmd.color ("blue", "resi 276 & chain Q")

cmd.select ("Outward", "resi 276 & chain Q", merge=1)

cmd.color ("blue", "resi 277 & chain Q")

cmd.select ("Outward", "resi 277 & chain Q", merge=1)

cmd.color ("blue", "resi 278 & chain Q")

cmd.select ("Outward", "resi 278 & chain Q", merge=1)

cmd.color ("blue", "resi 374 & chain Q")

cmd.select ("Outward", "resi 374 & chain Q", merge=1)

cmd.color ("blue", "resi 375 & chain Q")

cmd.select ("Outward", "resi 375 & chain Q", merge=1)

cmd.color ("blue", "resi 376 & chain Q")

cmd.select ("Outward", "resi 376 & chain Q", merge=1)

cmd.color ("blue", "resi 276 & chain R")

cmd.select ("Outward", "resi 276 & chain R", merge=1)

cmd.color ("blue", "resi 277 & chain R")

cmd.select ("Outward", "resi 277 & chain R", merge=1)

cmd.color ("blue", "resi 278 & chain R")

cmd.select ("Outward", "resi 278 & chain R", merge=1)

cmd.color ("blue", "resi 374 & chain R")

cmd.select ("Outward", "resi 374 & chain R", merge=1)

cmd.color ("blue", "resi 375 & chain R")

cmd.select ("Outward", "resi 375 & chain R", merge=1)

cmd.color ("blue", "resi 376 & chain R")

cmd.select ("Outward", "resi 376 & chain R", merge=1)

cmd.color ("blue", "resi 276 & chain S")

cmd.select ("Outward", "resi 276 & chain S", merge=1)

cmd.color ("blue", "resi 277 & chain S")

cmd.select ("Outward", "resi 277 & chain S", merge=1)

cmd.color ("blue", "resi 278 & chain S")

cmd.select ("Outward", "resi 278 & chain S", merge=1)

cmd.color ("blue", "resi 374 & chain S")

cmd.select ("Outward", "resi 374 & chain S", merge=1)

cmd.color ("blue", "resi 375 & chain S")

cmd.select ("Outward", "resi 375 & chain S", merge=1)

cmd.color ("blue", "resi 376 & chain S")

cmd.select ("Outward", "resi 376 & chain S", merge=1)

cmd.color ("blue", "resi 276 & chain T")

cmd.select ("Outward", "resi 276 & chain T", merge=1)

cmd.color ("blue", "resi 277 & chain T")

cmd.select ("Outward", "resi 277 & chain T", merge=1)

cmd.color ("blue", "resi 278 & chain T")

cmd.select ("Outward", "resi 278 & chain T", merge=1)

cmd.color ("blue", "resi 374 & chain T")

cmd.select ("Outward", "resi 374 & chain T", merge=1)

cmd.color ("blue", "resi 375 & chain T")

cmd.select ("Outward", "resi 375 & chain T", merge=1)

cmd.color ("blue", "resi 376 & chain T")

cmd.select ("Outward", "resi 376 & chain T", merge=1)

cmd.color ("blue", "resi 276 & chain U")

cmd.select ("Outward", "resi 276 & chain U", merge=1)

cmd.color ("blue", "resi 277 & chain U")

cmd.select ("Outward", "resi 277 & chain U", merge=1)

cmd.color ("blue", "resi 278 & chain U")

cmd.select ("Outward", "resi 278 & chain U", merge=1)

cmd.color ("blue", "resi 374 & chain U")

cmd.select ("Outward", "resi 374 & chain U", merge=1)

cmd.color ("blue", "resi 375 & chain U")

cmd.select ("Outward", "resi 375 & chain U", merge=1)

cmd.color ("blue", "resi 376 & chain U")

cmd.select ("Outward", "resi 376 & chain U", merge=1)

cmd.color ("blue", "resi 276 & chain V")

cmd.select ("Outward", "resi 276 & chain V", merge=1)

cmd.color ("blue", "resi 277 & chain V")

cmd.select ("Outward", "resi 277 & chain V", merge=1)

cmd.color ("blue", "resi 278 & chain V")

cmd.select ("Outward", "resi 278 & chain V", merge=1)

cmd.color ("blue", "resi 374 & chain V")

cmd.select ("Outward", "resi 374 & chain V", merge=1)

cmd.color ("blue", "resi 375 & chain V")

cmd.select ("Outward", "resi 375 & chain V", merge=1)

cmd.color ("blue", "resi 376 & chain V")

cmd.select ("Outward", "resi 376 & chain V", merge=1)

cmd.color ("blue", "resi 276 & chain W")

cmd.select ("Outward", "resi 276 & chain W", merge=1)

cmd.color ("blue", "resi 277 & chain W")

cmd.select ("Outward", "resi 277 & chain W", merge=1)

cmd.color ("blue", "resi 278 & chain W")

cmd.select ("Outward", "resi 278 & chain W", merge=1)

cmd.color ("blue", "resi 374 & chain W")

cmd.select ("Outward", "resi 374 & chain W", merge=1)

cmd.color ("blue", "resi 375 & chain W")

cmd.select ("Outward", "resi 375 & chain W", merge=1)

cmd.color ("blue", "resi 376 & chain W")

cmd.select ("Outward", "resi 376 & chain W", merge=1)

cmd.color ("blue", "resi 276 & chain X")

cmd.select ("Outward", "resi 276 & chain X", merge=1)

cmd.color ("blue", "resi 277 & chain X")

cmd.select ("Outward", "resi 277 & chain X", merge=1)

cmd.color ("blue", "resi 278 & chain X")

cmd.select ("Outward", "resi 278 & chain X", merge=1)

cmd.color ("blue", "resi 374 & chain X")

cmd.select ("Outward", "resi 374 & chain X", merge=1)

cmd.color ("blue", "resi 375 & chain X")

cmd.select ("Outward", "resi 375 & chain X", merge=1)

cmd.color ("blue", "resi 376 & chain X")

cmd.select ("Outward", "resi 376 & chain X", merge=1)

cmd.color ("blue", "resi 276 & chain Y")

cmd.select ("Outward", "resi 276 & chain Y", merge=1)

cmd.color ("blue", "resi 277 & chain Y")

cmd.select ("Outward", "resi 277 & chain Y", merge=1)

cmd.color ("blue", "resi 278 & chain Y")

cmd.select ("Outward", "resi 278 & chain Y", merge=1)

cmd.color ("blue", "resi 374 & chain Y")

cmd.select ("Outward", "resi 374 & chain Y", merge=1)

cmd.color ("blue", "resi 375 & chain Y")

cmd.select ("Outward", "resi 375 & chain Y", merge=1)

cmd.color ("blue", "resi 376 & chain Y")

cmd.select ("Outward", "resi 376 & chain Y", merge=1)

cmd.color ("blue", "resi 276 & chain Z")

cmd.select ("Outward", "resi 276 & chain Z", merge=1)

cmd.color ("blue", "resi 277 & chain Z")

cmd.select ("Outward", "resi 277 & chain Z", merge=1)

cmd.color ("blue", "resi 278 & chain Z")

cmd.select ("Outward", "resi 278 & chain Z", merge=1)

cmd.color ("blue", "resi 374 & chain Z")

cmd.select ("Outward", "resi 374 & chain Z", merge=1)

cmd.color ("blue", "resi 375 & chain Z")

cmd.select ("Outward", "resi 375 & chain Z", merge=1)

cmd.color ("blue", "resi 376 & chain Z")

cmd.select ("Outward", "resi 376 & chain Z", merge=1)

cmd.load_cgo( [9.0, 177.55002,177.55441,147.96214, 177.55118, 177.55116, 142.66772, 1, 1,1,0,0,0,1], "axis" )
