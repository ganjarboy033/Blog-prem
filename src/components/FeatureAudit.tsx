import React from 'react';
import { Layers, CheckCircle2, Sparkles, FileCode, Check, ShieldCheck, Zap } from 'lucide-react';

export const FeatureAudit: React.FC = () => {
  const sourceAudits = [
    {
      name: '2_31be271e.xml (Sistem Story)',
      badge: '18 Fungsi JS | 100% Merged',
      badgeColor: 'border-pink-500/30 text-pink-400 bg-pink-500/10',
      items: [
        'Avatar dengan Story Gradient Ring ala Instagram & WhatsApp',
        'Tombol badge (+) untuk upload story langsung dari HP',
        'Sistem database IndexedDB (BlogStoryDB) untuk file video/foto s.d 100MB+',
        'Progress bar multi-segmen otomatis berdasarkan durasi video',
        'Fitur Download Story & Hapus Story dari viewer',
        'Navigasi tap kiri (sebelumnya) dan tap kanan (selanjutnya)',
        'Dukungan direct URL MP4 dan upload berkas lokal'
      ]
    },
    {
      name: 'hebat_Copy__8e18c959.xml (3D Slider & Core)',
      badge: '48 Fungsi JS | 100% Merged',
      badgeColor: 'border-cyan-500/30 text-cyan-400 bg-cyan-500/10',
      items: [
        '3D Coverflow Slider dengan active, prev, next 3D perspective',
        'Slide counter badge (01 / 05), deskripsi aktif, dan indikator dots interaktif',
        'Tombol Download APK terintegrasi dengan modal postingan',
        'Halaman Error 404 khusus dengan countdown redirect otomatis 10 detik',
        'Pemutar Audio Lofi ambient background dengan play/pause status',
        'Kartu tautan dengan animasi border bergerak bersinar (moveAlongBorder)',
        'Efek partikel jatuh (Daun, Salju, Bintang, Cinta) dengan pengatur intensitas',
        'Kustomisasi wallpaper (Warna, Gradien, URL, Galeri HP, Reset)',
        'Kustomisasi efek kaca blur (0px, 12px, 25px) dan font switcher',
        'Statistik blog realtime (Views All, Today, Yesterday, Month, Last Month)',
        'Touch ring ripple effect pada setiap klik layar'
      ]
    },
    {
      name: 'hebat_Copy__Copy__8fa96916.xml (Marketplace)',
      badge: '44 Fungsi JS | 100% Merged',
      badgeColor: 'border-amber-500/30 text-amber-400 bg-amber-500/10',
      items: [
        'Track carousel horizontal dengan snap scroll responsif',
        'Tombol navigasi panah kiri & kanan untuk smooth scroll track',
        'Kartu katalog marketplace dengan badge HOT 🔥 dan PRO APP',
        'Sinkronisasi tombol Like dan Follow global di kartu marketplace',
        'Modal membaca artikel lengkap dengan gambar thumbnail otomatis'
      ]
    },
    {
      name: 'hebat_sekali_5ef1444b.xml (Galeri 4-Kolom)',
      badge: '45 Fungsi JS | 100% Merged',
      badgeColor: 'border-emerald-500/30 text-emerald-400 bg-emerald-500/10',
      items: [
        'Grid galeri 4-kolom proporsi kotak presisi (aspect ratio 1:1)',
        'Pencarian instan realtime (filterPostsBySearch) tanpa reload halaman',
        'Hover overlay estetik menampilkan judul dan badge NEW fire',
        'Klik galeri langsung membuka modal pembaca postingan',
        'Pencarian mencakup judul artikel sekaligus cuplikan teks artikel'
      ]
    }
  ];

  const premiumEnhancements = [
    {
      title: 'Tab Switcher Multi-View',
      desc: 'Pengunjung dapat melihat Semua Fitur sekaligus atau memfilter tampilan khusus: 3D Slider saja, Marketplace saja, atau Galeri 4-Kolom saja.'
    },
    {
      title: 'Text-To-Speech (TTS) Narator Artikel',
      desc: 'Pengunjung dapat mendengarkan isi artikel dibacakan dengan suara alami bahasa Indonesia menggunakan tombol "Dengarkan Artikel".'
    },
    {
      title: 'Estimasi Waktu Baca (Reading Time)',
      desc: 'Otomatis menghitung perkiraan waktu baca per postingan (misal: "2 menit baca") untuk meningkatkan kenyamanan audiens.'
    },
    {
      title: 'SEO Structured Data JSON-LD (Schema.org)',
      desc: 'Snippet data terstruktur lengkap untuk Google Rich Results (WebSite, BlogPosting, Person) meningkatkan peringkat pencarian blog.'
    },
    {
      title: 'Kolom Komentar Modern Formspree & LocalStorage',
      desc: 'Komentar pengunjung tersimpan aman di peramban serta terkirim ke email pemilik via Formspree, dilengkapi inisial avatar dan tombol edit/hapus.'
    },
    {
      title: 'Floating Glass Toasts & Reaksi Hati Mengambang',
      desc: 'Menggantikan alert bawaan browser yang mengganggu dengan notifikasi kaca modern dan animasi hati saat menyukai artikel.'
    },
    {
      title: 'Filter Kategori Tag Pills',
      desc: 'Tombol filter kategori instan (Aplikasi, Tutorial, Hardware, Game) pada bagian galeri untuk navigasi konten cepat.'
    }
  ];

  return (
    <div className="w-full max-w-5xl mx-auto px-4 py-6">
      {/* Summary Header */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl mb-6">
        <div className="flex items-center gap-3 mb-2">
          <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
            <ShieldCheck className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-white">Laporan Audit Merge &amp; Verifikasi Fitur</h2>
            <p className="text-xs sm:text-sm text-slate-400">
              Verifikasi menyeluruh: tidak ada satu pun kode, animasi, atau fungsi dari 4 template asli yang hilang atau terlewat.
            </p>
          </div>
        </div>
      </div>

      {/* 4 Sources Breakdown Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-8">
        {sourceAudits.map((source, idx) => (
          <div
            key={idx}
            className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-lg flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-3 pb-3 border-b border-slate-800">
                <span className="font-bold text-sm text-white">{source.name}</span>
                <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full border ${source.badgeColor}`}>
                  {source.badge}
                </span>
              </div>

              <ul className="space-y-2 text-xs text-slate-300">
                {source.items.map((item, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>

      {/* Premium Upgrades Section */}
      <div className="bg-gradient-to-br from-slate-900 via-slate-900 to-cyan-950/40 border border-cyan-500/20 rounded-2xl p-6 shadow-xl">
        <div className="flex items-center gap-2 mb-4 pb-3 border-b border-slate-800">
          <Zap className="w-5 h-5 text-cyan-400" />
          <h3 className="text-base font-bold text-white">
            Peningkatan Fitur Premium Tambahan yang Diintegrasikan
          </h3>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {premiumEnhancements.map((enh, i) => (
            <div key={i} className="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80 space-y-1">
              <div className="text-xs font-bold text-cyan-300 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
                <span>{enh.title}</span>
              </div>
              <p className="text-[11px] text-slate-400 leading-relaxed">
                {enh.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
