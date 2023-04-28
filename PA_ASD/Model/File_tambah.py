from Control.Control_Admin import Anime
from Model.Pemutaran import Pemutaran


mutar = Pemutaran()
admin = Anime()
admin.tambah_Anime("Black Clover","5")
admin.tambah_Anime("Fate Series","5")
admin.tambah_Anime("Haikyu","5")
admin.tambah_Anime("Naruto","5")
admin.tambah_Anime("One Piece","5")

mutar.append_blackclover('pict/black_clover/blackclover_1.mp4', 'pict/black_clover/blackclover_1.mp3')
mutar.append_blackclover('pict/black_clover/blackclover_2.mp4', 'pict/black_clover/blackclover_2.mp3')
mutar.append_blackclover('pict/black_clover/blackclover_3.mp4', 'pict/black_clover/blackclover_3.mp3')
mutar.append_blackclover('pict/black_clover/blackclover_4.mp4', 'pict/black_clover/blackclover_4.mp3')
mutar.append_blackclover('pict/black_clover/blackclover_5.mp4', 'pict/black_clover/blackclover_5.mp3')

mutar.append_fateseries('pict/fate_series/fate_1.mp4', 'pict/fate_series/fate_1.mp3')
mutar.append_fateseries('pict/fate_series/fate_2.mp4', 'pict/fate_series/fate_2.mp3')
mutar.append_fateseries('pict/fate_series/fate_3.mp4', 'pict/fate_series/fate_3.mp3')
mutar.append_fateseries('pict/fate_series/fate_4.mp4', 'pict/fate_series/fate_4.mp3')
mutar.append_fateseries('pict/fate_series/fate_5.mp4', 'pict/fate_series/fate_5.mp3')

mutar.append_haikyu('pict/haikyu/haikyu_1.mp4', 'pict/haikyu/haikyu_1.mp3')
mutar.append_haikyu('pict/haikyu/haikyu_2.mp4', 'pict/haikyu/haikyu_2.mp3')
mutar.append_haikyu('pict/haikyu/haikyu_3.mp4', 'pict/haikyu/haikyu_3.mp3')
mutar.append_haikyu('pict/haikyu/haikyu_4.mp4', 'pict/haikyu/haikyu_4.mp3')
mutar.append_haikyu('pict/haikyu/haikyu_5.mp4', 'pict/haikyu/haikyu_5.mp3')

mutar.append_naruto('pict/naruto/naruto_1.mp4', 'pict/naruto/naruto_1.mp3')
mutar.append_naruto('pict/naruto/naruto_2.mp4', 'pict/naruto/naruto_2.mp3')
mutar.append_naruto('pict/naruto/naruto_3.mp4', 'pict/naruto/naruto_3.mp3')
mutar.append_naruto('pict/naruto/naruto_4.mp4', 'pict/naruto/naruto_4.mp3')
mutar.append_naruto('pict/naruto/naruto_5.mp4', 'pict/naruto/naruto_5.mp3')

mutar.append_onepiece('pict/one_piece/onepiece_1.mp4', 'pict/one_piece/onepiece_1.mp3')
mutar.append_onepiece('pict/one_piece/onepiece_2.mp4', 'pict/one_piece/onepiece_2.mp3')
mutar.append_onepiece('pict/one_piece/onepiece_3.mp4', 'pict/one_piece/onepiece_3.mp3')
mutar.append_onepiece('pict/one_piece/onepiece_4.mp4', 'pict/one_piece/onepiece_4.mp3')
mutar.append_onepiece('pict/one_piece/onepiece_5.mp4', 'pict/one_piece/onepiece_5.mp3')

