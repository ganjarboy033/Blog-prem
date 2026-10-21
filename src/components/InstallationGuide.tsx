import React from 'react';
import { HelpCircle, CheckCircle2, AlertTriangle, ArrowRight, Smartphone, ShieldCheck, ExternalLink, Sparkles } from 'lucide-react';

export const InstallationGuide: React.FC = () => {
  const steps = [
    {
      num: 1,
      title: 'Salin atau Unduh Kode XML',
      desc: 'Klik tombol "Salin Seluruh Kode" atau "Unduh .XML" di bagian atas aplikasi ini. Anda akan mendapatkan seluruh kode XML master yang sudah di-merge sempurna.'
    },
    {
      num: 2,
      title: 'Buka Dashboard Blogger',
      desc: 'Kunjungi situs https://www.blogger.com lalu pilih blog yang ingin Anda pasang template ini.'
    },
    {
      num: 3,
      title: 'Masuk ke Menu Tema',
      desc: 'Di bilah menu navigasi sebelah kiri, klik menu "Tema" (Theme).'
    },
    {
      num: 4,
      title: 'Pilih Opsi "Edit HTML"',
      desc: 'Di sebelah tombol oranye "Sesuaikan", klik tanda panah ke bawah (⌄) lalu pilih menu "Edit HTML". Anda akan melihat editor kode Blogger.'
    },
    {
      num: 5,
      title: 'Hapus Seluruh Kode Lama & Tempel Kode Baru',
      desc: 'Klik di dalam editor kode, tekan Ctrl+A (pilih semua kode lama), lalu tekan tombol Backspace/Delete hingga bersih. Setelah itu, tekan Ctrl+V (Paste) seluruh kode XML master dari aplikasi ini.'
    },
    {
      num: 6,
      title: 'Klik Tombol Simpan (Ikon Disket)',
      desc: 'Klik tombol Simpan (ikon disket di pojok kanan atas editor). Tunggu hingga muncul notifikasi "Pembaruan Berhasil".'
    },
    {
      num: 7,
      title: 'Selesai & Buka Blog Anda!',
      desc: 'Buka blog Anda di tab baru. Seluruh fitur canggih: Story status, 3D Coverflow slider, Marketplace snap scroll, Galeri 4-kolom, kolom komentar modern, dan musik lofi langsung aktif!'
    }
  ];

  return (
    <div className="w-full max-w-4xl mx-auto px-4 py-6">
      {/* Header Info */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl mb-6">
        <div className="flex items-center gap-3 mb-2">
          <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
            <HelpCircle className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-white">Panduan Lengkap Pemasangan di Blogger</h2>
            <p className="text-xs sm:text-sm text-slate-400">
              Ikuti langkah mudah di bawah ini untuk memasang template XML hasil merge tanpa risiko error.
            </p>
          </div>
        </div>
      </div>

      {/* Step by Step Visual Guide */}
      <div className="space-y-4 mb-8">
        {steps.map((s) => (
          <div
            key={s.num}
            className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 sm:p-5 flex items-start gap-4 transition-all hover:border-slate-700 shadow-md"
          >
            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-600 text-white font-extrabold flex items-center justify-center text-sm shrink-0 shadow-lg shadow-cyan-500/20">
              {s.num}
            </div>
            <div className="space-y-1">
              <h3 className="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                <span>{s.title}</span>
              </h3>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {s.desc}
              </p>
            </div>
          </div>
        ))}
      </div>

      {/* Critical Setting Checklist */}
      <div className="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-5 mb-8 shadow-xl">
        <div className="flex items-center gap-2.5 text-amber-400 font-bold text-sm mb-3">
          <AlertTriangle className="w-5 h-5" />
          <span>Pengaturan Wajib di Dashboard Blogger (PENTING!)</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
          <div className="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
            <div className="font-bold text-white mb-1 flex items-center gap-1.5">
              <Smartphone className="w-4 h-4 text-cyan-400" />
              1. Nonaktifkan Template Seluler Bawaan
            </div>
            <p className="text-slate-400 text-[11px] leading-relaxed">
              Di menu <b>Tema</b> &gt; Klik tanda panah (⌄) di samping tombol Sesuaikan &gt; Pilih <b>Setelan Seluler</b> &gt; Pilih opsi <b>"Desktop"</b> lalu Simpan. Template ini sudah 100% responsif mobile-first, sehingga tidak butuh template seluler default Blogger yang kaku.
            </p>
          </div>

          <div className="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
            <div className="font-bold text-white mb-1 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              2. Aktifkan Pengalihan HTTPS
            </div>
            <p className="text-slate-400 text-[11px] leading-relaxed">
              Buka menu <b>Setelan</b> (Settings) Blogger &gt; Gulir ke bagian <b>HTTPS</b> &gt; Aktifkan <b>"Ketersediaan HTTPS"</b> dan <b>"Pengalihan HTTPS"</b> agar musik Lofi, IndexedDB Stories, dan FontAwesome berfungsi aman tanpa peringatan konten campuran.
            </p>
          </div>
        </div>
      </div>

      {/* Frequently Asked Questions */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
        <h3 className="text-base font-bold text-white flex items-center gap-2">
          <Sparkles className="w-4 h-4 text-cyan-400" />
          <span>Pertanyaan yang Sering Diajukan (FAQ)</span>
        </h3>

        <div className="space-y-3 text-xs sm:text-sm">
          <div className="border-b border-slate-800 pb-3">
            <h4 className="font-semibold text-cyan-300 mb-1">
              Bagaimana cara kerja sinkronisasi postingan baru?
            </h4>
            <p className="text-slate-400 text-xs">
              Setiap kali Anda membuat postingan baru di Blogger, template akan otomatis mengambilnya melalui Blogger JSON feed API (<code className="text-cyan-400">/feeds/posts/default</code>). Postingan tersebut langsung tampil di 3D Slider, Marketplace, dan Galeri 4-Kolom secara instan tanpa perlu edit kode!
            </p>
          </div>

          <div className="border-b border-slate-800 pb-3">
            <h4 className="font-semibold text-cyan-300 mb-1">
              Bagaimana jika saya ingin mengganti foto avatar profil?
            </h4>
            <p className="text-slate-400 text-xs">
              Gunakan tab <b>Kustomisasi Cepat</b> di studio ini, tempelkan tautan URL gambar avatar Anda di kolom URL Avatar, lalu unduh atau salin kembali kode XML-nya. Atau cari class <code className="text-cyan-400">.avatar-img</code> di dalam kode XML dan ganti URL atribut <code className="text-cyan-400">src</code>-nya.
            </p>
          </div>

          <div>
            <h4 className="font-semibold text-cyan-300 mb-1">
              Apakah fitur video &amp; foto story hingga 100MB membebani kuota hosting Blogger?
            </h4>
            <p className="text-slate-400 text-xs">
              Tidak sama sekali! Fitur story status menggunakan teknologi browser <b>IndexedDB lokal (BlogStoryDB)</b>. File video maupun foto tersimpan dengan performa tinggi langsung di peramban tanpa memakan kuota server hosting Blogger Anda.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
